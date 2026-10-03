# Guía 04 — Probar e instalar nuestra biblioteca

Fecha: martes 6 de octubre de 2026. Duración: 120 minutos.
Continuación de la [guía 03](03_archivos_importaciones.md). Estos contenidos
se consolidan el 13 oct. y forman parte del corte del parcial 2 del 21 de octubre; no se evalúa memorización de metadatos.

## Objetivos

Convertir contratos en casos normales, límites e inválidos; distinguir `assert`
de validación; probar resultados/excepciones con `pytest`; describir módulos y
dependencias; instalar el proyecto con `pip` y utilizarlo fuera de su carpeta.

## Preparación para poder probar antes de explicar el empaquetado

En la copia de trabajo de la guía 03, con el entorno activo, usar la configuración suministrada por el docente: `python -m pip install pytest` y `python -m pip install -e ./biblioteca`. Es preparación guiada, no construcción autónoma de metadatos. Así `from Libreria import velocidad` funciona durante el bloque de pruebas; el bloque de instalación explica después lo que se hizo. No ejecutar la suite antes de preparar este entorno.

## Secuencia

| Minutos | Explicación y demo | Práctica |
|---|---|---|
| 0–25 | Contratos y fallos de `2026-2/` y `casos_defectuosos.py` | Predecir primo 1 y división por cero; ordenar validación antes del cálculo |
| 25–70 | Crear pruebas normales, de frontera y de excepción | Comparación con tolerancia y defecto intencional detectado |
| 70–95 | Revisar pyproject.toml e instalar en modo editable | Distinguir instalación de importación; comprobar ruta del módulo |
| 95–110 | Prueba CSV con datos pequeños | Encabezado inválido o archivo vacío; `tmp_path` guiado |
| 110–120 | Cierre individual | Explicar prueba y contrato; registrar dificultad pendiente |

Se estudian las pruebas antes de la configuración. El proyecto de apoyo incluye la configuración necesaria para ejecutar pruebas; la parametrización y los detalles del backend no son objetivos de memorización. `tmp_path` se trabaja de forma guiada; si no alcanza el tiempo, queda como ampliación opcional. La instalación local se consolida en 25 min el 13 oct.; el taller del 7 y el lab. 2 admiten comprobaciones manuales.

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
normal se comprueba el 13 oct. instalando desde la carpeta del proyecto, sin wheel obligatorio. Después de modificar
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
El laboratorio 3 se abre el 15 oct., tras practicar convergencia y consolidar instalación local el 13. El jueves 8 se inicia el laboratorio 2.

Referencias: [instalación local](https://pip.pypa.io/en/stable/topics/local-project-installs/),
[pytest](https://docs.pytest.org/en/stable/getting-started.html),
[pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/).


## Consolidación del 13 de octubre

En un entorno limpio, instalar normalmente desde la ruta local del proyecto con `python -m pip install /ruta/al/proyecto/biblioteca` (sustituir por la ruta real; entre comillas si tiene espacios). Ejecutar desde una carpeta distinta: `python -c "import Libreria; print(Libreria.__file__)"`. Verificar que el módulo proviene del entorno instalado. No confundir esta prueba con la instalación editable del 6 oct.; el modo editable enlaza la fuente de desarrollo. No se necesita publicar ni construir manualmente un wheel.
