from pathlib import Path
import argparse,hashlib,json
from urllib.request import urlopen
import pandas as pd
URL='https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv'
p=argparse.ArgumentParser(description='Descarga y valida observaciones reales para el pipeline.')
p.add_argument('--salida',type=Path,required=True)
p.add_argument('--entrada',type=Path,help='CSV local opcional para repetir una ejecución sin red')
a=p.parse_args()
a.salida.mkdir(parents=True,exist_ok=True)
if a.entrada:
    contenido=a.entrada.read_bytes()
    origen=str(a.entrada.resolve())
else:
    with urlopen(URL,timeout=45) as respuesta:contenido=respuesta.read()
    origen=URL
(a.salida/'fuente.csv').write_bytes(contenido)
df=pd.read_csv(a.salida/'fuente.csv',na_values=['NA'])
requeridas=['species','island','year','body_mass_g','flipper_length_mm']
faltantes=set(requeridas)-set(df.columns)
if faltantes:raise ValueError(f'Faltan columnas: {sorted(faltantes)}')
if df.empty:raise ValueError('La fuente no contiene observaciones')
if df[['species','island','year']].isna().any().any():raise ValueError('Faltan claves descriptivas')
for columna in ['year','body_mass_g','flipper_length_mm']:
    df[columna]=pd.to_numeric(df[columna],errors='raise')
    presentes=df[columna].dropna()
    if not presentes.gt(0).all() or not presentes.lt(float('inf')).all():
        raise ValueError(f'{columna}: se esperan valores positivos finitos')
if not (df.year%1==0).all():raise ValueError('El año debe ser entero')
tabla=df[requeridas].rename(columns={'species':'especie','island':'isla','year':'anio','body_mass_g':'masa_g','flipper_length_mm':'aleta_mm'}).copy()
tabla['anio']=tabla.anio.astype(int)
tabla.insert(0,'registro_id',range(1,len(tabla)+1))
tabla.to_csv(a.salida/'datos.csv',index=False,na_rep='')
(a.salida/'procedencia.json').write_text(json.dumps({'origen':origen,'sha256_fuente':hashlib.sha256(contenido).hexdigest(),'filas':len(tabla),'masas_presentes':int(tabla.masa_g.count()),'columnas_exportadas':tabla.columns.tolist()},indent=2,ensure_ascii=False),encoding='utf-8')
print(f'Preparadas {len(tabla)} filas; no se imputaron mediciones ausentes.')
