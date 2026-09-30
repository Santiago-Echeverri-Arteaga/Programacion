# Guía 04 — Probar e instalar nuestra biblioteca

Fecha: martes 6 de octubre de 2026. Duración: 120 minutos.
Continuación de la [guía 03](03_archivos_importaciones.md). Estos contenidos
nuevos quedan fuera del parcial 2 del 8 de octubre.

## Objetivos

Convertir contratos en casos normales, límites e inválidos; distinguir `assert`
de validación; probar resultados/excepciones con `pytest`; describir módulos y
dependencias; instalar el proyecto con `pip` y utilizarlo fuera de su carpeta.

## Secuencia

| Minutos | Explicación y demo | Práctica |
|---|---|---|
| 0–15 | Ejecutar `casos_defectuosos.py` y leer `AssertionError` | Predecir primo 1 y factorial negativo antes de ejecutar |
| 15–30 | Revisar contratos, `return`/`print`, importaciones explícitas y relativas | Reemplazar un `import *` en una copia del ejemplo previo |
| 30–60 | Crear `pyproject.toml`, README y realizar instalación editable | Importar el paquete desde otra carpeta |
| 60–90 | Crear dos pruebas simples y una de excepción | Introducir un signo u operación incorrecta y detectarlo |
| 90–110 | Probar lectura con `tmp_path` y datos creados por la prueba | Añadir encabezado incorrecto o archivo sin mediciones |
| 110–120 | Verificación individual | Explicar entorno, instalación y una prueba |

## Comprobaciones antes de instalar

Desde la copia `practica_biblioteca`, activar el entorno de la primera clase:

```bash
source .venv/bin/activate
python casos_defectuosos.py
```

El fallo es deliberado, no un requisito para pasar. Contrastar el contrato con
el resultado; `assert` comprueba expectativas en pruebas. Validar entradas con
`if`/`raise`: los `assert` pueden desactivarse al ejecutar Python con `-O`.
La biblioteca final corrige `primos(1)` y deja la presentación al cliente.
Las funciones recursivas del ZIP sirven para discusión, no son requisito nuevo.

## Crear la configuración e instalar

Recorrer el [pyproject.toml](../Codigos/07_modulos_entornos/proyecto_biblioteca/biblioteca/pyproject.toml):
backend, nombre, versión, descripción, README, Python mínimo, dependencias y
descubrimiento de paquetes. El archivo va en `biblioteca`, junto a `Libreria`.
En vivo crear ese archivo y `biblioteca/README.md` en la copia de trabajo.

```bash
python --version
python -m pip --version
python -m pip install -e ./biblioteca
python -m pip show fisica-uq-ejemplo
python analizar.py
cd ..
python -c "import Libreria; print(Libreria.__file__)"
cd practica_biblioteca
```

`python -m pip` usa el intérprete seleccionado. `pip install` instala una
distribución; `import` carga un módulo/paquete. El nombre de distribución
`fisica-uq-ejemplo` no tiene que coincidir con el nombre importable `Libreria`.
La instalación editable permite desarrollar sobre la fuente; una instalación
normal se comprueba con el wheel en la tercera clase. Después de modificar
metadatos se reinstala. Usar un proceso nuevo para observar cambios de código.

`analizar.py` ya no modifica `sys.path`. No desinstalar ni modificar el entorno
global del equipo. Si persiste `ModuleNotFoundError`, comprobar intérprete,
`python -m pip show ...` y el archivo importado antes de agregar más rutas.

## Pruebas simples primero

```bash
python -m pip install pytest
python -m pytest -q
```

Crear en vivo `tests/test_cinematica.py` empezando con:

```python
import pytest
from Libreria import velocidad

def test_velocidad():
    assert velocidad(20, 5) == pytest.approx(4.0)

def test_intervalo_cero():
    with pytest.raises(ValueError):
        velocidad(20, 0)
```

Explicar preparar–ejecutar–comprobar, descubrimiento de `test_`, tolerancia y
excepción esperada. Cambiar temporalmente `/` por `*`, ejecutar e interpretar
el fallo; restaurar antes de seguir. `pytest.raises` comprueba que se rechaza
una entrada, no reemplaza la validación de la función.

Crear `tests/test_lectura.py` con una prueba que recibe `tmp_path`, escribe un
CSV pequeño con `write_text(..., encoding="utf-8")` y comprueba el resultado.
Mostrar después una fila inválida y `match="línea 2"`. Los datos de prueba no
deben depender de un CSV que otra persona pueda modificar. Las pruebas completas
del proyecto incluyen parametrización: es una extensión después de comprender
las funciones simples, no una sintaxis que deba memorizarse.

Ejecutar pruebas concretas:

```bash
python -m pytest tests/test_lectura.py -q
python -m pytest -k intervalo -q
```

La configuración local está en `practica_biblioteca/pytest.ini`. Desde la raíz
del repositorio docente, `pytest.ini` selecciona otra suite; no confundirlas.

## Cierre

Cada estudiante explica una prueba que detecta un defecto real y la diferencia
entre instalar e importar. `pytest` es una herramienta de desarrollo, no una
dependencia requerida para llamar a `velocidad`. Los módulos estándar no se
instalan con pip. La publicación en PyPI no es necesaria para instalación local.
El laboratorio 3 se abre después de la siguiente clase, cuando también se haya
practicado convergencia y construcción del wheel.

Referencias: [instalación local](https://pip.pypa.io/en/stable/topics/local-project-installs/),
[pytest](https://docs.pytest.org/en/stable/getting-started.html),
[pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/).
