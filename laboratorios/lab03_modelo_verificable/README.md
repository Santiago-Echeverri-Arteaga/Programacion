# Laboratorio 3 — Péndulo modular y verificable

## Pregunta

¿En qué condiciones la aproximación de ángulo pequeño describe adecuadamente un
péndulo simulado?

## IA

Nivel 1. El trabajo se realiza con documentación y discusión en pareja.

## Tareas

1. Representar parámetros y estado sin usar variables globales.
2. Implementar un paso de Euler-Cromer para el péndulo no lineal.
3. Separar el modelo físico del algoritmo que recorre el tiempo.
4. Validar el límite de ángulo pequeño frente al periodo analítico.
5. Comparar al menos tres amplitudes iniciales.
6. Probar entradas inválidas y una propiedad física del sistema.
7. Justificar si una clase mejora el diseño o si bastan funciones y estructuras de
   datos simples.

## Validaciones obligatorias

- Dimensiones y signos de la aceleración angular.
- Periodo cercano a `2*pi*sqrt(longitud/gravedad)` para amplitud pequeña.
- Estudio de sensibilidad al paso temporal.
- Energía aproximadamente conservada en el caso sin amortiguamiento, indicando
  la tolerancia observada.

## Criterio de diseño

No se otorgan puntos por crear jerarquías de herencia. Se evalúa que cada
abstracción tenga una responsabilidad clara y facilite las pruebas.

## Salida individual

Predecir el efecto de duplicar la longitud y explicar una prueba que detectaría un
signo incorrecto en la ecuación.

