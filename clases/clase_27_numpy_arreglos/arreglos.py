"""Primeros arreglos NumPy en un contexto de trayectoria."""

import numpy as np

tiempo_s = np.linspace(0.0, 2.0, 9)
posicion_m = 0.5 * 9.81 * tiempo_s**2

print("forma:", posicion_m.shape)
print("tipo:", posicion_m.dtype)
print("después de 1 s:", posicion_m[tiempo_s > 1.0])
print("matriz tiempo-posición:\n", np.column_stack((tiempo_s, posicion_m)))
