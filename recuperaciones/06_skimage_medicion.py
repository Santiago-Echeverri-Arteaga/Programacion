"""Demo de scikit-image: segmentar y medir discos sintéticos."""

import numpy as np
from skimage import draw, measure

imagen = np.zeros((80, 80), dtype=float)
fila_1, columna_1 = draw.disk((25, 25), 10, shape=imagen.shape)
fila_2, columna_2 = draw.disk((55, 50), 7, shape=imagen.shape)
imagen[fila_1, columna_1] = 0.9
imagen[fila_2, columna_2] = 0.6

mascara = imagen > 0.5
etiquetas = measure.label(mascara)
areas = [region.area for region in measure.regionprops(etiquetas)]

print("objetos detectados:", etiquetas.max())
print("áreas en píxeles:", areas)
