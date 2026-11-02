"""Recupera Gold directamente con Psycopg; Pandas analiza el resultado reducido."""
from pathlib import Path
import argparse
import json
import os
import numpy as np
import pandas as pd
import psycopg
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parents[1]


def informar(carpeta, dbname):
    carpeta.mkdir(parents=True, exist_ok=True)
    with psycopg.connect(dbname=dbname) as con:
        # Un solo resultado pequeno viaja al cliente; no descargamos toda Silver.
        with con.cursor() as cur:
            cur.execute((RAIZ/'sql/resumen_mensual.sql').read_text(encoding='utf-8'))
            resumen = pd.DataFrame(cur.fetchall(), columns=[c.name for c in cur.description])
        procedencia = con.execute('''SELECT DISTINCT fuente_url, sha256, cargado_en::text
                                     FROM bronze.observaciones ORDER BY 1,2,3''').fetchall()
    if resumen.empty:
        raise ValueError('Gold vacio: ejecute la ingesta primero')
    assert not resumen.duplicated(['ciudad_id','mes']).any()
    assert resumen['dias'].le(resumen['dias_esperados']).all()
    np.testing.assert_allclose(resumen.cobertura_precipitacion,
                               resumen.n_precipitacion/resumen.dias_esperados)
    assert resumen.loc[resumen.n_precipitacion.lt(resumen.dias_esperados),
                       'precipitacion_total_mm'].isna().all()
    resumen['diferencia_medias_extremos_c'] = resumen.tmax_media_c-resumen.tmin_media_c
    # Diferencia de medias coincide con media de amplitudes solo con igual soporte.
    resumen.to_csv(carpeta/'resumen_mensual.csv', index=False)
    fig, ax = plt.subplots(figsize=(9,4.8))
    for ciudad, grupo in resumen.groupby('nombre'):
        ax.plot(grupo.mes.astype(str).str[:7], grupo.tmax_media_c, marker='o', label=ciudad)
    ax.set(xlabel='Mes (America/Bogota)', ylabel='Media de máximas diarias (°C)',
           title='ERA5 vía Open-Meteo: temperaturas disponibles por mes')
    ax.legend(loc='upper left', bbox_to_anchor=(1.02,1)); ax.grid(alpha=.2); fig.tight_layout()
    fig.savefig(carpeta/'temperatura_mensual.png', dpi=150); plt.close(fig)
    lineas = ['# Informe meteorológico', '',
              'Fuente: Open-Meteo, ERA5 / C3S / ECMWF, CC BY 4.0. Son estimaciones de reanálisis.',
              'Cada media describe máximas o mínimas diarias disponibles; no es temperatura media diaria ni incertidumbre.',
              'Las diferencias entre ciudades no permiten aislar causas: altitud, circulación, relieve y representación de la celda pueden influir.',
              'Solo se publica precipitación mensual acumulada con cobertura del 100%; no se imputan ausencias.', '',
              '| Ciudad | Mes | Días | Cobertura precip. | Cobertura Tmax | Tmax media (°C) | Precipitación (mm) |',
              '|---|---|---:|---:|---:|---:|---:|']
    for r in resumen.itertuples():
        lluvia = 'No disponible' if pd.isna(r.precipitacion_total_mm) else f'{r.precipitacion_total_mm:.2f}'
        temperatura = 'No disponible' if pd.isna(r.tmax_media_c) else f'{r.tmax_media_c:.2f}'
        lineas.append(f'| {r.nombre} | {r.mes} | {r.dias}/{r.dias_esperados} | {r.cobertura_precipitacion:.1%} | {r.cobertura_tmax:.1%} | {temperatura} | {lluvia} |')
    lineas += ['', '![Temperaturas mensuales](temperatura_mensual.png)', '',
               'Python recibió '+str(len(resumen))+' filas agregadas. Los registros diarios permanecen en PostgreSQL.',
               'La diferencia de medias de extremos no es una estimación independiente de incertidumbre; con coberturas distintas puede no ser la media de amplitudes.']
    (carpeta/'informe.md').write_text('\n'.join(lineas)+'\n', encoding='utf-8')
    (carpeta/'procedencia.json').write_text(json.dumps(
        {'base':dbname, 'consulta':'sql/resumen_mensual.sql', 'filas_recibidas':len(resumen),
         'fuentes_bronze':procedencia, 'versiones':{'pandas':pd.__version__,'numpy':np.__version__,
         'psycopg':psycopg.__version__}}, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(f'Gold: {len(resumen)} filas recibidas; informe y figura generados.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--carpeta', type=Path, required=True)
    parser.add_argument('--db', default=os.environ.get('PGDATABASE','curso_datos'))
    args = parser.parse_args()
    informar(args.carpeta,args.db)
