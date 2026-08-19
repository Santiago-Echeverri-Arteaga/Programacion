"""Estructura funcional inicial del laboratorio 3."""

from __future__ import annotations

import math


def validar_parametros(
    longitud_m: float,
    gravedad_m_s2: float,
    dt_s: float,
    duracion_s: float,
) -> None:
    """Rechaza parámetros físicos o temporales no válidos."""
    raise NotImplementedError


def aceleracion_angular(
    angulo_rad: float,
    longitud_m: float,
    gravedad_m_s2: float,
) -> float:
    """Calcula -(g/L) sin(ángulo)."""
    raise NotImplementedError


def paso_euler_cromer(
    angulo_rad: float,
    velocidad_angular_rad_s: float,
    longitud_m: float,
    gravedad_m_s2: float,
    dt_s: float,
) -> tuple[float, float]:
    """Devuelve el nuevo ángulo y la nueva velocidad angular."""
    raise NotImplementedError


def simular(
    angulo_inicial_rad: float,
    longitud_m: float,
    dt_s: float,
    duracion_s: float,
    gravedad_m_s2: float = 9.81,
) -> list[dict[str, float]]:
    """Devuelve tiempo, ángulo y velocidad desde el estado inicial."""
    raise NotImplementedError


def periodo_angulo_pequeno(
    longitud_m: float,
    gravedad_m_s2: float = 9.81,
) -> float:
    """Referencia analítica para validar amplitudes pequeñas."""
    return 2 * math.pi * math.sqrt(longitud_m / gravedad_m_s2)

