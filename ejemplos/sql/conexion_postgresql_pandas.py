"""Carga una consulta PostgreSQL en Pandas sin interpolar datos del usuario."""

from __future__ import annotations

import os

import pandas as pd
from sqlalchemy import create_engine, text


def resumen(dsn: str) -> pd.DataFrame:
    sql = text("""
        SELECT s.nombre AS sensor, s.unidad, m.valor, m.incertidumbre
        FROM mediciones AS m
        JOIN sensores AS s ON s.id = m.sensor_id
        WHERE m.calidad = :calidad
    """)
    sqlalchemy_dsn = dsn.replace("postgresql://", "postgresql+psycopg://", 1)
    motor = create_engine(sqlalchemy_dsn)
    with motor.connect() as conexion:
        return pd.read_sql_query(sql, conexion, params={"calidad": "valida"})


if __name__ == "__main__":
    datos = resumen(os.environ["DATABASE_URL"])
    print(datos.groupby(["sensor", "unidad"])["valor"].agg(["count", "mean"]))
