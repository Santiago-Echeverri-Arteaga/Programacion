"""El orden de las operaciones afecta la aritmética de punto flotante."""

from math import fsum


def suma_secuencial(valores: list[float]) -> float:
    """Acumula de izquierda a derecha para hacer visible el redondeo."""
    total = 0.0
    for valor in valores:
        total += valor
    return total


valores = [1e16, 1.0, -1e16]
print("secuencial:", suma_secuencial(valores))
print("orden alterno:", suma_secuencial([1e16, -1e16, 1.0]))
print("math.fsum:", fsum(valores))
