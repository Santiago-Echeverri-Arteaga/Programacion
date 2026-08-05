"""Verifica simbólicamente una solución del oscilador armónico."""

import sympy as sp


t, amplitud, omega = sp.symbols("t A omega", positive=True, real=True)
x = amplitud * sp.cos(omega * t)
residuo = sp.simplify(sp.diff(x, t, 2) + omega**2 * x)

if __name__ == "__main__":
    print("x(t) =", x)
    print("x'' + omega² x =", residuo)

