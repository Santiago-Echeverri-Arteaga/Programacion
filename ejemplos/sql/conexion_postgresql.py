"""Consulta PostgreSQL local o remoto usando una URL en el entorno.

Antes de ejecutar:
    export DATABASE_URL='postgresql://usuario:clave@servidor:5432/base'

Para un servicio remoto suele requerirse `?sslmode=require` al final de la URL.
Nunca escriba credenciales reales directamente en este archivo.
"""

from __future__ import annotations

import os

import psycopg
from psycopg.rows import dict_row


def cargar_mediciones(dsn: str, sensor: str) -> list[dict[str, object]]:
    """Devuelve mediciones válidas de un sensor en orden temporal."""
    sql = """
        SELECT m.instante, m.valor, m.incertidumbre, s.unidad
        FROM mediciones AS m
        JOIN sensores AS s ON s.id = m.sensor_id
        WHERE s.nombre = %s AND m.calidad = %s
        ORDER BY m.instante
    """
    with psycopg.connect(dsn, row_factory=dict_row) as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(sql, (sensor, "valida"))
            return list(cursor.fetchall())


def main() -> None:
    try:
        dsn = os.environ["DATABASE_URL"]
    except KeyError as error:
        raise SystemExit("Falta la variable de entorno DATABASE_URL") from error

    for medicion in cargar_mediciones(dsn, "termopar_A"):
        print(medicion)


if __name__ == "__main__":
    main()

