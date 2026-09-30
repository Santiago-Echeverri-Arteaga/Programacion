"""Clase 1: posición de lectura, saltos de línea y cierre del archivo."""

from pathlib import Path

base = Path(__file__).resolve().parent
ruta = base / "datos" / "mediciones.csv"

if __name__ == "__main__":
    print("Ruta:", ruta)
    print("Directorio de ejecución:", Path.cwd())
    with ruta.open(encoding="utf-8") as archivo:
        print("Encabezado:", repr(archivo.readline()))
        for linea in archivo:
            print("Línea:", repr(linea))
    print("¿Archivo cerrado?", archivo.closed)
