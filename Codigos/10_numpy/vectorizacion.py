"""Contrasta un cálculo escalar con un cálculo vectorizado equivalente."""

from __future__ import annotations

import math

import numpy as np
from numpy.typing import NDArray


def oscilador_escalar(
    tiempos_s: list[float], amplitud_m: float, omega_rad_s: float
) -> list[float]:
    return [amplitud_m * math.cos(omega_rad_s * t) for t in tiempos_s]


def oscilador_vectorizado(
    tiempos_s: NDArray[np.float64], amplitud_m: float, omega_rad_s: float
) -> NDArray[np.float64]:
    return amplitud_m * np.cos(omega_rad_s * tiempos_s)


def main() -> None:
    tiempos = np.linspace(0.0, 2.0, 9)
    posiciones = oscilador_vectorizado(tiempos, amplitud_m=0.1, omega_rad_s=2.0)
    print("forma:", posiciones.shape)
    print("tipo:", posiciones.dtype)
    print("posiciones positivas:", posiciones[posiciones > 0])


if __name__ == "__main__":
    main()

