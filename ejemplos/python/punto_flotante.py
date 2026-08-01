"""Demostraciones breves de límites de la aritmética de punto flotante."""

from __future__ import annotations

import math


def main() -> None:
    suma = 0.1 + 0.2
    print(f"0.1 + 0.2 = {suma:.17f}")
    print(f"Comparación exacta: {suma == 0.3}")
    print(f"Comparación tolerante: {math.isclose(suma, 0.3)}")

    grande = 1.0e16
    print(f"(grande + 1) - grande = {(grande + 1.0) - grande}")
    print("El orden de operaciones puede perder información significativa.")


if __name__ == "__main__":
    main()

