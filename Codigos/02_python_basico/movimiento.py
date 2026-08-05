"""Funciones pequeñas para demostrar contratos, unidades y pruebas."""

from __future__ import annotations


def posicion_mru(x0_m: float, velocidad_m_s: float, tiempo_s: float) -> float:
    """Devuelve la posición en metros para movimiento rectilíneo uniforme."""
    if tiempo_s < 0:
        raise ValueError("El tiempo no puede ser negativo")
    return x0_m + velocidad_m_s * tiempo_s


def energia_cinetica_j(masa_kg: float, rapidez_m_s: float) -> float:
    """Devuelve 1/2*m*v² en joules."""
    if masa_kg < 0:
        raise ValueError("La masa no puede ser negativa")
    return 0.5 * masa_kg * rapidez_m_s**2

