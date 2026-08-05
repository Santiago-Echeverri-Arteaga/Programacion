"""Muestra cuándo aparecen *args y **kwargs en APIs."""

from __future__ import annotations


def promedio(*valores: float) -> float:
    if not valores:
        raise ValueError("Se requiere al menos un valor")
    return sum(valores) / len(valores)


def describir(nombre: str, **metadatos: object) -> str:
    partes = [nombre]
    partes.extend(f"{clave}={valor}" for clave, valor in sorted(metadatos.items()))
    return ", ".join(partes)


if __name__ == "__main__":
    print(promedio(1.0, 2.0, 3.0))
    print(describir("sensor_A", unidad="degC", resolucion=0.1))

