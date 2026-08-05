"""Patrones de comprobación para adaptar a una simulación."""

import numpy as np

rng_a = np.random.default_rng(42)
rng_b = np.random.default_rng(42)
serie_a = rng_a.choice((-1, 1), size=10).cumsum()
serie_b = rng_b.choice((-1, 1), size=10).cumsum()

assert serie_a.shape == (10,)
assert np.array_equal(serie_a, serie_b)
print("Comprobaciones mínimas superadas")
