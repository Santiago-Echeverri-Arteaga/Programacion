"""Clase 1: ejecutar el cliente antes de instalar la biblioteca."""

from pathlib import Path
import sys

base = Path(__file__).resolve().parent
sys.path.insert(0, str(base / "biblioteca"))

from analizar import analizar

if __name__ == "__main__":
    ruta = Path(sys.argv[1]) if len(sys.argv) > 1 else base / "datos" / "mediciones.csv"
    try:
        analizar(ruta)
    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta}", file=sys.stderr)
        raise SystemExit(1)
    except ValueError as error:
        print(f"No se pudieron analizar las mediciones: {error}", file=sys.stderr)
        raise SystemExit(1)
