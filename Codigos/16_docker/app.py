"""Programa mínimo para observar el entorno de un contenedor."""

from __future__ import annotations

import platform
from pathlib import Path


if __name__ == "__main__":
    print("Python:", platform.python_version())
    print("Sistema:", platform.system())
    print("Directorio:", Path.cwd())
    print("Archivos:", sorted(path.name for path in Path.cwd().iterdir()))

