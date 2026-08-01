# Laboratorio 6 — Del servidor PostgreSQL a una figura reproducible

## Pregunta

¿Puede construirse un análisis verificable cuyo origen sea una base PostgreSQL y
que se ejecute de la misma manera dentro de un contenedor?

## IA

Nivel 2. Puede utilizarse para crítica o generación de casos de prueba después de
una primera implementación propia. Debe entregarse `AI_USAGE.md`.

## Tareas

1. Iniciar la infraestructura suministrada.
2. Formular una pregunta que requiera al menos un `JOIN` y una agregación.
3. Probar primero la consulta en `psql`.
4. Ejecutar una consulta parametrizada desde Python.
5. Validar número de filas, unidades y un resultado calculable manualmente.
6. Construir una figura o tabla científica derivada del resultado.
7. Ejecutar el cliente dentro del contenedor de análisis.
8. Explicar por qué `localhost` cambia de significado dentro del contenedor.
9. Registrar la consulta, dependencias, comandos y asistencia de IA.

## Extensión remota

Si el docente suministra una cuenta temporal de lectura, cambiar únicamente
`DATABASE_URL` y verificar la misma consulta sobre el servicio remoto con TLS.

## Criterios de aceptación

- Ninguna credencial aparece en Git.
- La consulta usa parámetros para valores externos.
- SQL realiza filtrado, combinación o agregación que no conviene trasladar en
  bruto a Python.
- La imagen se construye desde el Dockerfile suministrado o uno justificado.
- Se distingue persistencia del volumen y ciclo de vida del contenedor.
- Existe al menos una prueba independiente del resultado de la consulta.

## Salida individual

Dibujar la arquitectura y responder oralmente una modificación de la consulta
elegida por el docente.

