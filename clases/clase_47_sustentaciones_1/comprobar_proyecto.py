"""Revisión estructural previa a la sustentación."""

from pathlib import Path

elementos = {
    "instrucciones": Path("README.md"),
    "dependencias": Path("requirements.txt"),
    "código": Path("src"),
    "pruebas": Path("tests"),
    "informe": Path("informe.pdf"),
    "declaración IA": Path("USO_IA.md"),
}
for nombre, ruta in elementos.items():
    print(f"{nombre:15} {'OK' if ruta.exists() else 'FALTA'}  {ruta}")
