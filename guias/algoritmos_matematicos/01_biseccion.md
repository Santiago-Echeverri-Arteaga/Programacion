# 1. Bisección: reducir una búsqueda conservando una condición

Código de referencia: [bisection.py](https://github.com/Santiago-Echeverri-Arteaga/Metodos_Numericos_Uniquindio/blob/a5c583075e984c3cc248afe5585200ca7cbfb5b9/examples/book_original/bisection.py). Autor del original: Alex Gezerlis, *Numerical Methods in Physics with Python*, segunda edición, 2023. La explicación y los ejemplos pequeños son material didáctico elaborado para Programación.

## Qué problema resuelve

Encontrar una raíz significa hallar r tal que f(r)=0. Para calcular √2 puedes buscar un cero de `f(x)=x**2-2`. f(1) es negativo y f(2) positivo: la solución positiva está entre esos números.

En física, la misma estructura aparece al buscar un instante en que una posición alcanza cierto valor o una temperatura coincide con una meta. Cambia la función; puede conservarse la búsqueda.

## Regla matemática que aceptamos

Si f es continua en [a,b] y tiene signos opuestos en los extremos, hay al menos una raíz dentro. Calculamos m=(a+b)/2. Si f(m)=0, ya la encontramos. En otro caso conservamos la mitad cuyos extremos siguen teniendo signos opuestos.

No debes demostrar aquí esa afirmación, sino programar la selección de la mitad. Dos valores del mismo signo no permiten aplicar esta regla, aunque pudiera haber raíces en el intervalo. El programa comprueba signos; no puede certificar continuidad evaluando solo unos puntos.

## Contrato y estado

Entradas: f, extremos a<b, tolerancia absoluta positiva y máximo entero positivo de iteraciones. Si un extremo ya es raíz, se devuelve. En otro caso se exige cambio de signo.

Estado: extremos actuales y, si se almacena, f(a). Salida: punto aproximado, o `None` si se agota el máximo sin satisfacer la parada. La tolerancia de esta guía significa ancho máximo aceptado del intervalo, no exactitud de la raíz.

## Traza manual

Para f(x)=x²−2:

| Paso | a antes | b antes | Punto medio | f(punto medio) | Intervalo que queda |
|---|---:|---:|---:|---:|---|
| 1 | 1 | 2 | 1,5 | 0,25 | [1; 1,5] |
| 2 | 1 | 1,5 | 1,25 | −0,4375 | [1,25; 1,5] |
| 3 | 1,25 | 1,5 | 1,375 | −0,109375 | [1,375; 1,5] |

La propiedad conservada es el cambio de signo entre extremos, salvo que ya se encuentre una raíz exacta. A una propiedad conservada durante el ciclo se le llama invariante.

## Traducción a operaciones

```text
validar extremos, tolerancia y máximo de iteraciones
si f(a) es cero: devolver a
si f(b) es cero: devolver b
si los signos no son opuestos: rechazar la entrada
repetir como máximo max_iter veces:
    m = (a + b) / 2
    si f(m) es cero o b-a <= tolerancia: devolver m
    si f(a) y f(m) tienen signos opuestos:
        b = m
    en otro caso:
        a = m
devolver None
```

Si guardas f(a), actualízala cuando cambies a. No debes comparar una evaluación de un extremo antiguo con el nuevo punto medio.

## Qué hace el original

| Elemento | Función en el programa |
|---|---|
| `f` | Define `exp(x-sqrt(x))-x`; exige x no negativo en números reales |
| `bisection(f,x0,x1,...)` | Recibe función y extremos, por lo que admite otra f |
| `f0` | Recuerda la evaluación del extremo izquierdo |
| `x2` | Punto medio antes de reducir el intervalo |
| `x2new` | Punto medio del intervalo reducido, que se imprime y devuelve |
| `xdiff` | Cambio entre ambos puntos medios |
| `for…else` | Establece `None` si el ciclo termina sin `break` |

El archivo hace dos búsquedas sobre su propia f. Las filas muestran iteración, aproximación, cambio y residuo `abs(f(aproximación))`; imprimir no es la búsqueda.

El original usa **cambio relativo de puntos medios** para parar; el pseudocódigo usa ancho absoluto del intervalo. Son decisiones diferentes. `range(1,kmax)` permite como máximo kmax−1 pasos.

## Casos para revisar código

El original no comprueba el cambio de signo inicial ni detecta expresamente una raíz exacta en el punto medio. Con `f(x)=x-1` y extremos 0 y 2, el primer punto medio ya es raíz, pero el código continúa y puede acercarse a 2. La condición matemática debe convertirse en una decisión explícita.

Su cociente de parada también divide por `x2new`, que podría ser cero. La parada absoluta usada aquí evita ese denominador; es una adaptación didáctica, no una descripción literal del archivo.

## Qué implementar y comprobar

Implementa el pseudocódigo como función con retorno y deja la impresión fuera. Comprueba x²−2 en [1,2], x−1 en [0,2], una raíz en un extremo y una entrada sin cambio de signo. Con x²−2, el original devuelve aproximadamente 1,4142135605 con sus parámetros por defecto.

Explica qué pasaría si actualizaras a sin cambiar el valor guardado de f(a). Justifica por qué un intervalo pequeño aporta información distinta de un residuo pequeño.

[Volver al índice](README.md).
