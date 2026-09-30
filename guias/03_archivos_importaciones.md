# Guía 03 — De la biblioteca del curso a las mediciones

Fecha: jueves 1 de octubre de 2026. Duración: 120 minutos.
Recupera lo pendiente de archivos/excepciones del 24 de septiembre y completa
la búsqueda de importaciones iniciada el 29. No supone que esos temas estén
dominados. Prerrequisitos: funciones, condicionales, ciclos, listas y tuplas.

## Objetivos y preparación

Construir rutas desde el script; leer con `with`; distinguir estructura,
contenido y requisitos físicos; capturar errores específicos; explicar
`PATH`, `sys.path`, `PYTHONPATH` y el papel de `__init__.py`.

El [proyecto de apoyo](../Codigos/07_modulos_entornos/proyecto_biblioteca/README.md)
adapta la biblioteca trabajada en clase. Es un ejemplo completo para estudiar,
no una solución ni un esqueleto del laboratorio 2. Desde la raíz del repositorio:

```bash
cp -R Codigos/07_modulos_entornos/proyecto_biblioteca ../practica_biblioteca
cd ../practica_biblioteca
python -m venv .venv
source .venv/bin/activate
pwd
ls
```

Comandos para Bash en Linux/WSL/macOS. Si el equipo solo reconoce `python3`,
usarlo para crear el entorno; activado este, comprobar `python --version`.
En PowerShell la activación es `.venv\Scripts\Activate.ps1`.
Trabajar en la copia para no sobrescribir los ejemplos ni los datos del curso.

## Secuencia de explicación, ejecución y práctica

| Minutos | Qué explicar y ejecutar | Trabajo del estudiante |
|---|---|---|
| 0–10 | Recuperar `import Libreria`, módulo/paquete/subpaquete y `__name__` | Identificar quién llama y quién calcula |
| 10–30 | Ejecutar `ejemplo_importacion.py`; retirar en la copia el `sys.path.insert` y observar el fallo | Explicar por qué se añade `biblioteca`, no `Libreria` |
| 30–45 | Ejecutar `explorar_archivo.py`; comentar `Path`, `resolve`, `parent`, `/`, `repr`, `readline`, `with` | Predecir dónde continúa el `for` después del encabezado |
| 45–70 | Construir en vivo `Libreria/lectura.py`, primero sin compactar conversiones | Comprobar encabezado, columnas y contenido |
| 70–90 | Construir `analizar.py`; ejecutar con el puente `analizar_temporal.py` | Calcular a mano el primer intervalo y explicar el signo |
| 90–110 | Alterar copias del CSV y ejecutar desde otra carpeta | Registrar instrucción que falla, línea y causa |
| 110–120 | Evidencia individual | Explicar una ruta y justificar una captura específica |

### Búsqueda de importaciones

```bash
python ejemplo_importacion.py
```

Mostrar `Path(__file__).resolve().parent`, `Path.cwd()` y `Libreria.__file__`.
Python busca módulos en `sys.path`; `PATH` es la búsqueda de ejecutables del
sistema. `PYTHONPATH` influye en la búsqueda de Python al iniciar. Añadir una
carpeta con `sys.path.insert(0, str(ubicacion))` cambia el proceso actual y le
da prioridad. No instala el paquete ni cambia permanentemente el equipo.

Retirar esa línea debe provocar `ModuleNotFoundError` en el entorno nuevo.
Restaurarla después de observar el fallo. La próxima clase resuelve esta misma
necesidad mediante instalación.

### Archivos y lectura

```bash
cat datos/mediciones.csv
python explorar_archivo.py
```

En vivo crear primero la lista vacía y el `with`; añadir el encabezado, después
el ciclo y por último la conversión. La lectura explícita separa:

```python
campos = linea.strip().split(",")
if len(campos) != 2:
    raise ValueError(f"línea {numero}: se esperaban dos columnas")
try:
    tiempo = float(campos[0])
    posicion = float(campos[1])
except ValueError as error:
    raise ValueError(f"línea {numero}: valor no numérico") from error
```

Explicar `enumerate(..., start=2)`, `append((tiempo, posicion))`, anotaciones de
tipo y `raise ... from error`. Las anotaciones no convierten ni validan datos.
Comparar después con la expresión compacta del [ejemplo original](../clases/clase_13_archivos_excepciones/leer_mediciones.py).
`float` acepta `nan`/`inf`: el ejemplo final usa `math.isfinite` para rechazarlos.
Una línea vacía se rechaza; el archivo sin mediciones también. Este lector es
para CSV pequeños numéricos sin campos entrecomillados; para CSV generales
mostrar `csv.reader`, sin exigir una API que no se haya practicado.

### Cálculo, errores y ubicación

```bash
python analizar_temporal.py
cp datos/mediciones.csv datos/prueba.csv
python analizar_temporal.py datos/prueba.csv
python analizar_temporal.py datos/ausente.csv
echo $?
cd ..
python practica_biblioteca/analizar_temporal.py
cd practica_biblioteca
```

El programa sin argumento usa datos junto al script. Una ruta introducida como
argumento es relativa al directorio de ejecución: hacer explícita la diferencia.
`sys.argv` es una lista de argumentos, no hace falta enseñar `argparse` aquí.

El resultado válido contiene velocidades 0.500, 1.400 y 2.500 m/s. El instante
inicial puede ser cero; el intervalo debe ser positivo. La validación de tiempos
crecientes pertenece al análisis; la lectura valida la tabla. La posición y el
desplazamiento negativos son admisibles.

Modificar una sola cosa en `datos/prueba.csv` cada vez: encabezado, texto no
numérico, columna faltante, columna extra, `nan`, tiempo repetido, solo encabezado.
Conservar `datos/mediciones.csv`. El programa principal captura
`FileNotFoundError` para informar una ruta ausente y `ValueError` para informar
datos inválidos; termina con código 1. No silencia fallos de programación ni
salta filas que podrían alterar la interpretación física.

## Evidencia y apertura del laboratorio 2

Explicar por qué el archivo funciona desde dos carpetas y por qué no se utilizó
`except Exception`. Abrir el [laboratorio 2](../laboratorios/lab02_python_nativo/README.md)
al terminar esta clase: Python nativo y comprobaciones manuales. No requiere
`pytest`, empaquetado, instalación ni publicación. Entrega: 13 de octubre.

Referencias: [módulos](https://docs.python.org/3.12/tutorial/modules.html),
[pathlib](https://docs.python.org/3.12/library/pathlib.html),
[excepciones](https://docs.python.org/3.12/tutorial/errors.html).
