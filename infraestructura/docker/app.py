"""Cliente mínimo para demostrar comunicación entre contenedores."""

from __future__ import annotations

import os

import psycopg
from psycopg.rows import dict_row


def resumen_por_sensor(dsn: str) -> list[dict[str, object]]:
    consulta = """
        SELECT
            s.nombre AS sensor,
            s.unidad,
            count(*) AS n,
            round(avg(m.valor)::numeric, 2) AS promedio
        FROM mediciones AS m
        JOIN sensores AS s ON s.id = m.sensor_id
        WHERE m.calidad <> %s
        GROUP BY s.id, s.nombre, s.unidad
        ORDER BY s.nombre
    """
    with psycopg.connect(dsn, row_factory=dict_row) as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(consulta, ("descartada",))
            return list(cursor.fetchall())


def main() -> None:
    dsn = os.environ["DATABASE_URL"]
    print("Resumen leído desde PostgreSQL:")
    for fila in resumen_por_sensor(dsn):
        print(
            f"- {fila['sensor']}: n={fila['n']}, "
            f"promedio={fila['promedio']} {fila['unidad']}"
        )


if __name__ == "__main__":
    main()

