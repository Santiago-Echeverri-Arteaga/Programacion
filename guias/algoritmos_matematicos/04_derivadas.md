# 4. Derivar mediante evaluaciones: convertir una fórmula en llamadas

Código de referencia: [finitediff.py](https://github.com/Santiago-Echeverri-Arteaga/Metodos_Numericos_Uniquindio/blob/a5c583075e984c3cc248afe5585200ca7cbfb5b9/examples/book_original/finitediff.py). Autor del original: Alex Gezerlis, *Numerical Methods in Physics with Python*, segunda edición, 2023. La explicación y los ejemplos pequeños son material didáctico elaborado para Programación.

## Para qué sirve

La derivada describe el ritmo de cambio de una función. Si x(t) es una posición, su derivada describe velocidad. Cuando podemos evaluar una función pero no usamos su derivada simbólica, se pueden combinar evaluaciones cercanas.

La tarea consiste en llamar a la función en los puntos correctos, conservar los paréntesis y comparar resultados.

## Dos reglas aceptadas

Para h positivo:

```text
adelantada = (f(x+h) - f(x)) / h
centrada   = (f(x+h/2) - f(x-h/2)) / h
```

Estiman f′(x) para pasos adecuados y funciones suficientemente regulares alrededor de x. En la segunda, los puntos están separados por h: por eso se divide por h. Otra convención usa x+h y x−h y divide por 2h; mezclar las convenciones altera el resultado.

## Contrato

Cada función recibe f, el punto x y h>0; devuelve un número. f debe estar definida en los puntos pedidos. No hay ciclo dentro de cada fórmula: el ciclo se necesita al repetir para varios pasos h.

## Ejemplo comprobable

Para f(x)=x² y x=3, la derivada conocida es 6. Con h=0,2:

| Regla | Evaluaciones | Diferencia | Cociente |
|---|---|---|---|
| Adelantada | f(3,2)=10,24; f(3)=9 | 1,24 | 6,2 |
| Centrada | f(3,1)=9,61; f(2,9)=8,41 | 1,20 | 6 |

La regla centrada coincide en este polinomio en aritmética exacta, no en cualquier función. En Python pueden diferir las últimas cifras.

## Estructura del experimento

```text
para cada h elegido:
    comprobar que h es positivo
    calcular aproximación adelantada
    calcular aproximación centrada
    calcular distancia absoluta de cada aproximación a la referencia
    guardar o mostrar h y las dos distancias
```

Una función para cada fórmula permite cambiar de problema sin modificar el experimento. La referencia se usa para comprobar, no para producir la aproximación.

## Correspondencia con el original

`calc_fd` implementa la adelantada; `calc_cd` la centrada con desplazamientos de h/2. El archivo define f(x)=exp(sin(2x)) y `fprime` proporciona su derivada de referencia. Puedes aceptar esa referencia sin deducirla aquí.

El programa principal fija x=0,5. `hs` contiene potencias decrecientes de diez. `fds` y `cds` guardan diferencias absolutas respecto a la referencia: **esas listas contienen errores absolutos del experimento, no las derivadas aproximadas**. `zip` empareja valores para imprimir filas.

Las comprensiones pueden reescribirse como ciclos con `append`. El formato de impresión afecta la presentación, no la fórmula.

## Qué implementar y observar

Escribe ambas funciones con argumentos y `return`, rechazando h<=0. Prueba x² en x=3 para h=0,2 y h=0,1: la adelantada da aproximadamente 6,2 y 6,1; la centrada queda cerca de 6 en ambos casos.

Con una función constante ambas diferencias deben ser cero. Explica por qué devolver siempre 6 superaría el primer ejemplo pero no implementaría el algoritmo. Identifica el fallo en `f(x+h) - f(x)/h` sin agrupar la resta.

El original explora h mucho menores. Restar números casi iguales en precisión finita puede perder información: reducir h indefinidamente no siempre mejora el resultado. Reconocer esa observación basta; su análisis formal pertenece a Métodos Numéricos.

[Volver al índice](README.md).
