"""Ejemplo 3: recorrer un resultado y preparar texto para un informe.
Ejecuta: python ejemplos/03_tablas_e_informe.py
Usa la copia real local; muestra texto por pantalla sin escribir resultados.
"""
from pathlib import Path
import pandas as pd
import numpy as np

carpeta = Path(__file__).resolve().parent
modulo = carpeta.parent
datos = pd.read_csv(modulo / 'datos' / 'meteorologia.csv')
resumen = datos.groupby('ciudad_id', as_index=False).agg(
    media_c=('tmax_c', 'mean'), presentes=('tmax_c', 'count'), dias=('fecha', 'size'))
resumen['cobertura'] = resumen['presentes'] / resumen['dias']

# itertuples permite recorrer filas del resultado pequeño y usar nombres de columnas.
# Los cálculos grandes se hacen con groupby, no con un ciclo de formato de texto.
lineas = ['Ciudad | Media de máximas (°C) | Cobertura de filas recibidas']
for fila in resumen.itertuples():
    if pd.isna(fila.media_c):
        temperatura = 'No disponible'
    else:
        temperatura = f'{fila.media_c:.2f}'  # .2f muestra dos decimales.
    cobertura = f'{fila.cobertura:.1%}'  # .1% muestra proporción como porcentaje.
    linea = f'{fila.ciudad_id} | {temperatura} | {cobertura}'
    lineas.append(linea)

# join coloca un salto de línea entre cadenas. No interpreta datos de entrada.
informe = '\n'.join(lineas)
print(informe)
# La cobertura anterior usa filas recibidas. Gold usa días esperados del calendario.
# No son intercambiables si falta un día completo de la tabla.

# En 03_informar.py, Matplotlib usa el backend Agg antes de importar pyplot:
# import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt
# Agg permite guardar PNG sin abrir una ventana: útil al automatizar con Bash.
# fig.savefig(ruta) escribe la figura; plt.close(fig) libera sus recursos.

# assert expresa una condición que esperamos verdadera; si no, detiene el programa.
# Sirve como comprobación del análisis, no sustituye las restricciones del servidor.
assert resumen['ciudad_id'].is_unique
# allclose compara números tolerando pequeñas diferencias de punto flotante.
np.testing.assert_allclose(resumen['cobertura'], resumen['presentes']/resumen['dias'])
print('Comprobaciones de claves y cobertura superadas.')
