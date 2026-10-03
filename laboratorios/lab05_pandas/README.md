# Laboratorio 5 — Datos de enfriamiento imperfectos

| Campo | Especificación |
|---|---|
| Inicio | Jueves 29 de octubre de 2026 |
| Entrega | Martes 10 de noviembre de 2026 |
| Modalidad | Inicio acompañado y continuación autónoma |
| Dedicación por estudiante | 75 minutos acompañados + 3–4 horas autónomas; incluye informe y video |
| Trabajo | Parejas con evidencia individual |
| Herramientas | Pandas, NumPy y Matplotlib |

## Teoría breve

La ley de enfriamiento de Newton relaciona la rapidez de cambio de temperatura
con la diferencia respecto al ambiente, bajo supuestos que deben declararse.
Antes de comparar zonas, una tabla se revisa por tipos, faltantes, duplicados,
rangos, unidades y categorías. Limpiar no significa borrar todo lo inusual: cada
acción debe quedar justificada y los datos crudos deben permanecer intactos.

## Objetivos

- auditar un conjunto tabular imperfecto;
- definir y aplicar reglas de transformación basadas en evidencia;
- conservar unidades, procedencia y conteos antes y después;
- comparar dos zonas sin exceder lo que permiten los datos;
- comunicar cómo una decisión de limpieza afecta la conclusión.

## Requerimientos y límites

- usar [enfriamiento_sintetico_sucio.csv](../../datos/enfriamiento_sintetico_sucio.csv) sin sobrescribirlo;
- emplear Pandas, NumPy y Matplotlib con operaciones ya vistas;
- crear el análisis desde cero, sin notebook o código inicial;
- no exigir `groupby`, uniones, ajustes de curvas ni SciPy;
- no eliminar silenciosamente filas, faltantes o valores sospechosos.

## Procedimiento

1. Documenten columnas, unidades, categorías y procedencia. Formulen una
   predicción sobre las dos zonas.
2. Carguen el archivo y registren forma, tipos, nulos, duplicados, categorías y
   rangos antes de transformar.
3. Elaboren una lista de incidencias con fila, problema, evidencia y acción
   propuesta.
4. Unifiquen unidades conservando los valores y unidades originales. Distingan
   duplicado exacto de posible repetición experimental.
5. Definan un tratamiento explícito para faltantes y valores sospechosos.
   Implementen cada cambio de manera reproducible.
6. Registren cuántas filas se conservan, marcan, convierten o excluyen en cada
   etapa y validen el resultado.
7. Comparen las dos zonas con selecciones, resúmenes y una figura que muestre la
   dispersión o incertidumbre disponible.
8. Repitan el análisis con una regla alternativa razonable para la decisión más
   incierta y comparen la conclusión.
9. Reinicien el entorno y ejecuten todo de principio a fin siguiendo solo las
   instrucciones del equipo.

## Resultados puntuales que deben obtener

1. auditoría inicial con forma, tipos, nulos, duplicados, categorías y rangos;
2. registro de cada incidencia y la acción tomada;
3. conteo de filas en cada etapa del proceso;
4. tabla procesada que conserve trazabilidad hacia los datos originales;
5. resumen comparable de las dos zonas con unidades comunes;
6. figura final legible y exportada desde el análisis;
7. comparación de la conclusión bajo dos reglas de limpieza;
8. conclusión que distinga descripción de afirmación física.

La guía no indica qué filas deben descartarse ni entrega una secuencia de
celdas. La calidad de la decisión y su justificación forman parte del resultado.

## Explicación escrita y video

El texto debe separar datos crudos, decisiones, resultados e inferencias;
explicar si excluir el valor sospechoso puede introducir sesgo; identificar el
metadato que resolvería la decisión más incierta; y comparar las dos reglas de
limpieza.

El video de YouTube, de 3 a 5 minutos, debe mostrar la auditoría, una
transformación trazable, la figura y el cambio producido por una regla
alternativa. Puede ser no listado y no exige mostrar el rostro.

## Evidencia individual

Cada estudiante analiza una regla propuesta por otra persona, identifica un
sesgo posible y señala qué evidencia necesitaría para aceptarla.


## Entrega en GitHub

Deben **subir el código y el informe a GitHub**. Entregar URL del repositorio y commit evaluable. El README debe enlazar el informe Markdown o PDF e indicar comandos, dependencias y versiones para reproducirlo. Incluir datos permitidos o su fuente, resultados solicitados, evidencia de comprobaciones y enlace al video de 3–5 minutos. El informe responde las preguntas de esta guía, interpreta resultados y reconoce limitaciones; no es una colección de capturas. Cada integrante identifica su contribución. Si el repositorio es privado, habilitar acceso al docente antes de entregar.

Se aplica la [rúbrica común](../README.md). No subir `.venv`, cachés ni credenciales. Comprobar que código, informe y resultados son visibles en GitHub, no solo en el computador.


## Inicio y alcance prudente

Inicio el 29 oct., después de lectura y limpieza del 27–28: 15 min de pregunta y auditoría, 25 de reglas y trazabilidad, 25 de transformación y 10 de commit. Continuar con 60 min de limpieza, 45–60 de comparación, 45–60 de informe y 30–60 de video y ejecución limpia. Basta una figura comparativa y dos reglas para una sola incidencia incierta. Agrupación y uniones no son obligatorias; no se exige ajustar la ley de enfriamiento ni estimar parámetros.

IA nivel 1 hasta la práctica crítica del 4 nov.; después se permite nivel 2 únicamente para revisar trabajo propio, documentándolo en `AI_USAGE.md`. También es válido declarar que no se usó IA. Evidencia individual sin IA.
