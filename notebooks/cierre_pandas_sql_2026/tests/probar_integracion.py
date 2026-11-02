"""Pruebas en una base NUEVA precreada: nunca borra ni reinicia bases existentes."""
from pathlib import Path
import os
import subprocess
import sys
import numpy as np
import pandas as pd
import psycopg

RAIZ=Path(__file__).resolve().parents[1]


def marco(con,sql):
    with con.cursor() as cur:
        cur.execute(sql)
        return pd.DataFrame(cur.fetchall(),columns=[c.name for c in cur.description])


def main():
    base=os.environ.get('PGDATABASE', '')
    if not base.startswith('test_meteo_'):
        raise ValueError('Usa una base independiente con prefijo test_meteo_')
    env={**os.environ,'PGDATABASE':base}
    with psycopg.connect(dbname=base) as con:
        if con.execute("SELECT 1 FROM pg_namespace WHERE nspname IN ('bronze','silver','gold')").fetchone():
            raise ValueError('La base ya tiene esquemas; crea otra. No se borra nada.')
    def pipeline(fase):
        # CWD distinto: comprobar rutas relativas al script, no a quien lo invoca.
        subprocess.run(['bash',str(RAIZ/'ampliacion/pipeline.sh'),'offline',fase],
                       cwd=RAIZ.parent,env=env,check=True)
    pipeline('inicial')
    with psycopg.connect(dbname=base) as con:
        assert con.execute('SELECT COUNT(*) FROM silver.observaciones').fetchone()[0]==93
        assert con.execute('SELECT COUNT(*) FROM gold.mensual').fetchone()[0]==3
        inicial=con.execute('SELECT * FROM silver.observaciones ORDER BY 1,2').fetchall()
        bronze_inicial=con.execute('SELECT * FROM bronze.observaciones ORDER BY 1,2').fetchall()
    pipeline('actualizacion');pipeline('actualizacion')
    with psycopg.connect(dbname=base) as con:
        assert con.execute('SELECT COUNT(*) FROM silver.observaciones').fetchone()[0]==180
        assert con.execute('SELECT COUNT(*) FROM bronze.observaciones').fetchone()[0]==180
        assert con.execute("SELECT * FROM silver.observaciones WHERE fecha<'2024-02-01' ORDER BY 1,2").fetchall()==inicial
        assert con.execute("SELECT * FROM bronze.observaciones WHERE fecha<'2024-02-01' ORDER BY 1,2").fetchall()==bronze_inicial
        assert not con.execute('SELECT ciudad_id,fecha FROM silver.observaciones GROUP BY 1,2 HAVING COUNT(*)>1').fetchall()
        datos=marco(con,'SELECT * FROM silver.observaciones ORDER BY 1,2')
        datos['fecha']=pd.to_datetime(datos.fecha)
        copia=pd.read_csv(RAIZ/'datos/meteorologia.csv',parse_dates=['fecha'])
        pd.testing.assert_frame_equal(datos,copia,check_dtype=False)
        gold=marco(con,'SELECT * FROM gold.mensual ORDER BY ciudad_id,mes')
        assert len(gold)==6
        datos['mes']=datos.fecha.dt.to_period('M').dt.to_timestamp().dt.date
        esperado=datos.groupby(['ciudad_id','mes']).agg(dias=('fecha','size'),n_tmax=('tmax_c','count'),
           n_tmin=('tmin_c','count'),n_precipitacion=('precipitacion_mm','count'),
           tmax_media_c=('tmax_c','mean'),tmin_media_c=('tmin_c','mean'),
           precipitacion_total_mm=('precipitacion_mm','sum')).reset_index()
        for columna in esperado.columns[2:]:
            np.testing.assert_allclose(gold[columna],esperado[columna],rtol=1e-10,atol=1e-10)
        np.testing.assert_allclose(gold.cobertura_precipitacion,1)
        assert gold.dias_esperados.tolist()==[31,29,31,29,31,29]
    # Pruebas deliberadas solo en transacciones revertidas de la base independiente.
    for sentencia,error in [
        ("UPDATE silver.observaciones SET precipitacion_mm=-1 WHERE ciudad_id='armenia'",psycopg.errors.CheckViolation),
        ("UPDATE silver.observaciones SET tmin_c=tmax_c+1 WHERE ciudad_id='armenia'",psycopg.errors.CheckViolation),
        ("UPDATE silver.observaciones SET tmax_c='NaN'::float8 WHERE ciudad_id='armenia'",psycopg.errors.CheckViolation),
        ("UPDATE silver.observaciones SET fecha=NULL WHERE ciudad_id='armenia'",psycopg.errors.NotNullViolation),
        ("UPDATE silver.observaciones SET ciudad_id='inexistente' WHERE ciudad_id='armenia'",psycopg.errors.ForeignKeyViolation),
        ("INSERT INTO silver.observaciones SELECT * FROM silver.observaciones LIMIT 1",psycopg.errors.UniqueViolation),
        ("INSERT INTO silver.ciudades VALUES ('otra','Bogotá',0,0)",psycopg.errors.UniqueViolation),
    ]:
        with psycopg.connect(dbname=base) as con:
            try:con.execute(sentencia)
            except error:con.rollback()
            else:
                con.rollback();raise AssertionError('No rechazo la restriccion: '+sentencia)
    with psycopg.connect(dbname=base) as con:
        con.execute("UPDATE silver.observaciones SET precipitacion_mm=NULL,tmax_c=NULL WHERE ciudad_id='armenia' AND fecha='2024-01-01'")
        row=con.execute("SELECT n_precipitacion,cobertura_precipitacion,precipitacion_total_mm,n_tmax FROM gold.mensual WHERE ciudad_id='armenia' AND mes='2024-01-01'").fetchone()
        assert row[0]==30 and np.isclose(row[1],30/31) and row[2] is None and row[3]==30
        con.rollback()
        con.execute("DELETE FROM silver.observaciones WHERE ciudad_id='armenia' AND fecha='2024-01-01'")
        row=con.execute("SELECT dias,dias_esperados,precipitacion_total_mm FROM gold.mensual WHERE ciudad_id='armenia' AND mes='2024-01-01'").fetchone()
        assert row==(30,31,None)
        con.rollback()
        # Fila artificial exclusivamente para verificar atomicidad; nunca confirmada.
        try:
            con.execute("INSERT INTO bronze.observaciones VALUES ('armenia','2024-03-01',10,20,0,'prueba artificial',%s,DEFAULT)",('0'*64,))
            con.execute((RAIZ/'ampliacion/02_resumir.sql').read_text())
        except psycopg.errors.CheckViolation:con.rollback()
        else:con.rollback();raise AssertionError('Debia fallar min>max')
        assert con.execute("SELECT COUNT(*) FROM bronze.observaciones WHERE fecha='2024-03-01'").fetchone()[0]==0
    subprocess.run(['psql','-X','-v','ON_ERROR_STOP=1','-f',str(RAIZ/'sql/01_consultas_clase.sql')],env=env,check=True,stdout=subprocess.DEVNULL)
    subprocess.run([sys.executable,str(RAIZ/'ampliacion/consulta_local.py')],env=env,check=True,stdout=subprocess.DEVNULL)
    subprocess.run(['bash',str(RAIZ/'ampliacion/ejecutar_resumen.sh')],env=env,check=True)
    carpetas=set((RAIZ/'salidas_pipeline').glob('ejecucion.*'))
    # Base inexistente: el pipeline debe fallar y no marcar su carpeta como completa.
    fallo=subprocess.run(['bash',str(RAIZ/'ampliacion/pipeline.sh')],env={**env,'PGDATABASE':base+'_no_existe'},capture_output=True)
    assert fallo.returncode!=0
    nuevas=set((RAIZ/'salidas_pipeline').glob('ejecucion.*'))-carpetas
    assert len(nuevas)==1 and not any((c/'COMPLETADO.txt').exists() for c in nuevas)
    completadas=[c for c in carpetas if (c/'COMPLETADO.txt').exists()]
    assert len(completadas)>=3
    for c in completadas:
        assert (c/'temperatura_mensual.png').stat().st_size>1000
        assert (c/'informe.md').stat().st_size>100
    print('OK: 93 -> 180 -> 180; Bronze/Silver preservados; Gold vs Pandas; NULL/dia ausente;')
    print('restricciones; rollback atomico; psql; Psycopg; Bash; rutas; informes; fallo sin COMPLETADO.')


if __name__=='__main__':main()
