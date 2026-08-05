"""Conversiones explícitas para discutir nombres y contratos."""

from __future__ import annotations


def celsius_a_kelvin(temperatura_c: float) -> float:
    if temperatura_c < -273.15:
        raise ValueError("Temperatura físicamente inválida")
    return temperatura_c + 273.15


def rapidez_media_m_s(distancia_m: float, tiempo_s: float) -> float:
    if distancia_m < 0 or tiempo_s <= 0:
        raise ValueError("Distancia no negativa y tiempo positivo requeridos")
    return distancia_m / tiempo_s

