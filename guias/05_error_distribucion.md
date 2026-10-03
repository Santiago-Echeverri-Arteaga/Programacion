# Guía 05 — Error numérico; distribución como extensión

Fecha: martes 13 de octubre de 2026. Bloque de error: 75 minutos; clase completa: 120 minutos. El 7 oct. se reemplaza por el [taller individual](taller_07_octubre_integracion/README.md).
Continuación de la [guía 04](04_pruebas_instalacion.md). El núcleo de error y convergencia
forma parte del parcial 2 del 21 oct. La construcción de wheel y publicación son extensiones no evaluables.

## Secuencia

| Minutos | Explicación y ejecución | Práctica |
|---|---|---|
| 0–10 | Punto flotante, igualdad y tolerancia | Distinguir redondeo de formato |
| 10–30 | Recuperar puntos medios ya presentes en `2026-2/` | Trazar un subintervalo y comprobar su valor |
| 30–55 | Tabla de aproximaciones y errores | Comparar n, 2n y 4n con una referencia |
| 55–75 | Pruebas y diagnóstico | Distinguir defecto, discretización y redondeo; caso inválido |
| 75–100 | Consolidación de instalación local según guía 04 | Ejecutar cliente desde otra carpeta |
| 100–110 | Pregunta y fuente del proyecto | Registrar elección breve |
| 110–120 | Cierre individual | Explicar una comprobación y registrar pendientes |

El bloque numérico reutiliza funciones ya conocidas, sin escribir otro algoritmo desde cero. Si un prerrequisito no se alcanza, reducir el alcance del lab. 3 y del corte del parcial; no trasladarlo a autoaprendizaje obligatorio. Las secciones de distribución siguientes son opcionales y quedan fuera de estos 120 minutos.

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

## Extensión opcional — construcción y prueba como usuario

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

## Continuidad con los laboratorios

El jueves 8 oct. se inicia el [laboratorio 2](../laboratorios/lab02_python_nativo/README.md), con Python nativo y archivos. El [laboratorio 3](../laboratorios/lab03_modelo_verificable/README.md) se abre el 15 oct. y se entrega el 27: puntos medios, pruebas, error e instalación local después de la consolidación del 13. No exige wheel, publicación ni una EDO no practicada. El péndulo se conserva como extensión opcional.

Referencias: [empaquetado](https://packaging.python.org/en/latest/tutorials/packaging-projects/),
[TestPyPI](https://packaging.python.org/en/latest/guides/using-testpypi/),
[punto flotante](https://docs.python.org/3.12/tutorial/floatingpoint.html).
