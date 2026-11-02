"""Ingesta del observatorio, organizada en cuatro pasos.

Bash proporciona MODO_DATOS, FASE_DATOS y PGDATABASE mediante export.
Sin esas variables: offline, inicial y curso_datos. No hay opciones --fase/--modo.
JSON sigue siendo necesario: es el formato que entrega la API, no un lenguaje
que los estudiantes deban aprender a analizar manualmente.
Ejemplos de cada herramienta nueva: carpeta ejemplos/.
"""
from pathlib import Path
from datetime import date, timedelta
from urllib.request import urlopen
import hashlib
import json
import math
import os
import sys
import psycopg

# __file__ es este archivo; parent es la carpeta que lo contiene.
CARPETA_SCRIPT = Path(__file__).resolve().parent
RAIZ = CARPETA_SCRIPT.parent
VARIABLES = ['temperature_2m_max', 'temperature_2m_min', 'precipitation_sum']


def leer_respuesta(entrada, modo):
    """Paso 1: obtener los mismos bytes desde disco o desde internet."""
    if modo == 'offline':
        ruta = RAIZ / 'datos' / entrada['archivo']
        contenido = ruta.read_bytes()
        huella = hashlib.sha256(contenido).hexdigest()
        if huella != entrada['sha256']:
            raise ValueError('La copia congelada cambió: revisa su SHA-256')
    else:
        # with cierra la respuesta incluso si ocurre un error.
        with urlopen(entrada['url'], timeout=45) as respuesta_http:
            contenido = respuesta_http.read()
        huella = hashlib.sha256(contenido).hexdigest()

    # json.loads convierte JSON en diccionarios y listas de Python.
    respuesta = json.loads(contenido)
    return respuesta, huella


def filas_respuesta(respuesta, fecha_inicio, fecha_fin):
    """Paso 2: comprobar la respuesta y convertir sus listas en filas."""
    if respuesta.get('error'):
        raise ValueError(respuesta.get('reason', 'Error de la API'))
    if respuesta['timezone'] != 'America/Bogota':
        raise ValueError('Zona horaria inesperada')
    if respuesta['utc_offset_seconds'] != -18000:
        raise ValueError('Desplazamiento horario inesperado')

    unidades = respuesta['daily_units']
    if unidades['temperature_2m_max'] != '°C':
        raise ValueError('Unidad de temperatura máxima inesperada')
    if unidades['temperature_2m_min'] != '°C':
        raise ValueError('Unidad de temperatura mínima inesperada')
    if unidades['precipitation_sum'] != 'mm':
        raise ValueError('Unidad de precipitación inesperada')

    # Las fechas están escritas explícitamente en el manifiesto.
    # No se extraen de una URL ni se manipulan como fragmentos de texto.
    inicio = date.fromisoformat(fecha_inicio)
    fin = date.fromisoformat(fecha_fin)
    fechas_esperadas = []
    dia = inicio
    while dia <= fin:
        fechas_esperadas.append(dia.isoformat())
        dia = dia + timedelta(days=1)

    diario = respuesta['daily']
    if diario['time'] != fechas_esperadas:
        raise ValueError('Fechas incompletas, repetidas o fuera de orden')
    cantidad = len(fechas_esperadas)
    for variable in VARIABLES:
        if len(diario[variable]) != cantidad:
            raise ValueError('Las columnas no tienen la misma longitud')
        for valor in diario[variable]:
            # None representa una ausencia real; no se reemplaza por cero.
            if valor is not None:
                if type(valor) not in (int, float):
                    raise ValueError('Se esperaba un número o None')
                if not math.isfinite(valor):
                    raise ValueError('Se recibió un número no finito')

    filas = []
    for i in range(cantidad):
        fecha = date.fromisoformat(diario['time'][i])
        maxima = diario['temperature_2m_max'][i]
        minima = diario['temperature_2m_min'][i]
        lluvia = diario['precipitation_sum'][i]
        filas.append((fecha, maxima, minima, lluvia))
    return filas


def guardar(lotes, dbname):
    """Paso 3: guardar Bronze y preparar Silver en una misma transacción."""
    insertar = '''INSERT INTO bronze.observaciones
        (ciudad_id,fecha,tmax_c,tmin_c,precipitacion_mm,fuente_url,sha256)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (ciudad_id,fecha) DO NOTHING'''
    preparar = (CARPETA_SCRIPT / '02_resumir.sql').read_text(encoding='utf-8')

    # Al salir sin error confirma; si hay una excepción, revierte las escrituras.
    # No se abre conexión HTTP mientras esta transacción está en curso.
    with psycopg.connect(dbname=dbname) as conexion:
        with conexion.cursor() as cursor:
            cursor.execute('SELECT COUNT(*) FROM silver.observaciones')
            antes = cursor.fetchone()[0]
            for fila in lotes:
                # SQL y valores separados: nunca concatenar valores dentro del SQL.
                cursor.execute(insertar, fila)
            cursor.execute(preparar)
            cursor.execute('SELECT COUNT(*) FROM silver.observaciones')
            despues = cursor.fetchone()[0]
    return antes, despues


def cargar(fase, modo, dbname):
    """Paso 4: coordinar funciones, sin analizar argumentos de terminal."""
    if fase not in ['inicial', 'actualizacion']:
        raise ValueError('FASE_DATOS debe ser inicial o actualizacion')
    if modo not in ['offline', 'online']:
        raise ValueError('MODO_DATOS debe ser offline u online')

    texto = (RAIZ / 'datos' / 'procedencia.json').read_text(encoding='utf-8')
    manifiesto = json.loads(texto)
    lotes = []
    for entrada in manifiesto['archivos']:
        if entrada['fase'] == fase:
            respuesta, huella = leer_respuesta(entrada, modo)
            filas = filas_respuesta(respuesta, entrada['fecha_inicio'], entrada['fecha_fin'])
            for fecha, maxima, minima, lluvia in filas:
                fila = (entrada['ciudad_id'], fecha, maxima, minima, lluvia,
                        entrada['url'], huella)
                lotes.append(fila)

    if len(lotes) == 0:
        raise ValueError('No hay registros para esta fase')
    antes, despues = guardar(lotes, dbname)
    nuevas = despues - antes
    print(f'{fase}: recibidas={len(lotes)}, antes={antes}, despues={despues}, nuevas={nuevas}')
    return antes, despues


# Este bloque se ejecuta al lanzar el archivo; no al importarlo para una prueba.
if __name__ == '__main__':
    # sys.argv contiene el nombre del programa y las palabras añadidas al ejecutarlo.
    if len(sys.argv) != 1:
        raise ValueError('Este programa no recibe opciones: usa export o ejecuta pipeline.sh')
    modo = os.environ.get('MODO_DATOS', 'offline')
    fase = os.environ.get('FASE_DATOS', 'inicial')
    base = os.environ.get('PGDATABASE', 'curso_datos')
    cargar(fase, modo, base)
