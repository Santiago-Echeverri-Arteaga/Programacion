"""Euler explícito con exactamente n-1 actualizaciones para n puntos.

Referencia: ivp_one.py, Alex Gezerlis (2023). Véase 06_euler.md.
La demostración contrasta la regla con una solución conocida de y'=-y.
"""
from collections.abc import Callable
from math import exp
from _apoyo import (real_finito, entero_positivo, tabla, opciones,
                    preparar_grafica, guardar_figura)


def euler(f: Callable[[float, float], float], a: float, b: float, n: int,
          y_inicial: float) -> list[tuple[float, float]]:
    """Devuelve n pares (t,y), incluyendo condición inicial y tiempo final.

    Entradas: f(t,y) da dy/dt, a<b finitos, n entero >=2 PUNTOS, y_inicial
    finito. El paso es (b-a)/(n-1). f debe estar definida en estados visitados.
    Salida: lista nueva; no imprime ni modifica datos externos. Solo evalúa
    la pendiente n-1 veces, usando el estado anterior de cada paso.
    ValueError: entradas, malla o resultados inválidos, o fallo de dominio.
    No garantiza estabilidad para cualquier modelo o tamaño de paso.
    """
    a, b = real_finito(a, "a"), real_finito(b, "b")
    y = real_finito(y_inicial, "y_inicial")
    n = entero_positivo(n, "n", 2)
    if a >= b:
        raise ValueError("Se requiere a < b")
    h = real_finito((b - a) / (n - 1), "paso")
    if h <= 0 or a + h == a or b - h == b:
        raise ValueError("La malla no distingue tiempos en precisión float")
    trayectoria = [(a, y)]
    for i in range(n - 1):
        t = a + i * h
        try:
            pendiente = real_finito(f(t, y), "pendiente")
        except (ValueError, OverflowError, ZeroDivisionError) as error:
            raise ValueError(f"Pendiente inválida en t={t}, y={y}: {error}") from error
        nuevo_y = real_finito(y + h * pendiente, "nuevo_y")
        nuevo_t = b if i == n - 2 else a + (i + 1) * h
        trayectoria.append((nuevo_t, nuevo_y))
        y = nuevo_y
    return trayectoria


def ritmo(t: float, y: float) -> float:
    """Devuelve -y en unidades normalizadas; t no altera este modelo autónomo."""
    return -y


def main() -> None:
    """Muestra Euler y referencia analítica para y(0)=2, y dibuja dos mallas."""
    args = opciones()
    trayectoria = euler(ritmo, 0, 1, 5, 2)
    filas = [(t, y, 2 * exp(-t), abs(y - 2 * exp(-t))) for t, y in trayectoria]
    tabla("EULER | y' = -y, y(0) = 2", ["Tiempo", "Euler", "Referencia", "Error absoluto"], filas)
    if args.sin_grafica:
        return
    plt = preparar_grafica(args.mostrar)
    fig, ax = plt.subplots(figsize=(8, 4.8), layout="constrained")
    tiempos = [i / 100 for i in range(101)]
    ax.plot(tiempos, [2 * exp(-t) for t in tiempos], color="#245fa7", label="Referencia: 2 exp(−t)", linewidth=2)
    for n, color in ((5, "#d76325"), (21, "#14806c")):
        pares = euler(ritmo, 0, 1, n, 2)
        ax.plot([p[0] for p in pares], [p[1] for p in pares], "o--", markersize=4, color=color, label=f"Euler: {n} puntos")
    ax.set(title="Una evolución construida paso a paso", xlabel="Tiempo (normalizado)", ylabel="y (normalizada)")
    ax.legend()
    guardar_figura(fig, args.salida, "06_euler.png", args.mostrar)


if __name__ == "__main__":
    main()
