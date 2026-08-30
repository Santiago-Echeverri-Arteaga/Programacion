"""Tres demos pequeñas de SciPy con comprobaciones independientes."""

import numpy as np
from scipy.integrate import quad
from scipy.optimize import curve_fit, root_scalar


raiz = root_scalar(lambda x: x**3 - 2, bracket=(1.0, 2.0))
print("raíz cúbica de 2:", raiz.root)
print("residuo de la raíz:", raiz.root**3 - 2)

integral, error_estimado = quad(lambda x: x**2, 0.0, 1.0)
print("integral de x**2 entre 0 y 1:", integral)
print("diferencia frente a 1/3:", integral - 1 / 3)
print("error estimado por quad:", error_estimado)

x = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
y = np.array([1.1, 3.0, 5.2, 6.9, 9.1])


def recta(valor_x, pendiente, intercepto):
    return pendiente * valor_x + intercepto


parametros, _ = curve_fit(recta, x, y)
prediccion = recta(x, *parametros)
print("ajuste [pendiente, intercepto]:", parametros)
print("residuos:", y - prediccion)
