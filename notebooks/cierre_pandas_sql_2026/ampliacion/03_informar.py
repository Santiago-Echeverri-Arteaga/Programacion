from pathlib import Path
import argparse,json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=argparse.ArgumentParser(description='Comprueba la salida SQL y genera un informe local.')
p.add_argument('--carpeta',type=Path,required=True)
a=p.parse_args()
datos=pd.read_csv(a.carpeta/'datos.csv')
resumen=pd.read_csv(a.carpeta/'resumen.csv').sort_values('isla').reset_index(drop=True)
# Comprobaciones del contrato de salida: no basta con que exista el archivo.
esperado=datos.groupby('isla').agg(total=('masa_g','size'),masas_presentes=('masa_g','count'),masa_media_g=('masa_g','mean'),masa_sd_g=('masa_g','std')).reset_index().sort_values('isla').reset_index(drop=True)
esperado['cobertura_pct']=100*esperado.masas_presentes/esperado.total
pd.testing.assert_frame_equal(resumen,esperado,check_dtype=False,atol=1e-8,rtol=1e-10)
fig,ax=plt.subplots(figsize=(7,4))
ax.bar(resumen.isla,resumen.masa_media_g/1000,color=['#245e77','#408c8c','#d19a38'])
ax.set(xlabel='Isla',ylabel='Masa media observada (kg)',title='Resumen descriptivo por isla')
ax.spines[['top','right']].set_visible(False)
fig.tight_layout()
fig.savefig(a.carpeta/'masa_por_isla.png',dpi=160)
plt.close(fig)
lineas=['# Informe de la ejecución','',f'Registros: {len(datos)}. Masas observadas: {int(datos.masa_g.count())}.','', 'La media compara las observaciones disponibles. La composición de especies varía entre islas; esta comparación no demuestra un efecto causal de la isla. No se imputaron datos.','', '| Isla | Filas | Masas presentes | Media (g) | Cobertura (%) |','|---|---:|---:|---:|---:|']
for r in resumen.itertuples():
    lineas.append(f'| {r.isla} | {r.total} | {r.masas_presentes} | {r.masa_media_g:.2f} | {r.cobertura_pct:.2f} |')
lineas+=['','![Masa por isla](masa_por_isla.png)','','Fuente y hash: `procedencia.json`. La equivalencia SQL/Pandas comprueba el cálculo, no la validez de una conclusión causal.']
(a.carpeta/'informe.md').write_text('\n'.join(lineas),encoding='utf-8')
print('Resumen SQL comprobado con Pandas; informe y figura generados.')
