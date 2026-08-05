"""Funciones pequeñas para diseñar pruebas."""

from __future__ import annotations


def promedio(valores: list[float]) -> float:
    if not valores:
        raise ValueError("No se puede promediar una lista vacía")
    return sum(valores) / len(valores)

