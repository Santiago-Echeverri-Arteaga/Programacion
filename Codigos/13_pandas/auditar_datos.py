"""Auditoría reproducible de datos sintéticos de enfriamiento."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def cargar_y_normalizar(ruta: Path) -> pd.DataFrame:
    datos = pd.read_csv(ruta, parse_dates=["instante"])
    datos["es_duplicado"] = datos.duplicated(
        subset=["instante", "sensor"], keep="first"
    )
    datos["temperatura_c"] = datos["temperatura"]
    mascara_kelvin = datos["unidad"].eq("K")
    datos.loc[mascara_kelvin, "temperatura_c"] -= 273.15
    datos["utilizable"] = (
        datos["temperatura_c"].notna()
        & ~datos["es_duplicado"]
        & datos["calidad"].ne("descartada")
    )
    return datos


if __name__ == "__main__":
    ruta = Path("datos/enfriamiento_sintetico_sucio.csv")
    datos = cargar_y_normalizar(ruta)
    print(datos.groupby("sensor")["utilizable"].agg(["sum", "count"]))

