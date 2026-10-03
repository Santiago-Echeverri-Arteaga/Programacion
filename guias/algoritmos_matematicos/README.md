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

Integración y Euler explican el papel de NumPy en el original y ofrecen pseudocódigo con ciclos y listas. Se pueden estudiar antes de aprender arreglos; ejecutar los originales sí requiere sus dependencias. En `newtoncotes.py` se explican las tres reglas; en `ivp_one.py` solo se desarrolla Euler y se identifica RK4 como otra regla para estudio posterior.

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

Se revisaron los archivos del [repositorio indicado por el docente](https://github.com/Santiago-Echeverri-Arteaga/Metodos_Numericos_Uniquindio/blob/a5c583075e984c3cc248afe5585200ca7cbfb5b9/examples/book_original/README.md), en el commit `a5c583075e984c3cc248afe5585200ca7cbfb5b9`. Su índice atribuye los programas a Alex Gezerlis, *Numerical Methods in Physics with Python*, segunda edición (Cambridge University Press, 2023).

Los enlaces fijan esa versión para que la explicación corresponda al código consultado. No se copian aquí programas completos ni se modifican los originales. Reglas, trazas y pseudocódigos se presentan como material explicativo propio con atribución de la referencia.

Los controles numéricos se contrastaron con las funciones originales usando problemas pequeños. Esto comprueba los ejemplos, no demuestra convergencia general ni que el original valide cualquier entrada.
