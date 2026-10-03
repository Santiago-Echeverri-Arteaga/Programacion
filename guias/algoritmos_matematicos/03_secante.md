# 3. Secante: recordar dos aproximaciones para producir la siguiente

Código de referencia: [secant.py](https://github.com/Santiago-Echeverri-Arteaga/Metodos_Numericos_Uniquindio/blob/a5c583075e984c3cc248afe5585200ca7cbfb5b9/examples/book_original/secant.py). Autor del original: Alex Gezerlis, *Numerical Methods in Physics with Python*, segunda edición, 2023. La explicación y los ejemplos pequeños son material didáctico elaborado para Programación.

## Qué problema resuelve

Se busca una raíz de f(x)=0. La secante usa dos evaluaciones para formar conceptualmente una recta y proponer dónde corta el eje horizontal. Con f(x)=x²−2 se vuelve a buscar √2.

La fórmula se entrega como regla: no es necesario deducir la ecuación de la recta.

## Regla matemática aceptada

```text
siguiente = actual - f(actual) * (actual-anterior) / (f(actual)-f(anterior))
```

Puede aproximar una raíz cuando el problema y los valores elegidos son adecuados. No garantiza mantener una raíz encerrada ni funcionar para cualquier pareja.

## Contrato y estado

Entradas: f, dos valores iniciales, tolerancia absoluta positiva y máximo entero positivo de pasos. Las evaluaciones deben estar definidas. Si el denominador se hace cero, no puede calcularse el paso y se informa mediante `ValueError`.

Estado: dos valores y sus evaluaciones. Salida: aproximación o `None` por agotamiento. En esta guía se acepta una raíz exacta o un cambio absoluto menor que la tolerancia; el residuo se comprueba después para interpretar el resultado.

## Un paso completo

Para anterior=1, actual=2 y f(x)=x²−2:

- f(anterior)=−1 y f(actual)=2; su diferencia es 3.
- siguiente = 2 − 2·(2−1)/3 = 4/3.
- Para el próximo paso la pareja es (2,4/3), no (1,4/3).

Después se obtiene 1,4 y luego aproximadamente 1,4146341463. Las aproximaciones no tienen que moverse siempre en la misma dirección.

## Pseudocódigo

```text
validar tolerancia y máximo de pasos
si alguno de los valores iniciales es raíz: devolverlo
repetir como máximo max_iter veces:
    evaluar f en anterior y actual
    denominador = f(actual) - f(anterior)
    si denominador es cero: lanzar ValueError
    siguiente = actual - f(actual) * (actual-anterior) / denominador
    si f(siguiente) es cero o abs(siguiente-actual) <= tolerancia:
        devolver siguiente
    actualizar simultáneamente (anterior, actual) a (actual, siguiente)
devolver None
```

La actualización simultánea conserva los valores del lado derecho antes de reemplazarlos. Si guardas evaluaciones para evitar llamadas repetidas, deben corresponder a la nueva pareja.

## Lectura del archivo

Importa f desde `bisection.py`; ese archivo debe estar disponible para importar, incluso si después llamas a `secant` con otra función. La f del ejemplo es `exp(x-sqrt(x))-x`.

`f0` guarda f(x0), `f1` evalúa f(x1), `ratio` reúne la división de diferencias y `x2` es la propuesta. Calcula `xdiff`, desplaza x0 y x1 y conserva f1 como el nuevo f0. Imprime paso, aproximación, cambio absoluto y residuo.

La parada original divide el cambio por x2. No comprueba previamente el denominador nulo de la fórmula ni x2=0 en la parada. La validación y la comparación absoluta del pseudocódigo son adaptaciones didácticas.

## Comprobaciones

Con x²−2 e iniciales 1 y 2, el original devuelve aproximadamente 1,4142135623730954. Registra las primeras tres parejas de tu implementación y contrástalas con el recorrido anterior.

Para f(x)=x²+1 e iniciales −1 y 1, ambas evaluaciones son iguales: el paso no existe. Para f(x)=x e iniciales −1 y 1, el siguiente es cero y debe reconocerse como raíz antes de una división relativa.

Explica por qué valores iniciales distintos no garantizan un denominador distinto de cero. Propón qué comunicar si la siguiente evaluación sale del dominio; no confundas ese fallo con agotar el número de pasos.

[Volver al índice](README.md).
