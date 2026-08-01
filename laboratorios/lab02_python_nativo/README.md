# Laboratorio 2 — Caída libre con Python nativo

## Pregunta

¿Son compatibles las posiciones suministradas con un movimiento de caída libre
desde el reposo?

## Restricciones

- Usar únicamente la biblioteca estándar.
- No usar NumPy, Pandas, SciPy ni IA generativa.
- Separar lectura, validación, cálculo y presentación.

## Tareas

1. Leer `datos/caida_libre_sintetica.csv` con el módulo `csv`.
2. Convertir cada fila a tipos numéricos y validar orden temporal, alturas e
   incertidumbres.
3. Para cada tiempo positivo, calcular
   `g_i = 2 * (altura_inicial - altura_i) / tiempo_i**2`.
4. Resumir los valores mediante media y dispersión usando funciones propias o
   `statistics`.
5. Identificar por qué los primeros tiempos pueden producir estimaciones más
   inestables.
6. Producir una salida textual con unidades y cifras razonables.
7. Diseñar al menos cuatro casos de prueba para funciones puras.

## Criterios de aceptación

- Un archivo vacío o una fila inválida produce un mensaje explicativo.
- No se usa `except Exception` para ocultar errores.
- El programa no depende del directorio desde el que se invoque.
- La conclusión distingue medición, modelo y estimación.

## Salida individual

Escribir en papel una función que rechace una serie con tiempos no crecientes y
explicar dos casos límite.

