"""Demo de xarray: campo con dimensiones y coordenadas etiquetadas."""

import numpy as np
import xarray as xr

temperatura = xr.DataArray(
    np.array([[20.0, 20.5, 21.0], [19.8, 20.2, 20.7]]),
    dims=("tiempo_s", "posicion_m"),
    coords={"tiempo_s": [0, 10], "posicion_m": [0.0, 0.5, 1.0]},
    attrs={"unidades": "degC", "descripcion": "placa unidimensional"},
)

print(temperatura)
print("perfil en t=10 s:", temperatura.sel(tiempo_s=10).values)
print("promedio temporal:", temperatura.mean(dim="tiempo_s").values)
