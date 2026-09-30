"""Programa cliente: usa una biblioteca instalada, sin modificar sys.path."""

from pathlib import Path
import sys

from Libreria import leer_posiciones, velocidad


def analizar(ruta: Path) -> None:
    """Calcula velocidades de intervalos consecutivos, con tiempos crecientes."""
    filas = leer_posiciones(ruta)
    if len(filas) < 2:
        raise ValueError("se necesitan al menos dos mediciones")
    for i in range(1, len(filas)):
        t_anterior, x_anterior = filas[i - 1]
        t_actual, x_actual = filas[i]
        intervalo = t_actual - t_anterior
        if intervalo <= 0:
            raise ValueError(f"línea {i + 2}: los tiempos deben ser crecientes")
        v = velocidad(x_actual - x_anterior, intervalo)
        print(f"Entre {t_anterior:.2f} y {t_actual:.2f} s: v={v:.3f} m/s")


if __name__ == "__main__":
    base = Path(__file__).resolve().parent
    ruta = Path(sys.argv[1]) if len(sys.argv) > 1 else base / "datos" / "mediciones.csv"
    try:
        analizar(ruta)
    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta}", file=sys.stderr)
        raise SystemExit(1)
    except ValueError as error:
        print(f"No se pudieron analizar las mediciones: {error}", file=sys.stderr)
        raise SystemExit(1)
