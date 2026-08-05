"""Agrupación y unión con validación explícita."""

import pandas as pd

mediciones = pd.DataFrame(
    {"sensor_id": [1, 1, 2, 2], "voltaje_v": [1.0, 1.2, 0.8, 0.9]}
)
sensores = pd.DataFrame(
    {"sensor_id": [1, 2], "ubicacion": ["norte", "sur"]}
)

resumen = mediciones.groupby("sensor_id", as_index=False).agg(
    media_v=("voltaje_v", "mean"), cantidad=("voltaje_v", "size")
)
resultado = resumen.merge(sensores, on="sensor_id", how="left", validate="one_to_one")
print(resultado)
