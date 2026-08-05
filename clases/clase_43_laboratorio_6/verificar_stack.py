"""Chequeos locales no destructivos antes de entregar el laboratorio."""

from pathlib import Path

requeridos = [Path("compose.yaml"), Path("Dockerfile"), Path("sql"), Path("src")]
for ruta in requeridos:
    print("OK" if ruta.exists() else "FALTA", ruta)

for archivo in Path(".").rglob("*"):
    if archivo.is_file() and archivo.suffix in {".py", ".sql", ".yaml", ".yml"}:
        contenido = archivo.read_text(encoding="utf-8", errors="ignore").lower()
        if "password=" in contenido or "postgresql://postgres:" in contenido:
            print("REVISAR posible secreto:", archivo)
