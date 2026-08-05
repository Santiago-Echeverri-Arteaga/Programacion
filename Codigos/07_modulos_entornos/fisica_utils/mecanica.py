"""Funciones mecánicas del paquete de demostración."""

from __future__ import annotations

import math


def periodo_pendulo_s(longitud_m: float, gravedad_m_s2: float = 9.81) -> float:
    if longitud_m <= 0 or gravedad_m_s2 <= 0:
        raise ValueError("Longitud y gravedad deben ser positivas")
    return 2 * math.pi * math.sqrt(longitud_m / gravedad_m_s2)

