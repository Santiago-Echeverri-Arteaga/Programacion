"""Integra aproximadamente el trabajo a partir de fuerza y desplazamiento."""

from __future__ import annotations


def trabajo_j(fuerzas_n: list[float], desplazamientos_m: list[float]) -> float:
    if len(fuerzas_n) != len(desplazamientos_m):
        raise ValueError("Las series deben tener igual longitud")
    acumulado = 0.0
    for fuerza_n, desplazamiento_m in zip(fuerzas_n, desplazamientos_m):
        acumulado += fuerza_n * desplazamiento_m
    return acumulado


if __name__ == "__main__":
    print(trabajo_j([2.0, 2.5, 3.0], [0.1, 0.1, 0.1]), "J")

