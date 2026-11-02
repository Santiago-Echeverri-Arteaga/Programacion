"""Valida material y ejecuta notebooks con copias locales desde kernel limpio."""
from pathlib import Path
import ast
import hashlib
import json
import runpy
from copy import deepcopy
import subprocess
import nbformat
from nbclient import NotebookClient

RAIZ = Path(__file__).resolve().parents[1]


def main():
    for folder in ['ampliacion','tests','ejemplos']:
        for archivo in (RAIZ/folder).glob('*.py'):
            ast.parse(archivo.read_text(encoding='utf-8-sig'),filename=str(archivo))
    for archivo in list((RAIZ/'ampliacion').glob('*.sh')) + list((RAIZ/'ejemplos').glob('*.sh')):
        subprocess.run(['bash','-n',str(archivo)],check=True)
    manifiesto = json.loads((RAIZ/'datos/procedencia.json').read_text(encoding='utf-8'))
    lector = runpy.run_path(str(RAIZ/'ampliacion/01_preparar.py'))['filas_respuesta']
    for entrada in manifiesto['archivos']:
        raw=(RAIZ/'datos'/entrada['archivo']).read_bytes()
        assert hashlib.sha256(raw).hexdigest()==entrada['sha256']
        assert 'start_date='+entrada['fecha_inicio'] in entrada['url']
        assert 'end_date='+entrada['fecha_fin'] in entrada['url']
        respuesta=json.loads(raw)
        filas=lector(respuesta,entrada['fecha_inicio'],entrada['fecha_fin'])
        assert len(filas)==entrada['filas']
        ausente=deepcopy(respuesta)
        ausente['daily']['temperature_2m_max'][0]=None
        assert lector(ausente,entrada['fecha_inicio'],entrada['fecha_fin'])[0][1] is None
        for defecto in ['unidades','longitud','fecha','numero']:
            mal=deepcopy(respuesta)
            if defecto=='unidades':mal['daily_units']['precipitation_sum']='inch'
            if defecto=='longitud':mal['daily']['temperature_2m_min'].pop()
            if defecto=='fecha':mal['daily']['time'][0]='2020-01-01'
            if defecto=='numero':mal['daily']['precipitation_sum'][0]=float('nan')
            try:lector(mal,entrada['fecha_inicio'],entrada['fecha_fin'])
            except ValueError:pass
            else:raise AssertionError('No se detecto: '+defecto)
    salida=RAIZ/'salidas_pruebas';salida.mkdir(exist_ok=True)
    for archivo in sorted(RAIZ.glob('*.ipynb')):
        notebook=nbformat.read(archivo,as_version=4)
        nbformat.validate(notebook)
        for celda in notebook.cells:
            if celda.cell_type=='code':ast.parse(celda.source)
        # Rechazar red en este kernel: la ejecucion debe ser realmente offline.
        notebook.cells.insert(0, nbformat.v4.new_code_cell(
            "import socket\n_original_connect=socket.socket.connect\n"
            "def sin_red(self, address):\n"
            "    raise RuntimeError('Prueba offline: red deshabilitada')\n"
            "socket.socket.connect=sin_red\n"))
        NotebookClient(notebook,timeout=120,kernel_name='python3',
                       resources={'metadata':{'path':str(RAIZ)}}).execute()
        nbformat.write(notebook,salida/archivo.name)
        print('Notebook validado y ejecutado offline:',archivo.name)
    print('Sintaxis Python/Bash, hashes y notebooks: OK')


if __name__=='__main__':main()
