"""Composición de calibración y sensor."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CalibracionLineal:
    pendiente: float
    intercepto: float

    def aplicar(self, lectura_cruda: float) -> float:
        return self.pendiente * lectura_cruda + self.intercepto


@dataclass
class Sensor:
    nombre: str
    unidad: str
    calibracion: CalibracionLineal

    def medir(self, lectura_cruda: float) -> float:
        return self.calibracion.aplicar(lectura_cruda)


if __name__ == "__main__":
    termopar = Sensor("T1", "degC", CalibracionLineal(0.1, -2.0))
    print(termopar.medir(250.0), termopar.unidad)

