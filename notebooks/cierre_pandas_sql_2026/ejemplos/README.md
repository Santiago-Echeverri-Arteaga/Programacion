# Ejemplos para comprender los scripts

Estos archivos explican las funcionalidades nuevas que el pipeline necesita. Se leen y ejecutan fuera de clase, sin ampliar las tres sesiones. No hace falta dominar la implementación interna de HTTP, JSON o PostgreSQL: el objetivo es comprender qué entra, qué sale y qué se confirma.

| Orden | Archivo | Qué explica | Requisitos |
|---|---|---|---|
| 1 | `01_archivos_y_json.py` | Path, __file__, bytes, JSON como diccionarios/listas, None, fechas, SHA-256, with y HTTP | Python; datos locales incluidos |
| 2 | `02_conexion_y_transaccion.py` | export/os.environ, conexión, cursor, parámetros %s, tupla de un elemento, fetch y rollback | Psycopg y base propia ya cargada |
| 3 | `03_tablas_e_informe.py` | itertuples, isna, formato decimal/porcentaje, join y backend Agg | Pandas; datos locales incluidos |
| 4 | `04_bash_paso_a_paso.sh` | Argumentos, if, comillas, export, sustitución de comandos, set, códigos de salida, redirección y mktemp | Bash y Python |

Desde la carpeta del módulo, con el entorno activado:

```bash
python ejemplos/01_archivos_y_json.py
python ejemplos/03_tablas_e_informe.py
bash ejemplos/04_bash_paso_a_paso.sh inicial
# Solo cuando la base ya esté preparada:
export PGDATABASE=curso_datos
python ejemplos/02_conexion_y_transaccion.py
```

En el primero verás dict/list, el día 2024-01-01, tres máximas reales y el paso del 28 al 29 de febrero de 2024. En el tercero aparecen tres ciudades, medias de máximas y cobertura. El ejemplo Bash muestra que Python recibe la fase, escribe y lee dos líneas en un temporal propio y trata un error esperado. El ejemplo PostgreSQL consulta hasta tres días reales y revierte una tabla temporal artificial: no modifica observaciones.

## Del ejemplo al programa

`01_preparar.py` separa cuatro pasos: `leer_respuesta`, `filas_respuesta`, `guardar` y `cargar`. Los ciclos muestran cómo se recorre cada columna y se construye cada fila. La mínima/máxima y precipitación se validan además en Silver. El ciclo de INSERT es suficiente para las 180 filas; no se presenta como la opción más rápida para millones de registros.

`03_informar.py` conserva el análisis Pandas/NumPy ya estudiado y muestra la construcción del informe con condicionales explícitos. `pipeline.sh` ejecuta una etapa por línea. Es más largo que una versión compacta, pero permite inspeccionar el estado tras cada paso sin descifrar expresiones anidadas.

## Qué significa evitar parsing aquí

Eliminamos el analizador de opciones argparse y no lo reemplazamos por otro parser manual. Python lee variables de entorno que Bash exporta. Las fechas inicial/final están explícitas en el manifiesto, en vez de extraerlas del texto de una URL. Bash comprueba dos argumentos con if, sin expresiones regulares ni arrays.

Se conserva `json.loads` para interpretar el formato de la API y `date.fromisoformat` para crear fechas. Quitarlos obligaría a escribir conversiones manuales más difíciles y propensas a errores. También se conservan hashes, transacciones, SQL parametrizado y comprobaciones de calidad: permiten mantener el resultado y la seguridad de las cargas.

Las utilidades de `tests/` son herramientas de verificación del material, no programas que el estudiante deba escribir en clase; utilizan nbclient/subprocess y pruebas deliberadas de fallos. Los ejemplos docentes están separados para no confundir esas pruebas con el flujo científico.

Los programas Python también comprueban `len(sys.argv)`: esa lista contiene el nombre del archivo y las palabras añadidas al ejecutarlo. Si hay opciones antiguas, muestran un error para evitar ejecutar por accidente la fase predeterminada. Solo cuentan argumentos; no interpretan sus nombres ni valores. En condiciones normales, `python ampliacion/01_preparar.py` produce una lista de un elemento.
