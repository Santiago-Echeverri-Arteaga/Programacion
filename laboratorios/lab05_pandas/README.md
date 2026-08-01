# Laboratorio 5 — Datos de enfriamiento imperfectos

## Pregunta

¿Qué puede concluirse sobre el enfriamiento de dos zonas de una placa después de
documentar y tratar problemas de calidad de los datos?

## IA

Nivel 1. Esta actividad ocurre antes de la clase formal de IA.

## Datos

`datos/enfriamiento_sintetico_sucio.csv` contiene intencionalmente:

- una fila duplicada;
- una medición faltante;
- unidades mezcladas;
- un valor físicamente sospechoso;
- etiquetas de calidad que no deben ignorarse.

## Tareas

1. Cargar sin modificar el archivo original.
2. Inspeccionar tipos, nulos, duplicados, categorías y rangos.
3. Convertir temperaturas a una unidad común conservando la columna original.
4. Definir y justificar reglas de exclusión o marcado.
5. Crear una tabla limpia reproducible.
6. Comparar sensores mediante resúmenes y una figura con incertidumbre.
7. Registrar cuántas filas cambian en cada etapa.
8. Redactar una conclusión que no exceda la evidencia disponible.

## Criterios de aceptación

- No se eliminan filas silenciosamente.
- Una fila sospechosa no se transforma automáticamente en descartada.
- La procedencia y las unidades permanecen rastreables.
- El notebook puede ejecutarse de principio a fin con kernel reiniciado.

## Salida individual

Se presenta una regla de limpieza propuesta por otra persona. El estudiante debe
identificar un posible sesgo e indicar qué evidencia necesitaría para aceptarla.

