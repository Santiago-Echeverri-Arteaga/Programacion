"""Comportamientos del ejemplo previo: predecir antes de corregir.

No forman parte de la biblioteca instalada. El programa debe fallar: es una demo.
"""


def primos_original(num: int) -> bool:
    for divisor in range(2, num):
        if num % divisor == 0:
            return False
    return True


def factorial_original(n: int) -> int:
    return 1 if n <= 1 else n * factorial_original(n - 1)


if __name__ == "__main__":
    print("primos(1):", primos_original(1))
    print("factorial(-3):", factorial_original(-3))
    assert primos_original(1) is False
