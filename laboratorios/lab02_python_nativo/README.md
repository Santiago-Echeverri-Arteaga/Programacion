# Laboratorio 2 — Caída libre con Python nativo

| Campo | Especificación |
|---|---|
| Fecha de realización/entrega | Martes 29 de septiembre de 2026 |
| Modalidad | Tarea; no reemplaza la clase regular de ese día |
| Tiempo estimado | 120 minutos |
| Trabajo | Parejas con evidencia individual |
| Herramientas | Python 3.12 y biblioteca estándar |

## Teoría breve

Para movimiento vertical con aceleración constante y velocidad inicial nula,
`h(t)=h₀-g t²/2`. Para `t>0`, cada observación permite estimar
`gᵢ=2(h₀-hᵢ)/tᵢ²`. Los tiempos muy pequeños amplifican las perturbaciones.
Una media resume valores, pero no basta para validar el modelo: también se deben
revisar unidades, orden temporal, datos inválidos y sensibilidad.

## Objetivos

- leer y validar un CSV con la biblioteca estándar;
- separar lectura, validación, cálculo y presentación en funciones propias;
- estimar y resumir `g` con unidades;
- comprobar el programa con casos normales, de frontera e inválidos;
- explicar el alcance físico del resultado.

## Requerimientos y límites

- usar `datos/caida_libre_sintetica.csv` y conservarlo sin cambios;
- emplear `csv`, `pathlib`, `statistics` y `math` según se necesiten;
- crear todo el código desde cero; no se suministra esqueleto ni nombres de
  funciones obligatorios;
- no usar NumPy, Pandas, SciPy, `pytest` ni IA generativa;
- no ocultar errores mediante `except Exception` sin tratamiento específico.

## Procedimiento

1. Lean el encabezado y documenten columnas, unidades y significado físico.
2. Diseñen antes de programar cómo separarán lectura, validación, cálculo,
   resumen y escritura de resultados.
3. Lean el CSV y conviertan sus campos a tipos numéricos. Un dato inválido debe
   producir un mensaje que permita localizar la fila.
4. Validen archivo no vacío, columnas necesarias, tiempos estrictamente
   crecientes y valores compatibles con el diccionario de datos.
5. Calculen `gᵢ` solo para tiempos positivos y conserven cada estimación.
6. Obtengan media, desviación y rango. Comparen con el valor de referencia y
   definan qué significa «compatible» para el equipo.
7. Comprueben como mínimo un caso calculable a mano, un archivo vacío, una fila
   inválida, tiempos no crecientes y el límite `t=0`. Pueden usar llamadas y
   `assert` sencillos.
8. Ejecuten el programa desde dos ubicaciones distintas para revisar el manejo de
   rutas y registren cualquier corrección necesaria.

## Resultados puntuales que deben obtener

1. número de filas leídas, aceptadas y rechazadas;
2. tabla con `t`, `h` y cada `gᵢ`, incluyendo unidades;
3. media, desviación, mínimo y máximo de las estimaciones válidas;
4. diferencia absoluta y relativa frente al valor de referencia;
5. resultado visible de los cinco casos de comprobación;
6. conclusión explícita sobre compatibilidad y al menos una limitación.

Los valores numéricos no se anticipan en la guía. El equipo debe obtenerlos,
verificarlos y decidir una presentación comprensible.

## Explicación escrita y video

El texto debe explicar la ecuación y sus supuestos, la organización elegida para
el programa, el criterio de compatibilidad, por qué los tiempos iniciales son más
inestables y qué validación protege la conclusión física.

El video de YouTube, de 3 a 5 minutos, debe ejecutar el programa, mostrar la tabla
o resumen principal, demostrar un caso inválido y explicar una decisión del
diseño. Puede ser no listado y no exige mostrar el rostro.

## Evidencia individual

Cada estudiante escribe una función corta de validación, propone dos casos límite
y explica la diferencia entre `return` y `print` en este análisis.
