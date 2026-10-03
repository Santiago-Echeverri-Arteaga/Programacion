"""Iteración de punto fijo con historial. Referencia: fixedpoint.py,
Alex Gezerlis (2023). Véase 02_punto_fijo.md para las diferencias didácticas.
"""
from _apoyo import Funcion, Historial, controles, evaluar, real_finito, tabla


def punto_fijo(g: Funcion, inicial: float, tolerancia: float = 1e-8,
               max_iter: int = 100) -> tuple[float | None, Historial]:
    """Aplica g repetidamente y devuelve (aproximación o None, historial).

    Requiere inicial real finito, tolerancia>0 finita, max_iter entero positivo
    y g determinista definida en todos los puntos visitados. Cada fila es
    (paso, nuevo, abs(nuevo-anterior), abs(g(nuevo)-nuevo)). El último campo
    es el residuo de punto fijo, no el error respecto a una solución conocida.
    Para aceptar el resultado exige cambio Y residuo <= tolerancia.
    No garantiza convergencia para cualquier g. None indica límite agotado.
    ValueError indica parámetros o evaluaciones no válidos. No imprime.
    """
    tolerancia, max_iter = controles(tolerancia, max_iter)
    anterior = real_finito(inicial, "inicial")
    historial: Historial = []
    for paso in range(1, max_iter + 1):
        nuevo = evaluar(g, anterior)
        cambio = real_finito(abs(nuevo - anterior), "cambio")
        residuo = real_finito(abs(evaluar(g, nuevo) - nuevo), "residuo")
        historial.append((paso, nuevo, cambio, residuo))
        if cambio <= tolerancia and residuo <= tolerancia:
            return nuevo, historial
        anterior = nuevo
    return None, historial


def transformacion(x: float) -> float:
    """Devuelve (x+2)/2 para x real; su punto fijo es 2."""
    return (x + 2) / 2


def main() -> None:
    """Imprime iteraciones de un ejemplo convergente y otro que agota el límite."""
    resultado, historial = punto_fijo(transformacion, 0, tolerancia=1e-5)
    tabla("PUNTO FIJO | g(x) = (x + 2) / 2", ["Paso", "Aproximación", "Cambio", "Residuo"], historial)
    print(f"\nResultado: {resultado}")
    def sin_punto_fijo(x: float) -> float:
        """Devuelve x+1: no existe un real que quede fijo bajo esta regla."""
        return x + 1
    resultado, historial = punto_fijo(sin_punto_fijo, 0, max_iter=5)
    tabla("CONTROL | g(x) = x + 1", ["Paso", "Aproximación", "Cambio", "Residuo"], historial)
    print("\nEstado: límite agotado; resultado =", resultado)


if __name__ == "__main__":
    main()
