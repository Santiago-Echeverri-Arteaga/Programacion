# 7. Recurrencia: calcular el siguiente resultado a partir del anterior

Código de referencia: [recforw.py](https://github.com/Santiago-Echeverri-Arteaga/Metodos_Numericos_Uniquindio/blob/a5c583075e984c3cc248afe5585200ca7cbfb5b9/examples/book_original/recforw.py). Autor del original: Alex Gezerlis, *Numerical Methods in Physics with Python*, segunda edición, 2023. La explicación y los ejemplos pequeños son material didáctico elaborado para Programación.

## Qué se intenta calcular

El programa genera aproximaciones de una familia de integrales:

```text
I_n = integral entre 0 y 1 de x**n * exp(-x)
```

En vez de integrar desde cero para cada n, usa una relación entre integrales consecutivas. Se entrega la relación y su valor inicial, sin exigir deducirlos:

```text
I_0 = 1 - exp(-1)
I_n = n * I_(n-1) - exp(-1), para n >= 1
```

Muestra cómo una relación matemática se transforma en una actualización corta. También permite observar que una fórmula válida no garantiza una evaluación numérica fiable indefinidamente.

## Recurrencia y programación

Una recurrencia expresa un valor usando anteriores. No obliga a escribir una función que se llame a sí misma: aquí basta un ciclo y una variable que recuerde la integral anterior.

Entrada: cantidad entera positiva de términos. Salida propuesta: lista de pares (n,I_n), desde 0 hasta cantidad−1.

## Traza

Con `exp(-1)` aproximadamente 0,3678794412:

| Índice | Operación | Valor aproximado |
|---:|---|---:|
| 0 | 1−exp(−1) | 0,6321205588 |
| 1 | 1·I_0−exp(−1) | 0,2642411177 |
| 2 | 2·I_1−exp(−1) | 0,1606027941 |
| 3 | 3·I_2−exp(−1) | 0,1139289413 |

El índice de la multiplicación corresponde al valor que se calcula. Usar siempre 1 o el índice anterior cambiaría la recurrencia.

## Pseudocódigo con retorno

```text
validar que cantidad sea un entero positivo
anterior = 1 - exp(-1)
resultados = [(0, anterior)]
para n desde 1 hasta cantidad-1:
    nuevo = n*anterior - exp(-1)
    agregar (n, nuevo) a resultados
    anterior = nuevo
devolver resultados
```

Un número basta para continuar; la lista permite entregar todos los valores. Si solo se pidiera el último, podría omitirse.

## Qué hace el original

`forward` inicializa `oldint`. En cada iteración imprime n−1 y el valor anterior, calcula `newint` y lo guarda para la siguiente vuelta. No devuelve una colección: su retorno implícito es `None`.

Con `nmax=22`, el ciclo recorre n=1,…,21: imprime índices 0,…,20 y calcula I_21 sin imprimirlo. La versión didáctica define la entrada como **cantidad de términos devueltos**, por lo que no conserva exactamente la semántica de impresión original.

Las demostraciones se ejecutan al importar porque no están protegidas por `if __name__ == "__main__":`. Esto permite repasar función reutilizable frente a demostración.

## Una comprobación accesible

La función integrada es positiva en el interior de [0,1], así que I_n debe ser positivo. Allí `x**(n+1) <= x**n`: los valores de esta familia deben disminuir al aumentar n.

Si el cálculo produce negativos o empieza a crecer, no basta decir «Python ejecutó el ciclo». La recurrencia multiplica por n el error que ya contenía el anterior, lo que ayuda a entender por qué se deteriora al avanzar.

El original incluye como referencia para n=20 el número 0,0183504676972562. Esa constante se usa para comparar, no para actualizar. No debes forzar los resultados a ser positivos para ocultar discrepancias. El análisis formal de estabilidad se estudiará después.

## Qué implementar y explicar

Escribe una función que devuelva cuatro términos y contrasta la tabla. Añade una demostración fuera de la función que imprima los pares. Explica qué cambia si actualizas `anterior` antes de agregar el término, según cuál variable agregues.

Distingue recurrencia matemática, recursividad de funciones y ciclo iterativo. Indica una propiedad comprobable automáticamente y una afirmación que esa comprobación no demuestra por sí sola.

[Volver al índice](README.md).
