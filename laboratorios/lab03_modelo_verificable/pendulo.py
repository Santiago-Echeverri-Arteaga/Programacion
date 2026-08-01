"""Estructura inicial del laboratorio 3."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ParametrosPendulo:
    longitud_m: float
    gravedad_m_s2: float = 9.81

    def __post_init__(self) -> None:
        if self.longitud_m <= 0:
            raise ValueError("La longitud debe ser positiva")
        if self.gravedad_m_s2 <= 0:
            raise ValueError("La gravedad debe ser positiva")


@dataclass
class EstadoPendulo:
    tiempo_s: float
    angulo_rad: float
    velocidad_angular_rad_s: float


def paso_euler_cromer(
    estado: EstadoPendulo,
    parametros: ParametrosPendulo,
    dt_s: float,
) -> EstadoPendulo:
    """Avanza un paso temporal. Complete y valide la implementación."""
    raise NotImplementedError


def simular(
    inicial: EstadoPendulo,
    parametros: ParametrosPendulo,
    dt_s: float,
    duracion_s: float,
) -> list[EstadoPendulo]:
    """Devuelve la historia temporal incluido el estado inicial."""
    raise NotImplementedError

