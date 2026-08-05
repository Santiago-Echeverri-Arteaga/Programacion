"""Cliente mínimo. DATABASE_URL debe venir del entorno."""

import os

import psycopg

url = os.environ.get("DATABASE_URL")
if not url:
    raise SystemExit("Defina DATABASE_URL; no escriba credenciales en el código")

experimento_id = 1
consulta = """
    SELECT m.instante, m.valor, s.unidad
    FROM mediciones AS m
    JOIN sensores AS s ON s.id = m.sensor_id
    WHERE s.experimento_id = %s AND m.calidad = %s
    ORDER BY m.instante
"""

with psycopg.connect(url) as conexion:
    with conexion.cursor() as cursor:
        cursor.execute(consulta, (experimento_id, "valida"))
        for fila in cursor:
            print(fila)
