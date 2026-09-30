"""Clase 1: añadir la carpeta contenedora del paquete al proceso actual."""

from pathlib import Path
import sys

base = Path(__file__).resolve().parent
ubicacion = base / "biblioteca"
sys.path.insert(0, str(ubicacion))

import Libreria

if __name__ == "__main__":
    print("Directorio de ejecución:", Path.cwd())
    print("Archivo importado:", Libreria.__file__)
    print("Velocidad:", Libreria.velocidad(20, 5))
