"""Funciones con contratos simples para cinemática unidimensional."""


def posicion_mru(x0_m: float, velocidad_m_s: float, tiempo_s: float) -> float:
    """Calcula x=x0+v*t; requiere tiempo_s >= 0 y devuelve metros."""
    if tiempo_s < 0:
        raise ValueError("el tiempo no puede ser negativo")
    return x0_m + velocidad_m_s * tiempo_s


def velocidad_media(desplazamiento_m: float, intervalo_s: float) -> float:
    """Devuelve la velocidad media en m/s; el intervalo debe ser positivo."""
    if intervalo_s <= 0:
        raise ValueError("el intervalo debe ser positivo")
    return desplazamiento_m / intervalo_s
