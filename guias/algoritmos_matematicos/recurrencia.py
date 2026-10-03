"""Recurrencia de integrales: cálculo correcto no implica estabilidad numérica.

Referencia: recforw.py, Alex Gezerlis (2023). Véase 07_recurrencia.md.
Los valores inestables no se recortan ni se presentan como integrales fiables.
"""
from math import exp
from _apoyo import entero_positivo, real_finito, tabla


def integrales_recurrentes(cantidad: int) -> list[tuple[int, float]]:
    """Devuelve cantidad pares (índice, aproximación) desde índice 0.

    Requiere cantidad entera >=1, sin bool. Usa I0=1-exp(-1) e
    In=n*I(n-1)-exp(-1). No imprime ni modifica entradas. ValueError si el
    parámetro falla o se produce un valor no finito. La salida es la evaluación
    float de la recurrencia: puede perder positividad/monotonía por inestabilidad.
    Esas propiedades se diagnostican en la demostración; no se corrigen a escondidas.
    """
    cantidad = entero_positivo(cantidad, "cantidad")
    constante = exp(-1)
    anterior = 1 - constante
    resultados = [(0, anterior)]
    for n in range(1, cantidad):
        nuevo = real_finito(n * anterior - constante, f"I_{n}")
        resultados.append((n, nuevo))
        anterior = nuevo
    return resultados


def main() -> None:
    """Imprime 22 términos, marca fallos observables y compara I20 con referencia."""
    pares = integrales_recurrentes(22)
    filas = []
    for i, valor in pares:
        anterior = pares[i - 1][1] if i else float("inf")
        estado = "VIOLA propiedades" if valor <= 0 or valor >= anterior else "Sin violación visible"
        filas.append((i, valor, estado))
    tabla("RECURRENCIA | I_n = integral de x^n exp(-x) en [0,1]", ["n", "Aproximación float", "Diagnóstico"], filas)
    referencia = 0.0183504676972562
    valor20 = pares[20][1]
    print(f"\nReferencia I20: {referencia:.16g}")
    print(f"Error absoluto I20: {abs(valor20 - referencia):.8g}")
    print("Positividad y descenso son controles necesarios; no garantizan exactitud.")
    print("Los términos inestables se muestran para diagnosticar, no para ocultar el fallo.")


if __name__ == "__main__":
    main()
