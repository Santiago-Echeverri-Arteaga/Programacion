"""Lectura explícita de un CSV numérico pequeño, sin campos entrecomillados."""

from math import isfinite
from pathlib import Path


def leer_posiciones(ruta: Path) -> list[tuple[float, float]]:
    """Lee dos columnas finitas; informa fila y causa de datos inválidos."""
    filas = []
    with ruta.open(encoding="utf-8") as archivo:
        encabezado = archivo.readline().strip()
        if encabezado != "tiempo_s,posicion_m":
            raise ValueError("línea 1: encabezado inesperado")
        for numero, linea in enumerate(archivo, start=2):
            campos = linea.strip().split(",")
            if len(campos) != 2:
                raise ValueError(f"línea {numero}: se esperaban dos columnas")
            try:
                tiempo = float(campos[0])
                posicion = float(campos[1])
            except ValueError as error:
                raise ValueError(f"línea {numero}: valor no numérico") from error
            if not isfinite(tiempo) or not isfinite(posicion):
                raise ValueError(f"línea {numero}: se requieren valores finitos")
            filas.append((tiempo, posicion))
    if not filas:
        raise ValueError("el archivo no contiene mediciones")
    return filas
