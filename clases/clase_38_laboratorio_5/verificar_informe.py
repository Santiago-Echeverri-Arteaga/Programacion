"""Lista estructural mínima para el Laboratorio 5."""

from pathlib import Path

for ruta in (Path("datos/raw"), Path("src"), Path("resultados"), Path("informe.pdf")):
    estado = "OK" if ruta.exists() else "FALTA"
    print(f"{estado:5} {ruta}")
