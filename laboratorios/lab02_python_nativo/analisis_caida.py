"""Archivo inicial del laboratorio 2."""

from __future__ import annotations

import csv
from pathlib import Path


def leer_datos(ruta: Path) -> list[dict[str, float]]:
    """Lee y valida las columnas numéricas del archivo."""
    datos: list[dict[str, float]] = []
    with ruta.open(encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        for numero_fila, fila in enumerate(lector, start=2):
            # TODO: convertir, validar y agregar una fila.
            raise NotImplementedError(f"Complete la fila {numero_fila}: {fila}")
    return datos


def estimaciones_gravedad(datos: list[dict[str, float]]) -> list[float]:
    """Calcula una estimación de g para cada tiempo positivo."""
    raise NotImplementedError


def main() -> None:
    ruta = Path(__file__).parents[2] / "datos" / "caida_libre_sintetica.csv"
    datos = leer_datos(ruta)
    print(estimaciones_gravedad(datos))


if __name__ == "__main__":
    main()

