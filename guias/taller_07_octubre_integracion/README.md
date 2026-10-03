# Taller individual — Análisis, depuración e integración de Python

**Miércoles 7 de octubre de 2026 · Duración: dos horas · Individual.**

Nueve ejercicios independientes basados en los programas trabajados en clase. Se evalúa la explicación del comportamiento, la identificación de errores y la coherencia entre contratos, código y resultados. Una salida correcta sin justificación no resuelve una pregunta de análisis.

Puedes consultar apuntes y códigos de clase. No se permite IA generativa ni compartir soluciones. No se exige pytest, instalación de paquetes ni herramientas científicas nuevas. Es una actividad formativa y no modifica los pesos de evaluación.

En los ejercicios de análisis registra tu predicción antes de ejecutar y contrástala con el resultado. En los de corrección entrega el fragmento corregido y un caso que muestre por qué era necesario cambiarlo. No hace falta construir una aplicación que reúna todos los ejercicios.

## 1. Entrada, conversión y control de un ciclo

El siguiente programa pretende acumular mediciones no negativas hasta que el usuario escriba `fin`:

```python
total = 0.0
cantidad = 0
while True:
    texto = input("Medición o fin: ")
    valor = float(texto)
    if texto == "fin":
        break
    if valor >= 0:
        total += valor
    cantidad += 1
print(total / cantidad)
```

1. Para las entradas sucesivas `"4"`, `"-2"`, `"6"`, `"fin"`, determina el valor de las variables después de cada entrada y dónde se interrumpe el programa. ¿Llega a imprimir un promedio?
2. Corrige el programa para que reconozca `fin`, rechace entradas no numéricas con un mensaje y continúe solicitando datos. Los valores negativos no deben entrar en la suma ni en el contador. Si no se aceptó ninguna medición, debe informar esa situación sin dividir.
3. Explica por qué cambiar `float(texto)` por `eval(texto)` no es una corrección adecuada para el contrato «recibir una medición numérica».

No se requiere tolerar variantes como `FIN` ni validar infinitos: el problema se limita a las condiciones indicadas.

## 2. Colecciones, alias y estado de una función

```python
def registrar(valores, registro):
    copia = valores.copy()
    copia[0] = copia[0] + 1
    registro["ultima"] = copia
    return copia

datos = [2, 4]
registro = {}
salida = registrar(datos, registro)
salida.append(8)
print(datos)
print(registro)
print(salida)
```

1. Predice las tres salidas. Identifica qué objetos son distintos y qué nombres o entradas del diccionario apuntan a la misma lista. ¿Copiar `valores` evita todas las modificaciones compartidas de este programa?
2. Cambia únicamente la asignación a `registro["ultima"]` para que modificaciones posteriores de `salida` no cambien lo almacenado en el registro. Justifica por qué basta en este caso de números.
3. Si `datos` fuera la tupla `(2, 4)`, señala la primera operación que fallaría. Propón un cambio en la creación de `copia` que permita recibir lista o tupla conservando el resto de la función.

## 3. Primalidad, `break` y `for…else`

Esta versión reproduce la estructura del algoritmo visto en clase:

```python
def es_primo(n):
    for divisor in range(2, n):
        if n % divisor == 0:
            resultado = False
            break
    else:
        resultado = True
    return resultado
```

1. Determina qué devuelve para `1`, `2` y `9`, justificando si el ciclo se ejecuta y si se alcanza su `else`. Para `9`, indica los divisores que se prueban.
2. Corrige la función para cumplir: «recibe un entero; devuelve `False` para todos los menores que 2 y decide primalidad para los demás». No necesitas optimizar la búsqueda ni comprobar el tipo de entrada.
3. Un compañero dice que el `else` significa «el último `if` fue falso». Refuta esa interpretación con uno de los casos anteriores.

## 4. Recursividad: contrato, caso base y progreso

Se consideran entradas enteras en ambos fragmentos:

```python
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)


def euclides(a, b):
    if b == 0:
        return a
    return euclides(b, a % b)
```

1. Escribe la secuencia de llamadas de `euclides(84, 30)` hasta el caso base y el valor que se devuelve. Explica qué cantidad disminuye y por qué termina para esos argumentos.
2. La primera función parece funcionar con 0 y 4. ¿Por qué esos casos no bastan para verificar el contrato «factorial de un entero no negativo»? Corrígela para rechazar entradas negativas mediante `ValueError`.
3. Para `factorial(4)`, distingue llegar al caso base de terminar toda la ejecución: muestra las multiplicaciones pendientes al llegar al caso base. No se pide convertirla a una versión iterativa.

## 5. Contratos con `*args`, `**kwargs` y `zip`

Diseña esta función, inspirada en el cálculo de varias velocidades de clase:

```python
def velocidades(intervalos, *pares, **opciones):
    # Tu implementación
    ...
```

Cada elemento de `intervalos` es una duración en segundos; cada elemento de `pares` contiene exactamente dos posiciones en metros. Se calcula `(posición final − posición inicial) / intervalo`. Puedes asumir números y pares bien formados, pero debes cumplir estas condiciones:

- Debe existir al menos un par y la cantidad de intervalos debe coincidir con la de pares.
- Todos los intervalos deben ser positivos. Ante un incumplimiento, lanza `ValueError`.
- La única opción admitida es `escala`, cuyo valor por defecto es 1 y multiplica cada velocidad calculada. Supón una escala numérica; una clave desconocida también debe producir `ValueError`.
- Devuelve una lista y no modifica las entradas ni imprime desde la función. Incluye un contrato breve como docstring.

Explica por qué usar `zip` sin verificar longitudes puede ocultar un error. Muestra cómo llamar a tu función desempaquetando estas colecciones:

```python
intervalos = [2, 4]
pares = [(1, 7), (8, 0)]
opciones = {"escala": 3.6}
```

Comprueba una llamada válida y una con longitudes distintas. Explica qué recibiría la función si usaras `pares` sin `*`, y qué ocurriría con la opción mal escrita `esacala`. No se pide una interfaz interactiva.

## 6. Paquetes, importaciones y rutas

Se tiene esta estructura:

```text
curso/
├── principal.py
├── datos/
│   └── mediciones.csv
└── biblioteca/
    └── Libreria/
        ├── __init__.py
        └── cinematica/
            ├── __init__.py
            └── codigo.py
```

`Libreria/__init__.py` contiene `from .cinematica import velocidad`.
`cinematica/__init__.py` contiene `from .codigo import velocidad`.
`codigo.py` contiene:

```python
def velocidad(dx, dt):
    return dx / dt

print("Demostración", velocidad(10, 2))
```

Y `principal.py` contiene:

```python
from pathlib import Path
import sys

sys.path.insert(0, "biblioteca")
import Libreria
print(Libreria.velocidad(12, 3))
ruta = Path("datos/mediciones.csv")
```

1. Ejecutando desde `curso/` en un proceso nuevo, predice las líneas impresas y explica cómo `velocidad` llega a estar disponible como `Libreria.velocidad`.
2. Si se lanza `python curso/principal.py` desde la carpeta superior, sin tener instalado el paquete ni configurado `PYTHONPATH`, explica los problemas de las dos rutas relativas. Reescribe únicamente la construcción de esas rutas usando la ubicación de `principal.py`.
3. Corrige `codigo.py` para conservar la demostración al ejecutarlo directamente y evitarla al importarlo. Explica la diferencia entre `sys.path` y `Libreria.__file__` en este diagnóstico.

No se requiere crear todos los archivos: entrega los fragmentos y la explicación.

## 7. Revisar un lector que oculta datos defectuosos

Contrato: «leer un CSV con encabezado exacto `tiempo_s,posicion_m`, devolver una lista de tuplas numéricas y rechazar encabezado incorrecto, filas con otra cantidad de campos, campos no numéricos o ausencia de mediciones». La función recibe un objeto `Path`. Los datos no contienen comas entre comillas.

```python
def leer(ruta):
    filas = []
    with ruta.open(encoding="utf-8") as archivo:
        archivo.readline()
        for numero, linea in enumerate(archivo, start=2):
            campos = linea.strip().split(",")
            try:
                filas.append((float(campos[0]), float(campos[1])))
            except Exception:
                pass
    return filas
```

1. Explica qué devuelve con este archivo y qué información se pierde:

```csv
tiempo_s,posicion_m
0,2
1,error
2,8,extra
```

2. Corrige el lector para cumplir su contrato. Un fallo en una fila debe identificar su número; no debes continuar omitiendo la fila. No captures `FileNotFoundError` dentro del lector ni impongas condiciones físicas adicionales sobre tiempos o posiciones.
3. Propón dos archivos pequeños que distingan la versión corregida de la original, indicando el comportamiento esperado de cada una. Justifica por qué devolver `[]` ante cualquier problema impediría distinguir situaciones diferentes.

## 8. Algoritmo de puntos medios: corregir a partir de una especificación

En clase se aproximó la integral de x² entre a y b mediante n subintervalos iguales: `ancho = (b-a)/n`, el centro del subintervalo i es `a + (i+0.5)*ancho`, y se suman las contribuciones `centro**2 * ancho`.

Revisa esta implementación deliberadamente defectuosa:

```python
def integrar_cuadrado(a, b, n):
    ancho = (b - a) / n
    if n <= 0 or b <= a:
        raise ValueError("intervalo o partición inválidos")
    acumulado = 0.0
    for i in range(n):
        centro = a + i * ancho
        acumulado = centro**2 * ancho
    return acumulado
```

1. Para `a=0`, `b=2`, `n=2`, calcula a mano qué devuelve este código y qué debe devolver el algoritmo especificado. Muestra las contribuciones, no solo el resultado final.
2. Corrige la ubicación de la validación y los errores del algoritmo. Puedes asumir que n es entero. Explica por qué arreglar únicamente la posición del centro no basta.
3. Elige un caso válido y uno inválido para comprobar tu corrección. Distingue una aproximación por puntos medios de la integral exacta; no se pide estudiar convergencia, orden del error ni usar bibliotecas numéricas.

## 9. Entorno, terminal y Git: diagnóstico de una secuencia

Este ejercicio utiliza Bash en Linux/WSL y un repositorio de estudiante que ya tiene remoto `origin` configurado. Analiza los comandos; no necesitas modificar tu entorno para responder.

```bash
python3 -m venv .venv
source .venv/bin/activate
python programa.py
```

1. Explica qué hace cada línea y por qué crear el entorno no equivale a activarlo. ¿Borrar la carpeta `.venv` borra el código de `programa.py`, que está junto a ella y no dentro? Justifica según la estructura de archivos.
2. Tras `git add respuestas.md` modificas de nuevo ese archivo y ejecutas `git commit -m "Respuestas"`. ¿Cuál de las dos versiones entra en el commit? Escribe cómo incluirías también la modificación posterior en un nuevo commit.
3. Distingue guardar un archivo, crear un commit y subirlo a GitHub. Indica el comando para ver los cambios pendientes y el necesario para enviar los commits al remoto, suponiendo que la rama ya tiene seguimiento configurado.

## Entrega

Sube a GitHub las respuestas numeradas y los fragmentos de código, con los casos de comprobación solicitados. Puedes usar un documento Markdown y archivos `.py` por ejercicio, o comentarios identificados junto al código. No se exige informe de laboratorio, video ni una estructura de proyecto. Entrega el enlace y el commit; no incluyas entornos virtuales.

Las respuestas deben permitir distinguir lo que predijiste, lo que observaste y por qué cambiaste el código. Identifica cualquier parte incompleta. La revisión considera corrección, cumplimiento de contratos, justificación y capacidad de detectar errores que una ejecución favorable no revela.
