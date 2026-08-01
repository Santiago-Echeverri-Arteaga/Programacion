"""Estructura inicial del laboratorio 4."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray


def simular_caminatas(
    n_caminantes: int,
    n_pasos: int,
    semilla: int,
) -> NDArray[np.int64]:
    """Devuelve posiciones con forma (n_caminantes, n_pasos + 1, 2)."""
    raise NotImplementedError


def desplazamiento_cuadratico_medio(
    posiciones: NDArray[np.int64],
) -> NDArray[np.float64]:
    """Promedia x**2 + y**2 para cada instante."""
    raise NotImplementedError

