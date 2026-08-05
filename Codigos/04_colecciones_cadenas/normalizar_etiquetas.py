"""Normaliza etiquetas conservando evidencia del texto original."""

from __future__ import annotations


def normalizar(texto: str) -> str:
    return "_".join(texto.strip().lower().split())


if __name__ == "__main__":
    originales = [" Sensor A ", "SENSOR   A", "Termopar B"]
    pares = [(texto, normalizar(texto)) for texto in originales]
    for original, limpio in pares:
        print(repr(original), "->", limpio)

