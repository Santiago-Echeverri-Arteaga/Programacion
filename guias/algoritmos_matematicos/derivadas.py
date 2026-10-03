"""Diferencias finitas con tablas y gráfica de error.

Referencia: finitediff.py, Alex Gezerlis (2023). Véase 04_derivadas.md.
El cálculo usa la biblioteca estándar; Matplotlib solo dibuja la demostración.
"""
from math import exp, sin, cos
from _apoyo import (Funcion, evaluar, real_finito, tabla, opciones,
                    preparar_grafica, guardar_figura)


def derivada(f: Funcion, x: float, h: float, metodo: str = "centrada") -> float:
    """Aproxima f'(x) con una diferencia adelantada o centrada.

    Entradas: f escalar, x finito, h>0 finito, metodo 'adelantada' o 'centrada'.
    f debe estar definida en los puntos evaluados. La centrada usa x±h/2 y
    divide por h. Devuelve un float finito, sin imprimir ni modificar entradas.
    ValueError: contrato inválido, resultado no finito o paso demasiado pequeño
    para distinguir los puntos en float. No asegura que h sea adecuado al modelo.
    """
    x, h = real_finito(x, "x"), real_finito(h, "h")
    if h <= 0:
        raise ValueError("h debe ser positivo")
    if metodo == "adelantada":
        izquierda, derecha = x, real_finito(x + h, "x+h")
    elif metodo == "centrada":
        izquierda = real_finito(x - h / 2, "x-h/2")
        derecha = real_finito(x + h / 2, "x+h/2")
    else:
        raise ValueError("metodo debe ser 'adelantada' o 'centrada'")
    if izquierda == derecha or (metodo == "centrada" and (izquierda == x or derecha == x)):
        raise ValueError("h no permite distinguir los puntos en precisión float")
    return real_finito((evaluar(f, derecha) - evaluar(f, izquierda)) / h, "derivada")


def funcion(x: float) -> float:
    """Devuelve exp(sin(2x)) para x real; función suave del ejemplo de referencia."""
    return exp(sin(2 * x))


def referencia(x: float) -> float:
    """Devuelve 2*exp(sin(2x))*cos(2x), derivada analítica de funcion."""
    return 2 * exp(sin(2 * x)) * cos(2 * x)


def main() -> None:
    """Compara dos reglas en x=0.5; muestra resultados y guarda errores vs h."""
    args = opciones()
    x = 0.5
    exacta = referencia(x)
    filas = []
    for i in range(1, 12):
        h = 10.0 ** (-i)
        adelantada = derivada(funcion, x, h, "adelantada")
        centrada = derivada(funcion, x, h)
        filas.append((h, adelantada, centrada, abs(adelantada - exacta), abs(centrada - exacta)))
    print(f"Referencia en x={x}: {exacta:.12f}")
    tabla("DERIVADAS | f(x) = exp(sin(2x))", ["h", "Adelantada", "Centrada", "Error adel.", "Error cent."], filas)
    if args.sin_grafica:
        return
    plt = preparar_grafica(args.mostrar)
    fig, ax = plt.subplots(figsize=(8, 4.8), layout="constrained")
    for columna, etiqueta, color in ((3, "Adelantada", "#d76325"), (4, "Centrada", "#245fa7")):
        # Cero no tiene logaritmo; si apareciera, se conserva en tabla y se omite aquí.
        puntos = [(f[0], f[columna]) for f in filas if f[columna] > 0]
        ax.loglog([p[0] for p in puntos], [p[1] for p in puntos], "o-", label=etiqueta, color=color)
    ax.invert_xaxis()
    ax.set(title="Reducir h no siempre reduce el error", xlabel="Paso h (de mayor a menor)", ylabel="Error absoluto frente a la derivada exacta")
    ax.legend()
    guardar_figura(fig, args.salida, "04_derivadas.png", args.mostrar)


if __name__ == "__main__":
    main()
