"""Ajuste lineal ponderado y residuales."""

from __future__ import annotations

import numpy as np
from scipy.optimize import curve_fit


def modelo(x: np.ndarray, pendiente: float, intercepto: float) -> np.ndarray:
    return pendiente * x + intercepto


if __name__ == "__main__":
    x = np.array([0.0, 1.0, 2.0, 3.0])
    y = np.array([0.1, 2.0, 4.2, 5.9])
    sigma = np.full_like(x, 0.2)
    parametros, covarianza = curve_fit(
        modelo, x, y, sigma=sigma, absolute_sigma=True
    )
    print("parámetros:", parametros)
    print("incertidumbres:", np.sqrt(np.diag(covarianza)))
    print("residuales:", y - modelo(x, *parametros))

