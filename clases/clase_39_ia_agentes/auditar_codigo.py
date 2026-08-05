"""Auditor estático mínimo: produce pistas, no certifica corrección."""

import ast
from argparse import ArgumentParser
from pathlib import Path

parser = ArgumentParser()
parser.add_argument("archivo", type=Path)
args = parser.parse_args()

arbol = ast.parse(args.archivo.read_text(encoding="utf-8"), filename=str(args.archivo))
for nodo in ast.walk(arbol):
    if isinstance(nodo, ast.ExceptHandler) and nodo.type is None:
        print(f"línea {nodo.lineno}: except desnudo; revisar qué error pretende tratar")
    if isinstance(nodo, ast.Call) and isinstance(nodo.func, ast.Name) and nodo.func.id == "eval":
        print(f"línea {nodo.lineno}: uso de eval; revisar seguridad y necesidad")

print("La ausencia de avisos no demuestra corrección algorítmica ni física.")
