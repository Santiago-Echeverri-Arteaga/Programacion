"""Código para clínica: funciona, pero requiere análisis y refactorización."""

import matplotlib.pyplot as plt


def hacer(a, b, n):
    xs = []
    ys = []
    for i in range(n + 1):
        x = a + i * (b - a) / n
        xs.append(x)
        ys.append(x * x)
    plt.plot(xs, ys)
    plt.savefig("resultado.png")
    print(sum(ys) / len(ys))


if __name__ == "__main__":
    hacer(0, 2, 100)
