"""Aproxima la integral de x**2 en [a,b] con puntos medios."""


def integrar_cuadrado(a: float, b: float, n: int) -> float:
    if n <= 0 or b <= a:
        raise ValueError("se requiere n>0 y b>a")
    ancho = (b - a) / n
    acumulado = 0.0
    for i in range(n):
        x = a + (i + 0.5) * ancho
        acumulado += x**2 * ancho
    return acumulado


for particiones in (10, 100, 1000):
    print(particiones, integrar_cuadrado(0.0, 1.0, particiones))
