# De una regla matemática a un programa

Estas guías muestran para qué sirve un algoritmo matemático y cómo convertirlo en variables, decisiones, ciclos y funciones. **No necesitas haber cursado Métodos Numéricos.** Se proporciona una regla matemática: aceptamos su utilidad bajo las condiciones indicadas y nos concentramos en implementarla, seguirla y comprobar que el código respeta lo pedido.

Son material complementario de Programación. No sustituyen el taller del 7 de octubre, no amplían su entrega y no agregan temas obligatorios a parciales o laboratorios.

## Problemas y patrones de programación

| Guía y referencia | Problema matemático | Idea de programación |
|---|---|---|
| [1. Bisección](01_biseccion.md) · `bisection.py` | Encontrar un cero de una función | Conservar una condición y descartar media búsqueda |
| [2. Punto fijo](02_punto_fijo.md) · `fixedpoint.py` | Encontrar un valor que una transformación deja igual | Actualizar un estado y decidir cuándo parar |
| [3. Secante](03_secante.md) · `secant.py` | Aproximar una raíz usando dos estimaciones | Mantener y desplazar una pareja de estados |
| [4. Derivadas](04_derivadas.md) · `finitediff.py` | Estimar qué tan rápido cambia una función | Traducir una fórmula y comparar variantes |
| [5. Integración](05_integracion.md) · `newtoncotes.py` | Aproximar una acumulación o área con signo | Generar posiciones, asignar pesos y acumular |
| [6. Euler](06_euler.md) · `ivp_one.py`, función `euler` | Construir una evolución desde su ritmo de cambio | Actualizar y guardar una trayectoria |
| [7. Recurrencia](07_recurrencia.md) · `recforw.py` | Obtener integrales reutilizando la anterior | Transportar un resultado entre iteraciones |

Las implementaciones locales usan ciclos y listas de Python; no requieren NumPy. Matplotlib se usa únicamente para las figuras. Las guías también explican el papel de NumPy en los originales, que mantienen sus propias dependencias. En `newtoncotes.py` se explican las tres reglas; en `ivp_one.py` solo se desarrolla Euler y se identifica RK4 como otra regla para estudio posterior.

## Código junto a las guías

| Guía | Implementación local | Salida al ejecutar |
|---|---|---|
| [Bisección](01_biseccion.md) | [biseccion.py](biseccion.py) | Tabla de iteraciones y gráfica del intervalo |
| [Punto fijo](02_punto_fijo.md) | [punto_fijo.py](punto_fijo.py) | Tablas de convergencia y agotamiento |
| [Secante](03_secante.md) | [secante.py](secante.py) | Aproximaciones, cambios y residuos |
| [Derivadas](04_derivadas.md) | [derivadas.py](derivadas.py) | Comparación de reglas y gráfica del error |
| [Integración](05_integracion.md) | [integracion.py](integracion.py) | Tres reglas y representación de trapecios |
| [Euler](06_euler.md) | [euler.py](euler.py) | Trayectoria y comparación gráfica con referencia |
| [Recurrencia](07_recurrencia.md) | [recurrencia.py](recurrencia.py) | Valores y diagnóstico de pérdida de propiedades |

Desde la raíz del repositorio, por ejemplo:

```bash
python guias/algoritmos_matematicos/biseccion.py
python guias/algoritmos_matematicos/punto_fijo.py
python guias/algoritmos_matematicos/secante.py
python guias/algoritmos_matematicos/derivadas.py
python guias/algoritmos_matematicos/integracion.py
python guias/algoritmos_matematicos/euler.py
python guias/algoritmos_matematicos/recurrencia.py
```

Para las cuatro demostraciones gráficas instala Matplotlib en tu entorno con `python -m pip install matplotlib`. Por defecto guardan PNG en `figuras/` junto a estas guías, sin abrir ventanas. Admiten `--mostrar` para abrir la figura, `--salida ruta` para cambiar su carpeta o `--sin-grafica` para ejecutar solo las tablas sin Matplotlib. Punto fijo, secante y recurrencia solo necesitan la biblioteca estándar y muestran tablas.

Las figuras de ejemplo están incluidas en las guías. Se regeneran ejecutando sus programas. Los algoritmos no imprimen ni abren ventanas al importarlos: `main()` se ocupa de la demostración. [_apoyo.py](_apoyo.py) concentra validación, tablas y guardado de imágenes. Si copias un ejemplo a otra carpeta, conserva este archivo a su lado.

### Cómo leer tipos y contratos

`float` representa un real de precisión finita; los parámetros reales aceptan también enteros, pero no booleanos. `int` se usa para conteos. `Callable[[float], float]` describe una función que recibe y devuelve un real. `list[tuple[float, float]]` representa una lista de pares, como una trayectoria.

Las anotaciones no validan por sí solas: cada función comprueba las precondiciones indicadas en su docstring. Se documentan entradas, salida, significado de las unidades, errores y efectos secundarios. `ValueError` indica una entrada o evaluación inválida; `None` en los buscadores indica que se agotó el límite sin satisfacer su criterio. El historial sigue disponible para analizar lo ocurrido.

Bisección, punto fijo y secante devuelven `(resultado, historial)`. Cada fila del historial contiene `(iteración, aproximación, medida, residuo)`: en bisección la medida es el ancho anterior a reducir; en los otros dos es el cambio absoluto. El residuo es `abs(f(x))` para raíces y `abs(g(x)-x)` para punto fijo. No equivale al error respecto a una solución exacta.

## Del enunciado al algoritmo

Para cada problema identifica:

- **Entradas:** datos que entrega quien llama y condiciones que deben cumplir.
- **Estado:** información que debes recordar para realizar el siguiente paso.
- **Regla:** cálculo que transforma el estado anterior en el siguiente.
- **Repetición:** número de pasos o condición que la termina.
- **Salida:** valor o colección que se devuelve y su significado.
- **Comprobación:** un caso calculable a mano y una entrada que debe rechazarse.

Aceptar una fórmula no significa aceptar cualquier implementación. Una división por cero, una variable sobrescrita o un ciclo mal delimitado siguen siendo errores de programación. Distinguimos las condiciones matemáticas que asumimos de las validaciones que el programa puede realizar.

## Una función también puede ser un argumento

Los originales reciben una función matemática como argumento. Así puede cambiarse el problema sin reescribir el algoritmo:

```python
def cuadrado(x):
    return x**2


def cambio(funcion, x, h):
    return funcion(x + h) - funcion(x)


print(cambio(cuadrado, 3, 1))
```

Se pasa `cuadrado`, sin paréntesis: el algoritmo necesita llamarla con distintos valores. `cuadrado(3)` sería un número calculado una sola vez. El parámetro `funcion` recibe esa función; la llamada anterior devuelve 7. Este es el puente nuevo necesario para leer las firmas de los métodos.

## Qué contiene cada guía

Un problema concreto, la regla aceptada, un contrato, un recorrido manual, pseudocódigo, correspondencia con el archivo original y preguntas de implementación. El pseudocódigo es una especificación para traducir a Python, no un programa ejecutable literalmente.

Los ejemplos pequeños cambian deliberadamente la función usada por el libro. Así puedes comprobar una ejecución sin entender todavía su aplicación avanzada. Cuando cambia una parada o una validación respecto al original, se indica.

No necesitas estudiar toda la teoría del error para observar diferencias, pero un ejemplo favorable tampoco demuestra que un método sirve para todos los problemas.

## Procedencia

Se revisaron los archivos del [repositorio de Métodos Numéricos](https://github.com/Santiago-Echeverri-Arteaga/Metodos_Numericos_Uniquindio/blob/a5c583075e984c3cc248afe5585200ca7cbfb5b9/examples/book_original/README.md), en el commit `a5c583075e984c3cc248afe5585200ca7cbfb5b9`. Su índice atribuye los programas a Alex Gezerlis, *Numerical Methods in Physics with Python*, segunda edición (Cambridge University Press, 2023).

Los enlaces fijan esa versión para que la explicación corresponda al código consultado. Junto a cada guía se incluye una implementación didáctica revisada, con atribución del programa de referencia. Las funciones matemáticas originales siguen enlazadas en su versión consultada; los archivos locales aplican las validaciones y cambios de contrato descritos en cada guía.

Los controles numéricos se contrastaron con las funciones originales usando problemas pequeños. Esto comprueba los ejemplos, no demuestra convergencia general ni que el original valide cualquier entrada.
