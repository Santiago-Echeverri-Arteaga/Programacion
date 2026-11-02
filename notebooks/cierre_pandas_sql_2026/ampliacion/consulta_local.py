"""Consulta parametrizada local; ejecutar tras la carga inicial."""
import os
import psycopg
import pandas as pd

with psycopg.connect(dbname=os.environ.get('PGDATABASE','curso_datos')) as con:
    with con.cursor() as cur:
        cur.execute('''SELECT ciudad_id, fecha, tmax_c FROM silver.observaciones
                       WHERE ciudad_id=%s AND tmax_c>=%s ORDER BY fecha''', ('armenia', 24))
        datos = pd.DataFrame(cur.fetchall(), columns=[c.name for c in cur.description])
print(datos)
# Los valores viajan separados del SQL: no usar f-strings para construir condiciones.
# fetchall es adecuado para este resultado pequeno; para grandes resultados ver escenario D.
