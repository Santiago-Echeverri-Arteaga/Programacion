# Laboratorio 4 — Análisis de enfriamiento y auditoría reproducible con Pandas

Analicen datos de enfriamiento con Pandas, documenten las decisiones de limpieza y comparen dos zonas. Verifiquen la trazabilidad de las transformaciones y la reproducibilidad del análisis mediante una auditoría.

| Campo | Especificación |
|---|---|
| Inicio | Jueves 5 de noviembre de 2026 |
| Entrega | Jueves 19 de noviembre de 2026 |
| Dedicación por estudiante | 6–7 horas totales, incluidos 45 minutos acompañados |
| Trabajo | Máximo dos estudiantes; evidencia individual escrita |
| Herramientas | Pandas, NumPy, Matplotlib y pytest |
| Evaluación | Sin sustentación oral ni video; rúbrica de evaluación |

## Pregunta y fundamento

¿Cómo cambian la comparación de dos zonas y su credibilidad cuando se documentan las decisiones de limpieza y se comprueba el análisis de manera independiente?

La ley de enfriamiento de Newton relaciona la rapidez de cambio de temperatura con la diferencia respecto al ambiente bajo supuestos físicos. Aquí se realiza un análisis descriptivo; no se exige ajustar esa ley ni estimar parámetros. Dos sensores con temperaturas iniciales diferentes no bastan para atribuir diferencias a un mecanismo causal o comparar constantes de enfriamiento.

Usen [enfriamiento_sintetico_sucio.csv](../../datos/enfriamiento_sintetico_sucio.csv) y [sensores_enfriamiento.csv](../../datos/sensores_enfriamiento.csv). Son datos didácticos sintéticos, no mediciones reales. El segundo archivo aporta la correspondencia de sensores y zonas; no contiene calibraciones ni información para decidir automáticamente qué lectura es correcta.

## Reto 1. Auditoría y transformación trazable

1. Conserven los archivos crudos intactos. Asignen un identificador de fila original antes de ordenar, filtrar o eliminar duplicados.
2. Documenten columnas y unidades; inspeccionen forma, tipos, faltantes, duplicados exactos, claves repetidas, categorías y rangos. Elaboren una tabla de incidencias con identificador, evidencia, regla y acción.
3. Conviertan fechas a tipo temporal conservando la zona horaria y valores numéricos con un tratamiento explícito de fallos de conversión. Usen selección con `.loc`, máscaras y operaciones vectorizadas.
4. Conviertan temperaturas a °C sin destruir valor y unidad originales. Diferencien temperatura e incertidumbre: un cambio de origen entre K y °C afecta la temperatura, no el tamaño de su incertidumbre.
5. Establezcan reglas para duplicados, faltantes y valores sospechosos. No confundan etiqueta sospechosa con dato necesariamente inválido. No imputen ni descarten sin justificación.
6. Registren conteos por etapa, filas excluidas y motivos; guarden una tabla procesada trazable y un registro de exclusiones. Cada fila original debe tener un destino documentado. No sumen conteos de incidencias superpuestas como si fueran filas distintas.

## Reto 2. Pandas para resumir y combinar

1. Comprueben que la tabla de sensores tiene clave única y unan los metadatos mediante `merge`, validando una relación muchos-a-uno y verificando coincidencias. Comparen número de filas antes y después para detectar multiplicación accidental o pérdida de registros.
2. Ordenen temporalmente por sensor. Usen `groupby` y agregaciones para obtener por zona: cantidad de temperaturas válidas, media, desviación estándar, mínimo y máximo. Indiquen qué ocurre si solo queda una observación. Esta desviación describe variación temporal de la muestra, no incertidumbre instrumental ni incertidumbre de la media.
3. Construyan una tabla ancha tiempo × sensor con `pivot` o equivalente, resolviendo explícitamente claves repetidas antes del cambio de forma. Si agregan repeticiones, expliquen por qué sería válido.
4. Calculen la diferencia A−B únicamente en tiempos con ambas temperaturas válidas, sin rellenar huecos artificialmente. Indiquen cuántos pares pudieron compararse.
5. Exporten una figura temporal comparativa con unidades y leyenda. Distingan las incertidumbres instrumentales de cualquier dispersión estadística que presenten.
6. Para **una** decisión incierta, repitan el análisis bajo dos reglas defendibles. Comparen al menos un resumen numérico y expliquen si cambia la conclusión. No seleccionen la regla porque produce la figura «más bonita».

**Incluyan:** selección, tipos, fechas, limpieza, agrupación, unión validada y cambio de forma. **Eviten:** SQL, Docker, aprendizaje automático, ajuste de curvas, nuevas fuentes o un dashboard. Se permiten clases si aportan claridad; no son requisito.

## Reto 3. Auditoría del propio análisis

1. Identifiquen un commit inicial funcional y el resultado concreto que auditarán. Desde una copia y entorno limpios, ejecuten usando solo el README. En pareja, la otra persona realiza la reproducción; en trabajo individual, se documenta la misma comprobación en un entorno nuevo.
2. Escriban al menos **cinco comprobaciones automatizadas**: conversión de temperatura e incertidumbre contra un caso manual; unicidad de la clave de metadatos; unión sin multiplicación ni sensores sin correspondencia; trazabilidad y conteos; resumen o diferencia sobre una pequeña tabla de dos o tres filas calculada a mano. Pueden usar datos mínimos de prueba propios, separados de los datos del análisis.
3. En una copia temporal introduzcan **un** defecto (conversión incorrecta, clave duplicada o pérdida de una fila). Guarden la salida que demuestra que una comprobación falla y expliquen por qué. Restáurenlo y registren que la suite final pasa. No dejen defectos intencionales activos en la entrega.
4. Comparen el resultado auditado antes y después de las correcciones. Cuantifiquen el cambio, o documenten igualdad si no cambió. Registren commits inicial/final, comandos, versiones, incidencias y limitaciones.

## Entrega y preguntas del informe

Entreguen URL de GitHub y commit final. Incluyan datos crudos con procedencia, código, dependencias, pruebas, tablas derivadas, registro de incidencias/exclusiones, figura y un informe Markdown o PDF con una sección de auditoría. El README debe permitir reconstruir todo desde cero, sin rutas personales ni pasos manuales ocultos. Los resultados evaluables deben estar versionados y ser visibles aunque una regla general de `.gitignore` ignore datos generados.

Respondan en el informe:

1. ¿Qué diferencia hay entre duplicado exacto y repetición experimental? ¿Qué información falta para decidir?
2. ¿Qué decisiones podrían sesgar la comparación de zonas?
3. ¿Por qué validaron la cardinalidad de la unión? ¿Qué pasaría con un sensor duplicado en metadatos?
4. ¿Por qué solo compararon tiempos comunes y qué limita el número de observaciones?
5. ¿Cómo afectó la regla alternativa al resultado? ¿Qué metadato resolvería la duda?
6. ¿Qué hace independiente a la comprobación manual y qué defecto detectó?
7. ¿Qué conclusiones físicas no se pueden obtener de estos datos?

Cada integrante añade una nota propia sobre una decisión, su sesgo posible y la comprobación realizada. Sin video, sustentación ni examen oral adicional. IA nivel 2 únicamente como crítica de trabajo propio después de la práctica correspondiente, con `AI_USAGE.md`; también es válido declarar que no se usó IA. Evidencia individual nivel 0.

## Tiempo y evaluación

Auditoría inicial 45 min; limpieza trazable 75; agrupación/unión/cambio de forma 75; comparación y figura 45; pruebas y ejecución limpia 60; informe y revisión 60–120. Total 6–7 h, incluido el acompañamiento. Planifiquen el trabajo teniendo en cuenta el parcial del 12 de noviembre, la entrega del proyecto del 16 y la entrega de este laboratorio el 19. La entrega se evalúa según la [rúbrica de los laboratorios 3 y 4](../README.md#rúbrica-de-los-laboratorios-integrados-3-y-4).
