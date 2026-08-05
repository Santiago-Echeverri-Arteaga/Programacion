"""Muchas condiciones iniciales y una malla temporal mediante broadcasting."""

import numpy as np

rng = np.random.default_rng(2026)
velocidades_m_s = rng.uniform(1.0, 5.0, size=(4, 1))
tiempos_s = np.linspace(0.0, 2.0, 6)[None, :]
posiciones_m = velocidades_m_s * tiempos_s

print("v:", velocidades_m_s.shape)
print("t:", tiempos_s.shape)
print("x:", posiciones_m.shape)
print(posiciones_m)
