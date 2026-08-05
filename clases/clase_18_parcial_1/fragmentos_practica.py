"""Fragmentos públicos para practicar trazado en papel."""

valores = [3, -1, 4, 0]
acumulado = 0
for indice, valor in enumerate(valores):
    if valor > 0:
        acumulado += indice * valor
print(acumulado)
