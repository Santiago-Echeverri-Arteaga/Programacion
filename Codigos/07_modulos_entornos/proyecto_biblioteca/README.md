# Proyecto de apoyo — Biblioteca instalable

Adaptación docente del ejemplo trabajado en el curso: conserva `Libreria`,
`cinematica` y funciones conocidas, separa lectura/cálculo/presentación y añade
configuración instalable. No incorpora cachés ni archivos compilados del ZIP.
Es una demostración de clase, no una solución de los laboratorios.

| Fecha | Guía | Archivos que se construyen/explican |
|---|---|---|
| 1 oct. | [03: archivos e importaciones](../../../guias/03_archivos_importaciones.md) | `ejemplo_importacion.py`, `explorar_archivo.py`, `Libreria/lectura.py`, `analizar_temporal.py` |
| 6 oct. | [04: pruebas e instalación](../../../guias/04_pruebas_instalacion.md) | `casos_defectuosos.py`, `biblioteca/pyproject.toml`, `tests/`, `analizar.py` |
| 7 oct. | [05: error y distribución](../../../guias/05_error_distribucion.md) | `experimento_integral.py`, documentación y wheel |

Desde esta carpeta, sin instalar:

```bash
python ejemplo_importacion.py
python explorar_archivo.py
python analizar_temporal.py
```

Para continuar, usar un entorno virtual y ejecutar:

```bash
python -m pip install -e ./biblioteca
python -m pip install pytest build twine
python analizar.py
python -m pytest -q
python experimento_integral.py
```

`casos_defectuosos.py` termina con `AssertionError` deliberadamente. No se
incluye en la suite que debe pasar. `analizar.py datos/ausente.csv` termina con
código 1 y un mensaje de ruta; el programa válido produce tres velocidades.

`biblioteca/Libreria` es el paquete importable; `biblioteca` es la raíz del
proyecto que pip instala. `pytest.ini` selecciona los tests locales. No añadir
`sys.path` en esos tests: utilizan la biblioteca instalada. El lector de clase
solo admite CSV pequeños numéricos sin campos entrecomillados; `csv.reader`
sería adecuado para formatos CSV más generales.

Construir desde `biblioteca` con `python -m build` y probar el wheel desde otra
carpeta y otro entorno. La [guía 05](../../../guias/05_error_distribucion.md)
detalla publicación opcional, licencia y nombres disponibles. Las mediciones
del cliente no son recursos incluidos en el paquete.
