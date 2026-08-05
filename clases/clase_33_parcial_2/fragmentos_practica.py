"""Práctica pública de formas y polimorfismo."""

import numpy as np

a = np.arange(12).reshape(3, 4)
b = np.array([10, 20, 30, 40])
seleccion = (a + b)[a % 2 == 0]
print(seleccion.shape, seleccion.sum())
