"""Funciones pequeñas adaptadas del ejemplo desarrollado en el curso."""

from math import isfinite


def velocidad(desplazamiento_m: float, tiempo_t: float) -> float:
    """Devuelve velocidad media en m/s; exige un intervalo finito positivo."""
    if not isfinite(desplazamiento_m) or not isfinite(tiempo_t):
        raise ValueError("se requieren valores finitos")
    if tiempo_t <= 0:
        raise ValueError("el intervalo debe ser positivo")
    return desplazamiento_m / tiempo_t


def primos(num: int) -> bool:
    """Indica si un entero es primo; las anotaciones no convierten entradas."""
    if num < 2:
        return False
    for divisor in range(2, num):
        if num % divisor == 0:
            return False
    return True


def integrar_cuadrado(a: float, b: float, n: int) -> float:
    """Aproxima la integral de x² en [a,b] usando n puntos medios."""
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
        raise ValueError("n debe ser un entero positivo")
    if not isfinite(a) or not isfinite(b) or b <= a:
        raise ValueError("se requieren límites finitos con b>a")
    ancho = (b - a) / n
    acumulado = 0.0
    for i in range(n):
        x = a + (i + 0.5) * ancho
        acumulado += x**2 * ancho
    return acumulado
