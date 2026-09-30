# Guía 05 — Error numérico y distribución de la biblioteca

Fecha: miércoles 7 de octubre de 2026. Duración: 120 minutos.
Continuación de la [guía 04](04_pruebas_instalacion.md). Los contenidos nuevos
de esta sesión no entran en el parcial 2 del 8 de octubre.

## Secuencia

| Minutos | Explicación y ejecución | Práctica |
|---|---|---|
| 0–15 | `0.1 + 0.2`, igualdad y `math.isclose` | Distinguir valor almacenado y salida formateada |
| 15–40 | `experimento_integral.py`: puntos medios, error y costo | Predecir y explicar la razón de errores |
| 40–55 | Prueba manual, reducción de error y entradas inválidas | Separar defecto del código, error del método y redondeo |
| 55–75 | README, versión, licencia y `python -m build` | Inspeccionar wheel y distribución fuente |
| 75–100 | Instalación normal del wheel en un entorno externo nuevo | Intercambiar paquete y reproducir un ejemplo |
| 100–115 | Demostración de TestPyPI y explicación de PyPI | Identificar pasos y autenticación |
| 115–120 | Cierre y apertura del laboratorio 3 | Explicar evidencia y alcance |

## Experimento numérico

Desde la copia de trabajo y su entorno activo:

```bash
python -c "print(0.1 + 0.2); print(0.1 + 0.2 == 0.3)"
python -c "from math import isclose; print(isclose(0.1 + 0.2, 0.3))"
python experimento_integral.py
```

Construir en vivo el ciclo sobre `n=[1,2,4,8,16,32]`. Usar la referencia
analítica `integral de x² entre 0 y 1 = 1/3`; calcular error absoluto y razón
entre errores consecutivos. La función ya se trabajó en el curso; recorrer
acumulación y ubicación del punto medio antes de usarla.

Los primeros valores son 0.25, 0.3125 y 0.328125. Duplicar `n` reduce el error
aproximadamente por un factor cuatro en este experimento y duplica las
iteraciones. No equivale a demostrar convergencia en cualquier integral ni a
garantizar mejora indefinida al aumentar `n`. La referencia calculada en Python
tiene también redondeo. Formatear menos cifras no cambia el valor almacenado.
Cancelación y acumulación se amplían, si hay tiempo, con
[`sumas.py`](../clases/clase_21_algoritmos_error/sumas.py).

La suite del proyecto contiene una prueba manual con `n=1`, una comparación
de errores y rechazo de `n<=0` o no entero. No exigir igualdad exacta con `1/3`
para una aproximación por puntos medios. Ejecutar:

```bash
python -m pytest -q
```

## Construcción y prueba como usuario

Primero revisar documentación, unidades, versión y límites. Elegir licencia y
reconocer autoría antes de una publicación pública. El nombre docente es
ilustrativo; no se publica el ejemplo durante una ejecución automática.

Desde `practica_biblioteca`:

```bash
python -m pip install build twine
cd biblioteca
python -m build
ls dist
python -m twine check dist/*
cd ..
```

Explicar `.whl` frente a `.tar.gz`. `twine check` valida aspectos de metadatos
y descripción, no corrección matemática. Construir no sube nada a PyPI.

Crear un entorno externo al proyecto y conservar el wheel entregado por otra
pareja. Copiar antes de cambiar de carpeta:

```bash
mkdir ../prueba_usuario
cp biblioteca/dist/*.whl ../prueba_usuario/
cd ../prueba_usuario
python -m venv .venv
source .venv/bin/activate
ls
python -m pip install ./fisica_uq_ejemplo-0.1.0-py3-none-any.whl
python -c "import Libreria; print(Libreria.__file__); print(Libreria.velocidad(20, 5))"
```

En PowerShell activar con `.venv\Scripts\Activate.ps1`; los demás pasos siguen
usando el intérprete de ese entorno.

Usar el nombre real mostrado por `ls`; si se cambió nombre/versión no coincide
con el ejemplo. El archivo importado debe provenir del entorno de usuario, no
de la fuente original. La biblioteca no empaqueta las mediciones del cliente;
los usuarios proporcionan sus propios datos mediante una ruta.

## Publicación: demostración opcional

Volver al entorno de desarrollo de `practica_biblioteca` y a `biblioteca`.
Escoger un nombre disponible propio; actualizar metadatos y versión, reconstruir
y seleccionar únicamente archivos de esa versión (una carpeta `dist` vieja
puede contener versiones previas). Crear cuenta y token en TestPyPI. Mostrar:

```bash
python -m twine upload --repository testpypi dist/*
```

No escribir tokens en código, README, Git ni grabaciones. Introducirlos mediante
la autenticación de Twine. En un entorno limpio de usuario y con el nombre real:

```bash
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps nombre-del-proyecto
```

`--no-deps` corresponde al ejemplo sin dependencias; no es una regla general.
TestPyPI tiene cuentas e índice separados de PyPI. Una publicación real se hace
con `python -m twine upload ...`; después otros usuarios utilizan
`python -m pip install nombre-del-proyecto`. GitHub almacena código; PyPI
distribuye versiones instalables. Publicar no demuestra calidad científica.

Si falla cuenta/red/autenticación, explicar el flujo con la documentación y
terminar la prueba local del wheel. Nadie necesita una cuenta pública para
aprobar. No convertir la sesión en diagnóstico de servicios.

## Apertura del laboratorio 3

Abrir el [laboratorio 3](../laboratorios/lab03_modelo_verificable/README.md)
al terminar: biblioteca propia de integración, pruebas, tabla de convergencia
y wheel instalable. No exige publicar ni una EDO no practicada. Entrega: 20 de
octubre. El péndulo Euler-Cromer anterior se conserva como extensión opcional.

Referencias: [empaquetado](https://packaging.python.org/en/latest/tutorials/packaging-projects/),
[TestPyPI](https://packaging.python.org/en/latest/guides/using-testpypi/),
[punto flotante](https://docs.python.org/3.12/tutorial/floatingpoint.html).
