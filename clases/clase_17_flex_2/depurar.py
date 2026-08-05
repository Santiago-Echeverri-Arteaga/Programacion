"""Código defectuoso para lectura y depuración, no usar como referencia."""


def maximo(valores: list[float]) -> float:
    actual = 0.0
    for valor in valores:
        if valor < actual:
            actual = valor
    return actual


def contar_positivos(valores: list[float]) -> int:
    total = 0
    for indice in range(len(valores) - 1):
        if valores[indice] >= 0:
            total += 1
    return total
