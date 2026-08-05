"""Código mínimo que será sometido a pruebas."""


def periodo_pendulo(longitud_m: float, gravedad_m_s2: float = 9.81) -> float:
    if longitud_m <= 0 or gravedad_m_s2 <= 0:
        raise ValueError("longitud y gravedad deben ser positivas")
    return 2 * 3.141592653589793 * (longitud_m / gravedad_m_s2) ** 0.5
