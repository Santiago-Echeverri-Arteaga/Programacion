"""Ejemplos acotados de temas opcionales."""

from collections.abc import Iterator
from functools import wraps


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n debe ser no negativo")
    return 1 if n == 0 else n * factorial(n - 1)


def tiempos_uniformes(paso_s: float, cantidad: int) -> Iterator[float]:
    for indice in range(cantidad):
        yield indice * paso_s


def contar_llamadas(funcion):
    llamadas = 0

    @wraps(funcion)
    def envoltura(*args, **kwargs):
        nonlocal llamadas
        llamadas += 1
        print(f"llamada {llamadas}")
        return funcion(*args, **kwargs)

    return envoltura
