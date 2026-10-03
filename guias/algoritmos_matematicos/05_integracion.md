# 5. Integración: posiciones, pesos y acumuladores

Código de referencia: [newtoncotes.py](https://github.com/Santiago-Echeverri-Arteaga/Metodos_Numericos_Uniquindio/blob/a5c583075e984c3cc248afe5585200ca7cbfb5b9/examples/book_original/newtoncotes.py). Autor del original: Alex Gezerlis, *Numerical Methods in Physics with Python*, segunda edición, 2023. La explicación y los ejemplos pequeños son material didáctico elaborado para Programación.

## Qué problema resuelve

Una integral acumula contribuciones: área con signo, desplazamiento a partir de velocidad o energía a partir de potencia. Se aproxima evaluando una función en posiciones elegidas, multiplicando por pesos y sumando.

En clase apareció puntos medios. Este archivo reúne rectángulos izquierdos, trapecios y Simpson. Aceptamos las reglas y nos concentramos en construir posiciones, contar correctamente y acumular.

## Primero decide qué significa n

En el original **n cuenta puntos**, no intervalos. Hay n−1 intervalos y `h=(b-a)/(n-1)`. En puntos medios de clase n contaba intervalos. Trasladar una fórmula sin revisar sus parámetros es un error de programación.

Entradas: f, a<b y n entero. Rectángulos y trapecios requieren n>=2. Simpson requiere n>=3 e impar, porque n−1 debe ser par. Una implementación de estudiante debe validarlo; el original no comprueba todas estas condiciones.

## Reglas proporcionadas

Sea x_i=a+i·h:

| Método | Puntos usados | Pesos | Resultado |
|---|---|---|---|
| Rectángulos izquierdos | i=0,…,n−2 | Todos 1 | h por la suma de f(x_i) |
| Trapecios | i=0,…,n−1 | 1/2 en extremos; 1 en interiores | h por la suma ponderada |
| Simpson | i=0,…,n−1 | 1 en extremos; 4 en interiores impares; 2 en interiores pares | h/3 por la suma ponderada |

«Par» e «impar» describen el **índice**, no x. Los extremos tienen prioridad sobre la paridad.

## Traza pequeña

Para f(x)=x², a=0, b=2 y n=5, h=0,5:

| i | x_i | f(x_i) | Peso trapecios | Peso Simpson |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0,5 | 1 |
| 1 | 0,5 | 0,25 | 1 | 4 |
| 2 | 1 | 1 | 1 | 2 |
| 3 | 1,5 | 2,25 | 1 | 4 |
| 4 | 2 | 4 | 0,5 | 1 |

Rectángulos usa solo las primeras cuatro filas. Resultados: 1,75 para rectángulos, 2,75 para trapecios y 8/3 para Simpson. La integral exacta es 8/3; la coincidencia de Simpson no demuestra exactitud para cualquier función.

## Un algoritmo con acumulación: trapecios

```text
validar a, b y n
h = (b-a)/(n-1)
suma = 0
para i desde 0 hasta n-1:
    x = a + i*h
    si i es el primero o el último: peso = 0.5
    en otro caso: peso = 1
    suma = suma + peso*f(x)
devolver h*suma
```

Puedes usar un `for`, sin NumPy. Para Simpson cambia pesos, valida la paridad y cambia el factor final; no basta reemplazar el nombre.

## Qué expresan los arreglos del original

| Expresión o variable | Equivalente conceptual con Python básico |
|---|---|
| `np.arange(n)` | Índices 0,…,n−1, como `range(n)` |
| `xs` | Colección de posiciones donde evaluar f |
| `np.ones(n)` | n pesos iniciales iguales a 1 |
| `cs[1::2]` | Posiciones de índice impar de los pesos |
| `cs*f(xs)` | Cada evaluación multiplicada por su peso |
| `np.sum(contribs)` | Acumulación de contribuciones |

La multiplicación elemento a elemento es de arreglos: dos listas normales no se multiplican así. El original espera que f acepte un arreglo; la versión con ciclos le entrega un número cada vez. Por eso su f usa NumPy.

El ejemplo integra `1/sqrt(1+x²)` entre 0 y 1 con 51 puntos y compara con `log(1+sqrt(2))`. La referencia se proporciona; no debes deducirla para escribir el acumulador.

## Comprobaciones

Implementa trapecios con ciclos y después otra regla de la tabla. Una función constante debe dar constante·(b−a) con cualquiera de las reglas y parámetros válidos. Usa x² para revisar índices y pesos.

Explica qué ocurre si recorres n puntos en rectángulos izquierdos o reinicias la suma dentro del ciclo. Rechaza n=1 antes de dividir. En Simpson, explica por qué comprobar únicamente n>1 no basta.

[Volver al índice](README.md).
