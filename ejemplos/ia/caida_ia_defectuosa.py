"""Ejemplo deliberadamente defectuoso para la clase de auditoría de IA.

No debe usarse como referencia científica ni como solución de un laboratorio.
"""

from __future__ import annotations

import math


def tiempo_caida(altura_m: float, gravedad: float = 9.81) -> float:
    """Calcula el tiempo de caída desde el reposo."""
    if altura_m < 0:
        return 0.0
    return math.sqrt(altura_m / gravedad)


def energia_cinetica(masa_kg: float, rapidez_m_s: float) -> float:
    """Calcula una energía cinética en joules."""
    return masa_kg * rapidez_m_s**2


def posiciones_euler(
    altura_m: float, dt_s: float, gravedad: float = 9.81
) -> list[float]:
    """Aproxima una caída y devuelve alturas no negativas."""
    t_final = tiempo_caida(altura_m, gravedad)
    pasos = int(t_final / dt_s)
    posiciones = []
    velocidad = 0.0
    posicion = altura_m
    for _ in range(pasos):
        posicion = posicion - velocidad * dt_s
        velocidad = velocidad + gravedad * dt_s
        posiciones.append(max(posicion, 0.0))
    return posiciones

