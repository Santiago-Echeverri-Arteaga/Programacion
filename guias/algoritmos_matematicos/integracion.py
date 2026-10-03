"""Rectángulos, trapecios y Simpson con ciclos, contratos y gráfica.

Referencia: newtoncotes.py, Alex Gezerlis (2023). Véase 05_integracion.md.
Aquí n cuenta puntos; no se necesita NumPy para las reglas de integración.
"""
from _apoyo import (Funcion, evaluar, real_finito, entero_positivo, tabla,
                    opciones, preparar_grafica, guardar_figura)


def integrar(f: Funcion, a: float, b: float, n: int,
             metodo: str = "trapecios") -> float:
    """Devuelve una integral aproximada por una regla compuesta.

    Entradas: f escalar definida en [a,b], a<b finitos, n entero >=2 PUNTOS,
    metodo 'rectangulos', 'trapecios' o 'simpson'. Simpson exige n impar >=3.
    Salida: float finito en unidades de f por unidades de x. No imprime.
    ValueError: contrato inválido, malla indistinguible en float, evaluaciones
    o acumulaciones no finitas. No muta entradas ni demuestra exactitud.
    """
    a, b = real_finito(a, "a"), real_finito(b, "b")
    n = entero_positivo(n, "n", 2)
    if a >= b:
        raise ValueError("Se requiere a < b")
    if metodo not in ("rectangulos", "trapecios", "simpson"):
        raise ValueError("Método desconocido")
    if metodo == "simpson" and (n < 3 or n % 2 == 0):
        raise ValueError("Simpson requiere un número impar de puntos >= 3")
    h = real_finito((b - a) / (n - 1), "paso")
    if h <= 0 or a + h == a or b - h == b:
        raise ValueError("La malla no distingue puntos en precisión float")
    suma = 0.0
    cantidad = n - 1 if metodo == "rectangulos" else n
    for i in range(cantidad):
        x = b if i == n - 1 else a + i * h
        if metodo == "rectangulos":
            peso = 1.0
        elif metodo == "trapecios":
            peso = 0.5 if i in (0, n - 1) else 1.0
        elif i in (0, n - 1):
            peso = 1.0
        else:
            peso = 4.0 if i % 2 else 2.0
        suma = real_finito(suma + peso * evaluar(f, x), "suma ponderada")
    factor = h / 3 if metodo == "simpson" else h
    return real_finito(factor * suma, "integral")


def cuadrado(x: float) -> float:
    """Recibe x real y devuelve x²; integral exacta entre 0 y 2: 8/3."""
    return x**2


def main() -> None:
    """Compara tres reglas para x² en [0,2] y dibuja la regla de trapecios."""
    args = opciones()
    exacta = 8 / 3
    filas = []
    for n in (5, 11, 21, 51):
        for metodo in ("rectangulos", "trapecios", "simpson"):
            valor = integrar(cuadrado, 0, 2, n, metodo)
            filas.append((metodo, n, n - 1, valor, abs(valor - exacta)))
    tabla("INTEGRACIÓN | f(x) = x² en [0, 2]", ["Regla", "Puntos", "Intervalos", "Integral", "Error absoluto"], filas)
    print(f"\nReferencia exacta: {exacta:.12f}")
    if args.sin_grafica:
        return
    plt = preparar_grafica(args.mostrar)
    fig, ax = plt.subplots(figsize=(8, 4.8), layout="constrained")
    xs = [i / 100 for i in range(201)]
    nodos = [i / 2 for i in range(5)]
    ax.plot(xs, [cuadrado(x) for x in xs], color="#245fa7", linewidth=2, label="Función x²")
    for i in range(4):
        izq, der = nodos[i:i + 2]
        ax.fill([izq, izq, der, der], [0, cuadrado(izq), cuadrado(der), 0],
                color="#d76325", alpha=0.22, edgecolor="#a54b18", label="Trapecios (5 puntos)" if i == 0 else None)
    ax.plot(nodos, [cuadrado(x) for x in nodos], "o--", color="#a54b18")
    ax.set(title="Acumular áreas: regla de trapecios", xlabel="x (adimensional)", ylabel="f(x)")
    ax.legend()
    guardar_figura(fig, args.salida, "05_integracion.png", args.mostrar)


if __name__ == "__main__":
    main()
