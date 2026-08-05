"""Compara suma ingenua y math.fsum."""

from __future__ import annotations

import math


if __name__ == "__main__":
    valores = [1.0e16, 1.0, -1.0e16]
    print("sum:", sum(valores))
    print("fsum:", math.fsum(valores))

