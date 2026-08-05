"""Lectura defensiva de un CSV pequeño."""

from __future__ import annotations

import csv
from pathlib import Path


def leer(ruta: Path) -> list[tuple[float, float]]:
    datos: list[tuple[float, float]] = []
    with ruta.open(encoding="utf-8", newline="") as archivo:
        for numero, fila in enumerate(csv.DictReader(archivo), start=2):
            try:
                tiempo_s = float(fila["tiempo_s"])
                altura_m = float(fila["altura_m"])
            except (KeyError, TypeError, ValueError) as error:
                raise ValueError(f"Fila {numero} inválida: {fila}") from error
            if tiempo_s < 0 or altura_m < 0:
                raise ValueError(f"Fila {numero} contiene una magnitud negativa")
            datos.append((tiempo_s, altura_m))
    return datos


if __name__ == "__main__":
    ruta = Path(__file__).with_name("mediciones_pequenas.csv")
    print(leer(ruta))

