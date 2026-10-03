"""Bisección con contrato, historial y demostración gráfica.

Referencia: bisection.py de Alex Gezerlis (2023); véase 01_biseccion.md.
Adaptación didáctica: parada por ancho, validación y raíces exactas explícitas.
"""
from _apoyo import (Funcion, Historial, controles, evaluar, real_finito, tabla,
                    opciones, preparar_grafica, guardar_figura)


def biseccion(f: Funcion, a: float, b: float, tolerancia: float = 1e-8,
              max_iter: int = 100) -> tuple[float | None, Historial]:
    """Busca una raíz en [a,b] conservando extremos de signos opuestos.

    Entradas: f escalar continua en el intervalo, a<b finitos, tolerancia>0
    finita (ancho máximo admitido), max_iter entero positivo. La continuidad
    es una hipótesis matemática, no una propiedad que esta función compruebe.
    Salida: (raíz aproximada o None, historial). Cada fila contiene
    (iteración, punto medio, ancho ANTES de reducir, abs(f(punto medio))).
    Una raíz inicial se registra como iteración 0. None significa agotamiento.
    ValueError: contrato inválido, falta de cambio de signo o evaluación inválida.
    No imprime ni modifica datos externos; acepta una raíz exacta sin dividir.
    """
    tolerancia, max_iter = controles(tolerancia, max_iter)
    a, b = real_finito(a, "a"), real_finito(b, "b")
    if a >= b:
        raise ValueError("Se requiere a < b")
    ancho = real_finito(b - a, "ancho")
    fa, fb = evaluar(f, a), evaluar(f, b)
    for x, fx in ((a, fa), (b, fb)):
        if fx == 0:
            return x, [(0, x, ancho, 0.0)]
    if (fa < 0) == (fb < 0):
        raise ValueError("Se requiere cambio de signo entre extremos")
    historial: Historial = []
    for paso in range(1, max_iter + 1):
        ancho = b - a
        medio = a + ancho / 2
        fm = evaluar(f, medio)
        historial.append((paso, medio, ancho, abs(fm)))
        if fm == 0 or ancho <= tolerancia:
            return medio, historial
        # Si float ya no permite partir el intervalo, no fingir convergencia.
        if medio == a or medio == b:
            return None, historial
        if (fa < 0) != (fm < 0):
            b = medio
        else:
            a, fa = medio, fm
    return None, historial


def problema(x: float) -> float:
    """Recibe x real y devuelve x²-2; su raíz positiva es sqrt(2)."""
    return x**2 - 2


def main() -> None:
    """Ejecuta el caso [1,2], muestra tabla y guarda una figura salvo opción contraria."""
    args = opciones()
    raiz, historial = biseccion(problema, 1, 2, tolerancia=1e-5)
    tabla("BISECCIÓN | f(x) = x² - 2", ["Paso", "Punto medio", "Ancho", "Residuo"], historial)
    print(f"\nResultado: {raiz:.10f}" if raiz is not None else "\nSin convergencia con el límite indicado.")
    if args.sin_grafica:
        return
    plt = preparar_grafica(args.mostrar)
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.5), layout="constrained")
    xs = [1 + i / 200 for i in range(201)]
    ax[0].plot(xs, [problema(x) for x in xs], color="#245fa7", label="x² − 2")
    ax[0].axhline(0, color="#555", linewidth=0.8)
    if raiz is not None:
        ax[0].scatter([raiz], [problema(raiz)], color="#d76325", label="Raíz aproximada", zorder=3)
    ax[0].set(title="El cero de la función", xlabel="x (adimensional)", ylabel="f(x)")
    ax[0].legend()
    ax[1].semilogy([f[0] for f in historial], [f[2] for f in historial], "o-", color="#14806c")
    ax[1].set(title="El intervalo se reduce", xlabel="Iteración", ylabel="Ancho del intervalo")
    guardar_figura(fig, args.salida, "01_biseccion.png", args.mostrar)


if __name__ == "__main__":
    main()
