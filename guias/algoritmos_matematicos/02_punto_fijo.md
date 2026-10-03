# 2. Punto fijo: aplicar una regla al resultado anterior

Código de referencia: [fixedpoint.py](https://github.com/Santiago-Echeverri-Arteaga/Metodos_Numericos_Uniquindio/blob/a5c583075e984c3cc248afe5585200ca7cbfb5b9/examples/book_original/fixedpoint.py). Autor del original: Alex Gezerlis, *Numerical Methods in Physics with Python*, segunda edición, 2023. La explicación y los ejemplos pequeños son material didáctico elaborado para Programación.

## Implementación documentada

Archivo: [punto_fijo.py](punto_fijo.py).

```python
punto_fijo(g, inicial, tolerancia=1e-8, max_iter=100)
```

Devuelve resultado e historial. La versión ejecutable refuerza el pseudocódigo: exige cambio y residuo de punto fijo menores o iguales a la tolerancia. Evalúa g también en el nuevo punto; por eso requiere una función sin efectos secundarios. Los tipos y el contrato completo están en la firma y el docstring.

Ejecuta desde la raíz del repositorio:

```bash
python guias/algoritmos_matematicos/punto_fijo.py
```

## Qué problema resuelve

Un punto fijo es un número que no cambia al aplicar una función: x=g(x). Algunas ecuaciones pueden escribirse así. Por ejemplo, `g(x)=(x+2)/2` tiene como punto fijo 2.

El patrón sirve para resolver relaciones donde la incógnita aparece en ambos lados y para actualizar estimaciones en modelos físicos. No toda reescritura produce una iteración que se acerque a una solución.

## Regla matemática aceptada

Para la g del ejemplo, repetir `nuevo=g(anterior)` aproxima su punto fijo. Asumimos esa propiedad para esta función; no se pide demostrarla ni decidir qué transformaciones funcionan en general.

La tarea es conservar el estado correcto, comparar antes de sobrescribirlo y terminar explícitamente.

## Contrato

Entradas: g, valor inicial, tolerancia absoluta positiva y límite entero positivo de pasos. g debe estar definida en los valores generados.

Salida: aproximación cuando el cambio absoluto sea pequeño, o `None` si se agota el límite. Un cambio pequeño es un criterio operativo; no prueba cercanía a una solución de cualquier problema.

## Traza manual

Con x inicial 0 y g(x)=(x+2)/2:

| Paso | anterior | nuevo | Cambio absoluto |
|---|---:|---:|---:|
| 1 | 0 | 1 | 1 |
| 2 | 1 | 1,5 | 0,5 |
| 3 | 1,5 | 1,75 | 0,25 |
| 4 | 1,75 | 1,875 | 0,125 |

Para calcular el siguiente basta el anterior. Guardar una lista adicional permite estudiar la trayectoria, pero no es necesario para aplicar la regla.

## Del enunciado al ciclo

```text
validar tolerancia y límite
anterior = valor inicial
repetir como máximo max_iter veces:
    nuevo = g(anterior)
    cambio = abs(nuevo - anterior)
    si cambio <= tolerancia:
        devolver nuevo
    anterior = nuevo
devolver None
```

Si sobrescribes el anterior antes de calcular la diferencia, obtendrías cambio cero aunque no hayas alcanzado el punto fijo.

## Correspondencia con el original

`fixedpoint` recibe g y `xold`; calcula `xnew`, imprime y decide si usa `break`. Solo si continúa asigna `xold=xnew`. El `else` del `for` establece `None` cuando no hubo interrupción por su criterio de parada.

La g original es `exp(x-sqrt(x))`. Las condiciones iniciales 0,99 y 2,499 corresponden a ese problema; no son constantes necesarias en todo algoritmo de punto fijo. La raíz cuadrada limita el dominio y la exponencial puede desbordarse.

El original divide el cambio por `xnew` para compararlo relativamente. Esta guía usa diferencia absoluta para poder estudiar un punto fijo cero sin esa división. Una evaluación fuera del dominio puede lanzar una excepción: `None` solo representa agotamiento del ciclo, no cualquier fallo.

## Comprobaciones y preguntas

Para g(x)=(x+2)/2 y x inicial 0, el original produce aproximadamente 1,9999999851. Tu implementación debe acercarse a 2; pueden cambiar las últimas cifras por la parada diferente.

Prueba g(x)=x+1: nunca se estabiliza, aunque cada evaluación sea válida. Debe terminar por el límite y comunicar falta de resultado. Contrasta con g(x)=0, que revela el problema de dividir por la nueva aproximación.

Implementa una versión con historial y otra que solo devuelva el resultado. Explica qué estado es indispensable y qué datos solo sirven para observar. Una regla definida por repetición no obliga a usar recursividad.

[Volver al índice](README.md).
