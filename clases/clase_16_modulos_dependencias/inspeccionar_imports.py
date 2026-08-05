"""Muestra información útil para explicar imports y entornos."""

import sys
from pathlib import Path

print("Ejecutable:", sys.executable)
print("Archivo:", Path(__file__).resolve())
print("Nombre del módulo:", __name__)
print("Primeras rutas de búsqueda:")
for ruta in sys.path[:3]:
    print(" -", ruta)
