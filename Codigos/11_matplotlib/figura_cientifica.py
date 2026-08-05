"""Figura mínima con la interfaz orientada a objetos de Matplotlib."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def crear_figura(ruta_salida: Path) -> None:
    tiempo_s = np.linspace(0.0, 4.0, 100)
    posicion_m = 0.08 * np.cos(2 * np.pi * tiempo_s)

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(tiempo_s, posicion_m, label="modelo armónico")
    ax.axhline(0.0, color="0.5", linewidth=0.8)
    ax.set(
        xlabel="Tiempo (s)",
        ylabel="Posición (m)",
        title="Oscilador armónico",
    )
    ax.legend()
    fig.tight_layout()
    fig.savefig(ruta_salida, dpi=160)
    plt.close(fig)


if __name__ == "__main__":
    destino = Path("resultados") / "oscilador.png"
    destino.parent.mkdir(exist_ok=True)
    crear_figura(destino)
    print(f"Figura guardada en {destino}")

