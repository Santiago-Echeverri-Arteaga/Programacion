"""Clasifica una lectura sin mezclar validación con presentación."""

from __future__ import annotations


def clasificar_temperatura(temperatura_c: float) -> str:
    if temperatura_c < -273.15:
        raise ValueError("Temperatura inferior al cero absoluto")
    if temperatura_c < 15.0:
        return "baja"
    if temperatura_c <= 30.0:
        return "ambiente"
    return "alta"


if __name__ == "__main__":
    for valor in (10.0, 22.0, 35.0):
        print(valor, clasificar_temperatura(valor))

