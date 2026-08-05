"""Tres lectores sobre el mismo archivo; comparar resultados y supuestos."""

import csv
from pathlib import Path

import numpy as np
import pandas as pd

ruta = Path(__file__).with_name("datos.csv")

with ruta.open(encoding="utf-8", newline="") as archivo:
    nativo = list(csv.DictReader(archivo))

numerico = np.genfromtxt(ruta, delimiter=",", names=True, usecols=(0, 1))
tabla = pd.read_csv(ruta)

print("nativo:", nativo)
print("NumPy:", numerico.dtype, numerico.shape)
print("Pandas:\n", tabla.dtypes)
