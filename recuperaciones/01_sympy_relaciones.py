"""Demo de SymPy: despeje, derivación y sustitución."""

import sympy as sp

m, v, energia = sp.symbols("m v energia", positive=True)
ecuacion = sp.Eq(energia, m * v**2 / 2)
velocidad = sp.solve(ecuacion, v)[0]
derivada = sp.diff(m * v**2 / 2, v)

print("ecuación:", ecuacion)
print("velocidad despejada:", velocidad)
print("derivada respecto a v:", derivada)
print("comprobación para m=2 y v=3:", ecuacion.rhs.subs({m: 2, v: 3}))
