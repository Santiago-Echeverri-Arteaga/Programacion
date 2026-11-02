"""Cliente HTTP proporcionado: descargar o leer la misma respuesta congelada.
No requiere Pandas ni CSV intermedio. La transaccion incluye Bronze y Silver.
"""
from pathlib import Path
import argparse
from datetime import date, timedelta
import hashlib
import json
import math
import os
from urllib.request import urlopen
from urllib.parse import parse_qs, urlparse
import psycopg

RAIZ = Path(__file__).resolve().parents[1]
VARIABLES = ('temperature_2m_max', 'temperature_2m_min', 'precipitation_sum')


def filas_respuesta(respuesta, url):
    """Comprueba contrato de transporte; SQL comprueba integridad fisica."""
    if respuesta.get('error'):
        raise ValueError(respuesta.get('reason', 'Error API'))
    if respuesta.get('timezone') != 'America/Bogota' or respuesta.get('utc_offset_seconds') != -18000:
        raise ValueError('Zona horaria inesperada')
    unidades = respuesta['daily_units']
    if [unidades[v] for v in VARIABLES] != ['°C', '°C', 'mm']:
        raise ValueError('Unidades inesperadas')
    diario = respuesta['daily']
    parametros = parse_qs(urlparse(url).query)
    inicio = date.fromisoformat(parametros['start_date'][0])
    fin = date.fromisoformat(parametros['end_date'][0])
    esperadas = [(inicio + timedelta(days=i)).isoformat() for i in range((fin-inicio).days+1)]
    if diario['time'] != esperadas:
        raise ValueError('Fechas incompletas, repetidas o fuera de orden')
    if any(len(diario[v]) != len(esperadas) for v in VARIABLES):
        raise ValueError('Longitudes incompatibles')
    filas = []
    for i, fecha in enumerate(esperadas):
        valores = [diario[v][i] for v in VARIABLES]
        if any(v is not None and (type(v) not in (int, float) or not math.isfinite(v)) for v in valores):
            raise ValueError('Valor no numerico o no finito')
        filas.append((date.fromisoformat(fecha), *valores))
    return filas


def cargar(fase, modo, dbname):
    manifiesto = json.loads((RAIZ/'datos/procedencia.json').read_text(encoding='utf-8'))
    lotes = []
    # Descargar todo antes de abrir la transaccion evita esperar a la red con bloqueos.
    for entrada in manifiesto['archivos']:
        if entrada['fase'] != fase:
            continue
        if modo == 'offline':
            contenido = (RAIZ/'datos'/entrada['archivo']).read_bytes()
            if hashlib.sha256(contenido).hexdigest() != entrada['sha256']:
                raise ValueError('La copia congelada no coincide con su SHA-256')
        else:
            with urlopen(entrada['url'], timeout=45) as respuesta:
                contenido = respuesta.read()
        filas = filas_respuesta(json.loads(contenido), entrada['url'])
        huella = hashlib.sha256(contenido).hexdigest()
        lotes.extend((entrada['ciudad_id'], *f, entrada['url'], huella) for f in filas)
    if len(lotes) == 0:
        raise ValueError('No hay lotes para la fase')
    # Sin host: socket local en Ubuntu y autenticacion peer. PG* permite otra conexion.
    with psycopg.connect(dbname=dbname) as con:
        antes = con.execute('SELECT COUNT(*) FROM silver.observaciones').fetchone()[0]
        with con.cursor() as cur:
            cur.executemany('''INSERT INTO bronze.observaciones
                (ciudad_id,fecha,tmax_c,tmin_c,precipitacion_mm,fuente_url,sha256)
                VALUES (%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (ciudad_id,fecha) DO NOTHING''', lotes)
        con.execute((RAIZ/'ampliacion/02_resumir.sql').read_text(encoding='utf-8'))
        despues = con.execute('SELECT COUNT(*) FROM silver.observaciones').fetchone()[0]
    # El contexto confirma al terminar; ante excepcion revierte ambas etapas.
    print(f'{fase}: recibidas={len(lotes)}, antes={antes}, despues={despues}, nuevas={despues-antes}')
    return antes, despues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fase', choices=['inicial','actualizacion'], required=True)
    parser.add_argument('--modo', choices=['online','offline'], default='offline')
    parser.add_argument('--db', default=os.environ.get('PGDATABASE','curso_datos'))
    args = parser.parse_args()
    cargar(args.fase, args.modo, args.db)


if __name__ == '__main__':
    main()
