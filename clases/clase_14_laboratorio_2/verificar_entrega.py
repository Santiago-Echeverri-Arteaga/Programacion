"""Comprobador estructural, no solución del Laboratorio 2."""

from pathlib import Path

REQUERIDOS = ("README.md", "informe.pdf", "src")
faltantes = [nombre for nombre in REQUERIDOS if not Path(nombre).exists()]
if faltantes:
    print("Faltan:", ", ".join(faltantes))
else:
    print("Estructura mínima presente; falta evaluar contenido y sustentación.")
