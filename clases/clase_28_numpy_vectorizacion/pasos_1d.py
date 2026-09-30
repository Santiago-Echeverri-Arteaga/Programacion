"""Práctica del 15 oct.: generador, ejes y acumulación de pasos en 1D.

La demo no resuelve el laboratorio de difusión bidimensional.
"""

import numpy as np

rng = np.random.default_rng(2026)
# Filas: caminantes; columnas: pasos.
pasos = 2 * rng.integers(0, 2, size=(4, 6)) - 1
posiciones = np.zeros((4, 7), dtype=int)
posiciones[:, 1:] = np.cumsum(pasos, axis=1)

print("Pasos:", pasos.shape, pasos.dtype)
print(pasos)
print("Posiciones con origen:", posiciones.shape)
print(posiciones)
print("Media por instante:", posiciones.mean(axis=0))
print("Media de cuadrados:", (posiciones**2).mean(axis=0))
assert np.all(np.abs(np.diff(posiciones, axis=1)) == 1)
