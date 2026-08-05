"""Patrón genérico de verificación para adaptar, no solución del laboratorio."""


def comprobar_monotonia(entradas: list[float], salidas: list[float]) -> bool:
    if len(entradas) != len(salidas):
        raise ValueError("las series deben tener igual longitud")
    return all(a <= b for a, b in zip(salidas, salidas[1:]))
