"""Clase 3: comparar aproximaciones de puntos medios y su costo."""

from Libreria import integrar_cuadrado

if __name__ == "__main__":
    referencia = 1 / 3
    error_anterior = None
    for n in [1, 2, 4, 8, 16, 32]:
        aproximacion = integrar_cuadrado(0, 1, n)
        error = abs(aproximacion - referencia)
        razon = "--" if error_anterior is None else f"{error_anterior / error:.2f}"
        print(f"n={n:2d}, integral={aproximacion:.10f}, error={error:.3e}, razón={razon}")
        error_anterior = error
