"""Decorador didáctico para leer funciones de orden superior."""

from __future__ import annotations

from collections.abc import Callable
from functools import wraps
from time import perf_counter
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def medir_tiempo(funcion: Callable[P, R]) -> Callable[P, R]:
    @wraps(funcion)
    def envoltura(*args: P.args, **kwargs: P.kwargs) -> R:
        inicio = perf_counter()
        resultado = funcion(*args, **kwargs)
        print(f"{funcion.__name__}: {perf_counter() - inicio:.6f} s")
        return resultado

    return envoltura

