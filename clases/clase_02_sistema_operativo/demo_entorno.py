"""Demo segura para relacionar programa, proceso, archivo y entorno."""

import os
import platform
import sys
from pathlib import Path

print("sistema:", platform.system(), platform.release())
print("Python:", sys.version.split()[0])
print("ejecutable:", sys.executable)
print("proceso actual:", os.getpid())
print("directorio de trabajo:", Path.cwd())
print("carpeta personal informada por el entorno:", Path.home())
