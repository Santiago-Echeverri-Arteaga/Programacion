"""Resume eventos de detectores usando diccionarios y conjuntos."""

from __future__ import annotations


def contar(eventos: list[str]) -> dict[str, int]:
    conteos: dict[str, int] = {}
    for evento in eventos:
        conteos[evento] = conteos.get(evento, 0) + 1
    return conteos


if __name__ == "__main__":
    muestra = ["muon", "fondo", "muon", "electron", "fondo"]
    print("categorías:", sorted(set(muestra)))
    print("conteos:", contar(muestra))

