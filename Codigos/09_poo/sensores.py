"""Polimorfismo estructural con Protocol."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


class Medible(Protocol):
    def medir(self) -> float: ...


@dataclass
class SensorConstante:
    valor: float

    def medir(self) -> float:
        return self.valor


def tomar_muestras(sensor: Medible, cantidad: int) -> list[float]:
    return [sensor.medir() for _ in range(cantidad)]


if __name__ == "__main__":
    print(tomar_muestras(SensorConstante(3.2), 4))

