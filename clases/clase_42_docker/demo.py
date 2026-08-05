"""Programa pequeño para concentrarse en el contenedor, no en la aplicación."""

import platform
import sys

print("Python:", sys.version.split()[0])
print("Sistema:", platform.platform())
print("Resultado:", sum(i * i for i in range(5)))
