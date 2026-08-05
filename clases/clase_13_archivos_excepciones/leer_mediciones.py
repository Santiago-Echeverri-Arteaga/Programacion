"""Lectura explícita de un CSV pequeño con Python nativo."""

from pathlib import Path


def leer_posiciones(ruta: Path) -> list[tuple[float, float]]:
    filas: list[tuple[float, float]] = []
    with ruta.open(encoding="utf-8") as archivo:
        encabezado = archivo.readline().strip()
        if encabezado != "tiempo_s,posicion_m":
            raise ValueError("encabezado inesperado")
        for numero, linea in enumerate(archivo, start=2):
            try:
                tiempo, posicion = (float(campo) for campo in linea.split(","))
            except ValueError as error:
                raise ValueError(f"dato inválido en la línea {numero}") from error
            filas.append((tiempo, posicion))
    return filas


if __name__ == "__main__":
    ruta = Path(__file__).with_name("mediciones.csv")
    print(leer_posiciones(ruta))
