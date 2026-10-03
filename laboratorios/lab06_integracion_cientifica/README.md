# Laboratorio 6 — Auditoría reproducible de un análisis científico

| Campo | Especificación |
|---|---|
| Inicio | Martes 3 de noviembre de 2026 |
| Entrega | Miércoles 11 de noviembre de 2026 |
| Dedicación por estudiante | 45 min acompañados + 1,5–2 h autónomas, incluido informe y video |
| Trabajo | Parejas con evidencia individual |
| Prerrequisitos | Archivos, funciones, pruebas, NumPy/Matplotlib y ejecución reproducible |

## Fundamento y objetivos

Un resultado es reproducible si otra persona puede reconstruirlo desde datos, código e instrucciones. Ejecutar sin errores no demuestra corrección física: hace falta una comprobación independiente. Esta actividad audita un trabajo previo, sin crear otro proyecto ni exigir bibliotecas nuevas.

## Problema y alcance

Elijan su laboratorio 3 o 4 ya entregado. Registren el commit original y conserven su historia. La evaluación corresponde a la nueva auditoría, no a calificar otra vez el mismo producto. Pueden trabajar en una nueva carpeta o rama del mismo repositorio. No exijan SQL, Docker, wheel, PyPI, nuevos datos ni una pregunta científica adicional.

## Procedimiento

1. Definan qué tabla o figura debe reproducirse y desde qué datos y parámetros.
2. Revisen README y dependencias. Un integrante sigue solo las instrucciones desde una copia limpia y un entorno nuevo; registren comando, versión de Python, salida y cualquier paso omitido.
3. Añadan una comprobación independiente que no estuviera en la entrega original: para puntos medios, un caso manual en otro intervalo; para caminata, una secuencia fija de pasos calculada a mano. No basta llamar dos veces a la misma función.
4. Introduzcan en una copia un defecto pequeño (signo, origen o límite), muestren que la comprobación falla y restáurenlo. No entregar código deliberadamente defectuoso como versión final.
5. Corrijan o documenten los problemas hallados y reproduzcan el resultado principal. Si el resultado cambia, cuantifiquen la diferencia y expliquen por qué; si no cambia, aporten evidencia.
6. Registren commit final, instrucciones completas y contribuciones individuales.

## Resultados y entrega en GitHub

Deben **subir el código y el informe a GitHub**, incluyendo la versión corregida, prueba nueva, datos necesarios, dependencias e instrucciones. Entregar URL y commits original/final; verificar que el acceso permita la revisión.

El informe breve (aproximadamente 1–2 páginas o Markdown equivalente) incluye: resultado auditado, protocolo de ejecución limpia, incidencias, comprobación independiente con valor esperado, defecto detectado, comparación antes/después y una limitación. Enlazar la tabla o figura reproducida y un video de 3–5 min que muestre ejecución, prueba y explicación de ambos integrantes. No repetir el informe completo del laboratorio original.

## Organización del tiempo

Inicio acompañado: 10 min de selección y predicción, 20 de ejecución limpia y 15 de diseño de comprobación. Trabajo autónomo: 30–40 min de prueba/corrección, 30–40 de informe y 30–40 de video y publicación. Puede terminarse antes del 10 nov. para liberar tiempo de estudio del parcial del 12.

## Evidencia individual y evaluación

Cada estudiante explica por qué su comprobación es independiente, predice el efecto del defecto y justifica una corrección. Se aplica la [rúbrica común](../README.md) a las evidencias nuevas. El peso sigue siendo 3,5 %.

IA nivel 2 solo después de la práctica del 4 nov., para crítica del trabajo propio con `AI_USAGE.md`; no es obligatoria. La evidencia individual es nivel 0. No se agregan requisitos al proyecto final.
