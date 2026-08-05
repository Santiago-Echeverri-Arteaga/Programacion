"""Ejemplos focalizados: solución simbólica y raíz numérica."""

import sympy as sp
from scipy.optimize import root_scalar

t, g, h = sp.symbols("t g h", positive=True)
soluciones = sp.solve(sp.Eq(h, g * t**2 / 2), t)
print("t simbólico:", soluciones)

raiz = root_scalar(lambda x: x**3 - 2, bracket=(1.0, 2.0))
print("raíz cúbica de 2:", raiz.root)
print("residuo:", raiz.root**3 - 2)
