"""Clasificación didáctica por número de Reynolds."""


def regimen_flujo(reynolds: float) -> str:
    if reynolds < 0:
        raise ValueError("Re no puede ser negativo")
    if reynolds < 2300:
        return "laminar"
    if reynolds <= 4000:
        return "transición"
    return "turbulento"


for valor in (0, 2299, 2300, 4000, 4001):
    print(valor, regimen_flujo(valor))
