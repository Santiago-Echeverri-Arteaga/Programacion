"""Composición de datos e instrumento en un experimento pequeño."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Medicion:
    tiempo_s: float
    posicion_m: float


@dataclass
class SensorPosicion:
    resolucion_m: float

    def cuantizar(self, valor_m: float) -> float:
        return round(valor_m / self.resolucion_m) * self.resolucion_m


class Experimento:
    def __init__(self, sensor: SensorPosicion) -> None:
        self.sensor = sensor
        self.mediciones: list[Medicion] = []

    def registrar(self, tiempo_s: float, posicion_m: float) -> None:
        self.mediciones.append(Medicion(tiempo_s, self.sensor.cuantizar(posicion_m)))
