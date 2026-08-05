"""Polimorfismo estructural sin jerarquías innecesarias."""

from typing import Protocol


class Sensor(Protocol):
    def convertir(self, voltaje_v: float) -> float: ...


class SensorLineal:
    def __init__(self, pendiente: float, intercepto: float = 0.0) -> None:
        self.pendiente = pendiente
        self.intercepto = intercepto

    def convertir(self, voltaje_v: float) -> float:
        return self.pendiente * voltaje_v + self.intercepto


def adquirir(sensor: Sensor, voltajes: list[float]) -> list[float]:
    return [sensor.convertir(voltaje) for voltaje in voltajes]
