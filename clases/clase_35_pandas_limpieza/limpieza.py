"""Auditoría explícita antes de limpiar una tabla pequeña."""

import pandas as pd

tabla = pd.DataFrame(
    {
        "tiempo_s": ["0.0", "0.1", "0.1", "error", "0.3"],
        "voltaje_v": [1.02, 1.05, 1.05, None, 1.18],
    }
)

print("tipos iniciales:\n", tabla.dtypes)
print("faltantes iniciales:\n", tabla.isna().sum())
print("duplicados:", tabla.duplicated().sum())

limpia = tabla.drop_duplicates().copy()
limpia["tiempo_s"] = pd.to_numeric(limpia["tiempo_s"], errors="coerce")
print("auditoría posterior:\n", limpia.isna().sum())
