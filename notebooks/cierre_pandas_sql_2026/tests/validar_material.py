"""Valida material y ejecuta notebooks con copias locales desde kernel limpio."""
from pathlib import Path
import ast
import hashlib
import json
import subprocess
import nbformat
from nbclient import NotebookClient

RAIZ = Path(__file__).resolve().parents[1]


def main():
    for folder in ['ampliacion','tests']:
        for archivo in (RAIZ/folder).glob('*.py'):
            ast.parse(archivo.read_text(encoding='utf-8-sig'),filename=str(archivo))
    for archivo in (RAIZ/'ampliacion').glob('*.sh'):
        subprocess.run(['bash','-n',str(archivo)],check=True)
    manifiesto = json.loads((RAIZ/'datos/procedencia.json').read_text(encoding='utf-8'))
    for entrada in manifiesto['archivos']:
        raw=(RAIZ/'datos'/entrada['archivo']).read_bytes()
        assert hashlib.sha256(raw).hexdigest()==entrada['sha256']
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
