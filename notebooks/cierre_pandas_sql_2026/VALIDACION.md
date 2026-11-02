# Validación del rediseño meteorológico

Ejecutada el **2 de noviembre de 2026**. Alcance: `notebooks/cierre_pandas_sql_2026/`.


## Revisión didáctica de scripts: menos parsing y ejemplos ejecutables

Se simplificaron los scripts tras el rediseño inicial. Se eliminaron argparse, el análisis de parámetros de URLs, expresiones regulares Bash, arrays Bash y trap. Se sustituyeron comprensiones/generadores y expresiones condicionales compactas del flujo por ciclos y if explícitos. La ingesta se organiza en cuatro funciones con una responsabilidad y realiza INSERT mediante un ciclo apropiado para la muestra pequeña. Bash exporta la configuración; las fechas del periodo ahora son campos explícitos del manifiesto. Los bytes de los seis JSON originales no cambiaron.

Se conservan las conversiones necesarias JSON/fechas, hashes, parámetros SQL, transacciones y reglas de integridad. Los programas de clase rechazan opciones antiguas en vez de ignorarlas silenciosamente; no interpretan sus valores. La guía y el notebook muestran la nueva configuración. Los comandos `bash ampliacion/pipeline.sh offline inicial` y `bash ampliacion/pipeline.sh offline actualizacion` se mantienen.

Se añadieron `ejemplos/01_archivos_y_json.py`, `02_conexion_y_transaccion.py`, `03_tablas_e_informe.py` y `04_bash_paso_a_paso.sh`, con comentarios, propósito, comandos y resultados esperados en `ejemplos/README.md`. Cubren rutas, bytes, JSON, ausencias, fechas, hashes, with, variables de entorno, cursores, parámetros, rollback, formato de informes y las funcionalidades Bash conservadas. Las utilidades tests son mantenimiento, no contenido que se deba implementar en clase.

**Pruebas ejecutadas sobre la revisión:**

- Clúster PostgreSQL temporal nuevo, socket aislado y base `test_meteo_sencillo`; detenido al terminar. Ninguna base personal modificada.
- Integración offline completa: 93 → 180 → 180, conservación de filas y procedencia, restricciones, rollback, cobertura con NULL/día ausente, Gold contra Pandas, psql, Psycopg, exportación y fallo sin marcador final.
- Validación de las seis respuestas con fechas explícitas; preservación de None y rechazo de unidades, longitudes, fechas y números no finitos incorrectos.
- Ambos notebooks ejecutados offline desde kernels limpios; sintaxis Python y Bash incluyendo los nuevos ejemplos.
- Los cuatro ejemplos ejecutados; el ejemplo PostgreSQL revierte su ensayo temporal.
- Actualización online real con los nuevos scripts: 180 registros conservados y seis resúmenes, sin duplicados.
- Tres ejecuciones con seis filas de Gold comparadas con el resultado anterior al cambio: **resumen_mensual.csv, informe.md y temperatura_mensual.png idénticos byte a byte**. No se exige identidad de los metadatos de ejecución (base, instante de carga) entre bases distintas.

Los registros de esta revisión están en las carpetas ignoradas salidas_pruebas (prefijo sencillo_) y salidas_pipeline. Versiones de dependencias iguales a las indicadas en este informe. También se corrigió la codificación del literal Bogotá en el ensayo de UNIQUE para que compruebe el nombre real del catálogo.

## Entorno utilizado

Ubuntu WSL2, Python 3.14.4, PostgreSQL 18.6, Psycopg 3.3.6, Pandas 3.1.0, NumPy 2.5.4, Matplotlib 3.11.2, nbformat 5.11.1, nbclient 0.11.0 e ipykernel 7.4.0.

El rol del servidor personal no tenía permiso para crear bases y sudo requería autenticación. Se utilizaron los binarios ya instalados para crear **un clúster temporal independiente**, con socket privado, autenticación peer y sin escucha TCP. Se crearon `test_meteo_integral` y `test_meteo_online` dentro de ese clúster. Se detuvo al terminar; no se borraron ni modificaron bases personales, roles o autenticación del servidor existente. Las dependencias de prueba se instalaron en un entorno virtual temporal Ubuntu.

## Pruebas realmente ejecutadas

| Verificación | Resultado observado |
|---|---|
| JSON de notebooks y validación nbformat | Ambos válidos |
| Sintaxis de todas las celdas Python, scripts y pruebas | Correcta mediante AST |
| Sintaxis Bash | `bash -n` correcto en ambos scripts |
| Ejecución de notebooks | Ambos desde kernel limpio con conexiones de red bloqueadas; sin errores |
| Datos offline | Seis respuestas JSON, hashes SHA-256 coincidentes con manifiesto |
| Pipeline offline inicial | 93 recibidas, 93 nuevas; Bronze/Silver=93, Gold=3 |
| Pipeline offline actualización | 108 recibidas, 87 nuevas; Bronze/Silver=180, Gold=6 |
| Repetición de actualización | 108 recibidas, 0 nuevas; conteos permanecen 180/6 |
| Preservación | Filas previas Silver y Bronze, incluidas procedencia/fecha de carga, sin cambios |
| Duplicados | Ninguna clave ciudad–fecha repetida |
| Copia Pandas | Las 180 filas SQL coinciden con el CSV derivado |
| Gold frente a Pandas | Conteos, medias y acumulados coinciden numéricamente; cobertura=1 |
| NULL permitido | Se admite ausencia de temperatura/precipitación; Gold reduce conteos y no publica acumulado incompleto |
| Día totalmente ausente | Gold mantiene denominador 31 y acumulado NULL para enero incompleto |
| Restricciones | Rechazadas precipitación negativa, mínima>máxima, NaN, fecha NULL, ciudad inexistente, PK duplicada y nombre UNIQUE repetido |
| Atomicidad | Fila artificial inválida de prueba revierte también Bronze; no permanece en la base |
| SQL docente | `sql/01_consultas_clase.sql` completo ejecutado con psql y ON_ERROR_STOP |
| Consulta Python | `consulta_local.py` ejecutado con Psycopg |
| Exportación | `ejecutar_resumen.sh` produce CSV final |
| Rutas | Pipeline invocado desde directorio distinto al módulo |
| Fallo controlado | Base inexistente: salida no cero, carpeta sin COMPLETADO.txt |
| Informe y gráficas | Generados en las tres corridas offline; figura final revisada visualmente |
| Pipeline online | HTTP real → Python → Psycopg → PostgreSQL; inicial 93, actualización 180; Gold 3→6 |
| Informe final ajustado | Reejecutado online y offline; fechas mensuales y leyenda legibles, coberturas visibles |
| Git | Sincronización inicial por fetch y pull --ff-only; revisión de alcance y diff sin errores de whitespace |

Los ensayos que alteran valores para provocar errores son **artificiales, exclusivamente en la base de pruebas y revertidos**. No se mezclaron con la muestra real publicada.

Los scripts reproducibles son `tests/validar_material.py` y `tests/probar_integracion.py`. Los logs, notebooks ejecutados y figuras de esta sesión permanecen en carpetas locales ignoradas `salidas_pruebas/` y `salidas_pipeline/`, fuera del commit. El informe final del chat identifica el commit y el resultado del push.

## Resultado Gold de referencia, copia congelada

| Ciudad | Mes | Días | Media Tmax (°C, redondeada) | Precipitación (mm) |
|---|---|---:|---:|---:|
| Armenia, Quindío | 2024-01 | 31 | 27.52 | 152.20 |
| Armenia, Quindío | 2024-02 | 29 | 26.68 | 313.80 |
| Barranquilla | 2024-01 | 31 | 33.78 | 0.30 |
| Barranquilla | 2024-02 | 29 | 32.91 | 26.50 |
| Bogotá | 2024-01 | 31 | 19.91 | 21.40 |
| Bogotá | 2024-02 | 29 | 19.81 | 76.80 |

En los seis grupos, las tres variables tienen cobertura del 100% de días del calendario. Las cifras describen esta muestra de reanálisis: no identifican estaciones, causas de diferencias ni tendencias climáticas.

## Preservación pedagógica y cambios de archivos

El notebook magistral pasó de 3792 a aproximadamente 7589 palabras Markdown; la práctica de 673 a 944. El conteo no demuestra calidad por sí solo: se revisó también la correspondencia de objetivos. Se conservan todos los bloques Pandas y SQL enumerados en el README. Se ampliaron fundamentos relacionales, interpretación de claves, transacciones, cobertura, comparación de herramientas y escenarios A–F. Se mantienen tres sesiones de 90 minutos y se distingue explicación, demostración, lectura y práctica autónoma.

Modificados: ambos notebooks, README, GUIA_POSTGRESQL, los seis programas/scripts de `ampliacion/` (01_preparar.py, 02_resumir.sql, 03_informar.py, consulta_local.py, ejecutar_resumen.sh, pipeline.sh), y los tres SQL 00_crear_y_cargar, 01_consultas_clase y 02_practica.

Creados: `.gitignore`, `.gitattributes`, este informe, `datos/README.md`, `datos/meteorologia.csv`, `datos/procedencia.json`, seis JSON `datos/originales/{armenia,bogota,barranquilla}_{inicial,actualizacion}.json`, `sql/resumen_mensual.sql`, `tests/validar_material.py`, `tests/probar_integracion.py` y `tests/requirements.txt`.

Eliminados por sustitución del caso científico: `datos/penguins.csv` y `sql/resumen_isla.sql`; permanecen recuperables en Git. No se modificaron otros módulos. Los archivos locales ajenos sin seguimiento se preservaron.

## Límites y verificaciones no realizadas

- No se repitió una instalación completa de Windows/WSL2/VS Code desde cero; se utilizó Ubuntu WSL2 existente. La guía conserva el procedimiento de preparación y autenticación local.
- La lectura local y ejecución offline de notebooks sí se probó; montajes interactivos de Google Drive/Colab y descarga alternativa Kaggle no se ejecutaron, pues necesitan cuentas/selección del estudiante.
- Las versiones mínimas de todos los rangos de dependencias no se ensayaron; arriba figuran las versiones efectivamente utilizadas.
- Los ejemplos remotos, memoria de 500 GB, lotes y Spark son material conceptual, no infraestructura desplegada ni benchmarks ejecutados.
- Bronze conserva primera recepción, no historial de revisiones. DO NOTHING no actualiza registros existentes. No se implementó DO UPDATE.
- La cobertura de Gold audita días publicados, no la completitud de todas las observaciones horarias subyacentes. Un mes sin ninguna fila no aparece; el calendario completo es ampliación.
- La modalidad online puede cambiar por revisión de la fuente o indisponibilidad futura; la reproducción exacta usa los JSON congelados.
