"""Secante con contratos y control de denominador; referencia: secant.py,
Alex Gezerlis (2023). Véase 03_secante.md. No importa otro ejemplo para funcionar.
"""
from _apoyo import Funcion, Historial, controles, evaluar, real_finito, tabla


def secante(f: Funcion, anterior: float, actual: float, tolerancia: float = 1e-8,
            max_iter: int = 100) -> tuple[float | None, Historial]:
    """Devuelve (raíz aproximada o None, historial) mediante dos estados.

    Requiere puntos finitos, tolerancia>0 finita, max_iter entero positivo y f
    escalar determinista definida en cada evaluación. La fila registra
    (paso, siguiente, cambio absoluto, residuo). Acepta raíz exacta o cambio
    Y residuo <= tolerancia. Una raíz inicial tiene paso 0 y cambio 0.
    ValueError: entradas inválidas, evaluaciones no finitas o denominador cero.
    None: agotamiento sin satisfacer el criterio. No imprime ni muta entradas.
    Un denominador muy pequeño no nulo aún puede producir pasos grandes;
    el contrato no promete convergencia para cualquier pareja inicial.
    """
    tolerancia, max_iter = controles(tolerancia, max_iter)
    anterior = real_finito(anterior, "anterior")
    actual = real_finito(actual, "actual")
    fa, fb = evaluar(f, anterior), evaluar(f, actual)
    for x, fx in ((anterior, fa), (actual, fb)):
        if fx == 0:
            return x, [(0, x, 0.0, 0.0)]
    historial: Historial = []
    for paso in range(1, max_iter + 1):
        denominador = real_finito(fb - fa, "diferencia de evaluaciones")
        if denominador == 0:
            raise ValueError("La secante no está definida: f(actual) = f(anterior)")
        siguiente = real_finito(actual - fb * ((actual - anterior) / denominador), "siguiente")
        fs = evaluar(f, siguiente)
        cambio = real_finito(abs(siguiente - actual), "cambio")
        historial.append((paso, siguiente, cambio, abs(fs)))
        if fs == 0 or (cambio <= tolerancia and abs(fs) <= tolerancia):
            return siguiente, historial
        anterior, actual = actual, siguiente
        fa, fb = fb, fs
    return None, historial


def problema(x: float) -> float:
    """Devuelve x²-2 para x real; referencia positiva sqrt(2)."""
    return x**2 - 2


def main() -> None:
    """Imprime aproximaciones desde 1 y 2, con cambio y residuo separados."""
    raiz, historial = secante(problema, 1, 2)
    tabla("SECANTE | f(x) = x² - 2", ["Paso", "Aproximación", "Cambio", "Residuo"], historial)
    print(f"\nRaíz aproximada: {raiz}" if raiz is not None else "\nEstado: límite agotado.")


if __name__ == "__main__":
    main()
