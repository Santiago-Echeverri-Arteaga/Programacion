"""Mismo cálculo ejecutable como script e importable como módulo."""

from argparse import ArgumentParser


def energia_potencial(masa_kg: float, altura_m: float, gravedad: float = 9.81) -> float:
    """Devuelve m*g*h en julios."""
    return masa_kg * gravedad * altura_m


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("masa", type=float)
    parser.add_argument("altura", type=float)
    args = parser.parse_args()
    print(f"E_p = {energia_potencial(args.masa, args.altura):.3f} J")
