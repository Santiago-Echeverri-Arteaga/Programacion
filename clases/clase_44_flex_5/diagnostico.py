"""Fragmentos acumulativos para predecir antes de ejecutar."""


def resumir_por_grupo(registros: list[tuple[str, float]]) -> dict[str, float]:
    acumulados: dict[str, list[float]] = {}
    for grupo, valor in registros:
        acumulados.setdefault(grupo, []).append(valor)
    return {grupo: sum(valores) / len(valores) for grupo, valores in acumulados.items()}


datos = [("A", 2.0), ("B", 3.0), ("A", 4.0)]
print(resumir_por_grupo(datos))
