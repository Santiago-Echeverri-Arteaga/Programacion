"""Práctica pública: leer, probar y explicar sin ejecutar inicialmente."""


def cambios_signo(valores: list[float]) -> list[int]:
    """Índices i donde valores[i-1] y valores[i] tienen signos opuestos."""
    indices = []
    for i in range(1, len(valores)):
        if valores[i - 1] * valores[i] < 0:
            indices.append(i)
    return indices


print(cambios_signo([2.0, -1.0, -3.0, 4.0, 0.0, -2.0]))
