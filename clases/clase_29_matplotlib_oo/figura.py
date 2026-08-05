"""Figura científica mínima con API orientada a objetos."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

tiempo_s = np.linspace(0.0, 2.0, 9)
posicion_m = 0.5 * 9.81 * tiempo_s**2
incertidumbre_m = np.full_like(posicion_m, 0.15)

fig, ax = plt.subplots(figsize=(6, 4), layout="constrained")
ax.errorbar(tiempo_s, posicion_m, yerr=incertidumbre_m, fmt="o", label="medición")
ax.set(xlabel="Tiempo [s]", ylabel="Posición [m]", title="Caída ideal simulada")
ax.grid(alpha=0.3)
ax.legend()
fig.savefig(Path(__file__).with_name("caida.png"), dpi=180)
