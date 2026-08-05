"""Propagación linealizada para z=x*y con variables independientes."""

from math import hypot


def producto_con_incertidumbre(
    x: float, ux: float, y: float, uy: float
) -> tuple[float, float]:
    z = x * y
    uz = hypot(y * ux, x * uy)
    return z, uz


valor, incertidumbre = producto_con_incertidumbre(2.00, 0.05, 3.0, 0.1)
print(f"z = {valor:.2f} ± {incertidumbre:.2f}")
