"""Ejemplos de firmas expresivas y argumentos nombrados."""

from collections.abc import Callable


def transformar(
    valores: list[float],
    modelo: Callable[[float], float],
    *,
    redondeo: int | None = None,
) -> list[float]:
    """Aplica un modelo y opcionalmente redondea cada resultado."""
    resultados = [modelo(valor) for valor in valores]
    if redondeo is not None:
        resultados = [round(valor, redondeo) for valor in resultados]
    return resultados


def recta(x: float, pendiente: float = 1.0, intercepto: float = 0.0) -> float:
    return pendiente * x + intercepto


print(transformar([0.0, 0.5, 1.0], lambda x: recta(x, pendiente=2.0), redondeo=2))
