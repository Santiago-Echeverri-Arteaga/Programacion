# PostgreSQL local con Ubuntu WSL2 y VS Code

## Qué se ejecuta dónde

| Componente | Lugar y función |
|---|---|
| VS Code | Aplicación Windows con extensión WSL; edita archivos de Ubuntu |
| Bash | Terminal de Ubuntu integrada en esa ventana de VS Code |
| PostgreSQL | Servicio en Ubuntu: conserva tablas y evalúa SQL |
| psql | Cliente de terminal que envía archivos `.sql` al servicio |
| Python/Psycopg | Cliente del pipeline: ingesta HTTP y recuperación de resultados, entorno virtual Ubuntu |
| Colab | Alternativa para Pandas; no se conecta a este PostgreSQL |
| Open-Meteo | API remota; copia JSON offline en la carpeta del módulo |

Realiza la preparación antes de las clases. Puede requerir reiniciar Windows y permisos de administrador. La instalación no está incluida en los 270 minutos de contenido. No se ejecutan comandos de configuración automáticamente al abrir los notebooks.

## 1. PowerShell de Windows: WSL2 y Ubuntu

Primero consulta instalaciones existentes:

```powershell
wsl --list --verbose
```

Si Ubuntu ya aparece con VERSION 2, úsalo. Si no tienes WSL, abre PowerShell como administrador:

```powershell
wsl --install -d Ubuntu
```

Reinicia si Windows lo solicita. Abre Ubuntu, crea tu usuario y contraseña Linux y verifica otra vez `wsl --list --verbose` en PowerShell. Si tu distribución existente figura con versión 1, usa `wsl --set-version Ubuntu 2`, sustituyendo Ubuntu por su nombre exacto. Si la instalación pide virtualización, sigue la documentación de Microsoft o solicita apoyo del laboratorio; no reinstales una distribución que ya contiene tus archivos.

## 2. VS Code conectado a Ubuntu

Instala VS Code **en Windows** y la extensión **WSL** de Microsoft. Abre la terminal Ubuntu y crea una carpeta de trabajo:

```bash
mkdir -p ~/curso_datos
cd ~/curso_datos
code .
```

La esquina inferior de VS Code debe indicar `WSL: Ubuntu` (o el nombre de tu distribución). Abre Terminal → Nueva terminal y comprueba `uname -s` (Linux), `whoami` (tu usuario Ubuntu) y `pwd` (ruta `/home/...`). Si ves un prompt de PowerShell, aún no estás trabajando en la terminal correcta.

Descarga y extrae el paquete del curso. Copia su contenido dentro de `~/curso_datos`, de modo que allí queden `sql`, `datos`, `ampliacion` y los notebooks. Puedes abrir el Explorador en esa carpeta ejecutando `explorer.exe .` desde Ubuntu y copiar allí los archivos ya extraídos de Descargas. Trabaja con los scripts SQL desde esa carpeta. El notebook puede seguir abierto en Colab como material de lectura; los bloques SQL se ejecutan en Ubuntu.

## 3. Terminal Bash de Ubuntu: instalar y arrancar

```bash
sudo apt update
sudo apt install postgresql postgresql-client python3-venv
sudo service postgresql start
pg_isready
psql --version
pg_lsclusters
```

`sudo` pide tu contraseña de Ubuntu, no una contraseña de PostgreSQL. `pg_isready` debe indicar que acepta conexiones. `psql --version` informa la versión del cliente; `SELECT version()` mostrará la del servidor. Usamos la versión mantenida por los repositorios de Ubuntu; no hace falta una versión mayor específica para estas consultas. PostgreSQL se usa localmente: no es necesario abrir puertos ni habilitar acceso de red desde Colab.

## 4. Crear tu rol y base de práctica (una vez)

En una instalación nueva, crea un rol con el mismo nombre de tu usuario Ubuntu y hazlo propietario de una base de práctica:

```bash
sudo -u postgres createuser --no-superuser --no-createdb --no-createrole "$USER"
sudo -u postgres createdb --owner="$USER" curso_datos
psql -X -d curso_datos -c 'SELECT current_database(), current_user, version();'
```

Solo estos pasos administrativos usan el usuario postgres. El trabajo de clase se realiza con tu propio rol. Ubuntu usa normalmente autenticación **peer** para sockets locales: comprueba que el usuario Linux coincide con el rol PostgreSQL. Por eso omitimos `-h` y no necesitamos guardar contraseñas. No cambies la autenticación a `trust`.

Si el rol o la base ya existen, no los borres ni repitas la creación. Comprueba la conexión y el propietario: `sudo -u postgres psql -c '\l curso_datos'`. Si la base pertenece a otra persona o a otro ejercicio, crea una base nueva con otro nombre y úsalo de forma consistente en todos los comandos y ejemplos de Python.

## 5. Entorno Python en Ubuntu (fuera de clase)

Desde la carpeta que contiene los notebooks, `sql`, `datos` y `ampliacion`:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r ampliacion/requirements.txt
# Para ejecutar los notebooks y su verificación automática:
python -m pip install nbformat nbclient ipykernel
```

Selecciona `.venv/bin/python` como intérprete/kernel en VS Code conectado a WSL. Un Python de Windows no comparte el socket local ni las bibliotecas de este entorno. La primera instalación necesita red; luego la modalidad offline no consulta la API. No instales Spark, MySQL, DuckDB, Docker ni servicios cloud.

Psycopg usa por defecto el mismo socket y usuario que psql. `PGDATABASE` selecciona la base en todos los scripts; si no se define usan `curso_datos`. Sin `PGHOST` ni `-h`, la instalación Ubuntu habitual utiliza peer. Una configuración personalizada debe revisarse antes de cambiar variables; no muestres contraseñas en código ni en el notebook.

## 6. Carga inicial y actualización

```bash
source .venv/bin/activate
export PGDATABASE=curso_datos
bash ampliacion/pipeline.sh offline inicial
bash ampliacion/pipeline.sh offline actualizacion
bash ampliacion/pipeline.sh offline actualizacion
```

En una base nueva: Silver **93 → 180 → 180** y Gold **3 → 6 → 6** filas. Cada fase crea una carpeta nueva `salidas_pipeline/ejecucion.XXXXXX/`. Allí aparecen `carga.txt`, `consulta.txt`, `resumen_mensual.csv`, `procedencia.json`, `temperatura_mensual.png`, `informe.md` y, solo al terminar, `COMPLETADO.txt`.

El CSV inicial de Pandas ya contiene los 180 registros; la base se carga en dos etapas. La primera incluye enero; la actualización incluye 25 de enero a 29 de febrero de 2024. Los 21 registros solapados se omiten por clave, se añaden 87 y se conservan los anteriores. Repetir inicial después de actualizar no vuelve a 93: se conserva lo ya cargado. No borres las tablas para repetir consultas.

Para observar cada paso por separado:

```bash
psql -X -v ON_ERROR_STOP=1 -f sql/00_crear_y_cargar.sql
export MODO_DATOS=offline
export FASE_DATOS=inicial
python ampliacion/01_preparar.py
psql -X -v ON_ERROR_STOP=1 -f sql/resumen_mensual.sql
export MODO_DATOS=offline
export FASE_DATOS=actualizacion
python ampliacion/01_preparar.py
python ampliacion/consulta_local.py
```

`00_crear_y_cargar.sql` crea estructuras y catálogo; la ingesta de valores corresponde a Python. El nombre del archivo se conserva para continuidad con el módulo anterior. No borra datos, y `IF NOT EXISTS` no migra estructuras de otra versión: si el esquema ya tiene tablas ajenas, usa otra base propia.

Para obtener de nuevo las mismas fechas desde internet:

```bash
bash ampliacion/pipeline.sh online inicial
bash ampliacion/pipeline.sh online actualizacion
```

La API remota puede revisar su producto. Offline verifica los hashes de JSON congelados y reproduce la muestra documentada. Online registra URL y hash de la respuesta recibida para cada clave nueva. Ambos caminos pasan por las mismas reglas. No existe sustitución silenciosa online→offline ante un fallo; elige el modo explícitamente.

## 7. Consultas en psql y archivos

```bash
psql -X -v ON_ERROR_STOP=1 -f sql/01_consultas_clase.sql
psql -X
```

En el prompt psql, termina cada SQL con `;`. `curso_datos->` significa que falta terminar la sentencia. `\r` limpia el buffer, `\dt silver.*` lista tablas, `\d silver.observaciones` muestra estructura y `\q` regresa a Bash. Sal del paginador con `q` o desactívalo con `\pset pager off`. Las metaórdenes con barra invertida son del cliente, no SQL del servidor. Una transacción fallida requiere `ROLLBACK;`.

```sql
SELECT COUNT(*) FROM silver.observaciones;
SELECT ciudad_id,fecha,COUNT(*) FROM silver.observaciones
GROUP BY ciudad_id,fecha HAVING COUNT(*)>1;
SELECT * FROM gold.mensual ORDER BY ciudad_id,mes;
```

La segunda consulta debe devolver cero filas. Gold usa días del calendario: precipitación mensual es NULL si falta algún valor diario, incluso si faltan días enteros de la tabla. Las medias disponibles llevan coberturas. Un mes completamente ausente no aparece en esta vista; no se inventan días ni ceros.

Guarda tus preguntas en `.sql` y ejecútalas con `psql -f`. SQLTools o pgAdmin son clientes opcionales; no hacen falta. Exportación opcional:

```bash
bash ampliacion/ejecutar_resumen.sh
head -n 5 salidas_sql/resumen_mensual.csv
```

El script escribe a un temporal y reemplaza el CSV solo tras terminar la consulta. El flujo principal recupera Gold directamente con Psycopg: no necesita ese CSV intermedio.

## 8. Seguir el pipeline y entender fallos

Bash coordina ingesta, preparación, consultas y análisis. Python usa urllib de la biblioteca estándar para descargar JSON y Psycopg para enviar filas. Bronze conserva primera recepción, URL, SHA-256 y momento de carga. Silver impone tipos, claves y condiciones físicas. `INSERT INTO ... SELECT` promueve datos dentro de la **misma transacción** que la carga Bronze. Gold es una vista mensual; al consultarla incorpora cambios confirmados.

`03_informar.py` recibe solo las filas agregadas, crea un DataFrame, comprueba cobertura con NumPy y genera informe/figura. La persistencia, reglas compartidas y actualización son aportes reales de PostgreSQL. Las tres herramientas no se limitan a recalcular el mismo promedio.

`set -euo pipefail` detiene el flujo ante fallos, pero no revierte toda la ejecución como una sola transacción. Si falla la ingesta, se revierten sus escrituras Bronze/Silver. Si falla la figura después de confirmar la ingesta, las tablas permanecen y la carpeta queda sin COMPLETADO.txt. Repetir no duplica claves. No reutilices carpetas incompletas como resultados finales.

DO NOTHING **no corrige valores existentes**. Un registro nuevo y una revisión de un registro antiguo requieren políticas distintas. Este módulo conserva primera recepción; un historial de revisiones y DO UPDATE quedan como ampliación, no requisito.

## 9. Pruebas en una base independiente

Nunca uses una base personal como banco de pruebas. Si tu rol no tiene permiso CREATEDB, un administrador puede crear una base **nueva**, sin borrar ni reemplazar ninguna:

```bash
sudo -u postgres createdb --owner="$USER" test_meteo_curso
export PGDATABASE=test_meteo_curso
python tests/probar_integracion.py
python tests/validar_material.py
```

La prueba integral exige nombre con prefijo `test_meteo_` y rechaza esquemas existentes: no resetea bases ni elimina registros personales. Conserva la base al terminar para inspección; para una nueva ejecución usa otro nombre. Comprueba carga 93, actualización 180, repetición, conservación de datos, restricciones, transacciones, Gold contra Pandas, consulta Python, scripts Bash, figuras y fallo controlado. `validar_material.py` valida notebooks, sintaxis, hashes y ejecución Python desde kernel limpio sin API.

Los resultados concretos de la revisión de este repositorio figuran en `VALIDACION.md`; no confundir un procedimiento disponible con una prueba realmente ejecutada. El entorno de pruebas puede usar una instancia temporal independiente; el entorno docente sigue siendo una sola instancia local.

## 10. Problemas frecuentes y cierre

- **Archivo inexistente:** revisa `pwd`, `ls sql` y la carpeta del módulo. El pipeline resuelve rutas desde su propia ubicación; los comandos manuales de esta guía se ejecutan desde el módulo.
- **Socket no encontrado:** `sudo service postgresql start`, `pg_isready`, `pg_lsclusters`. Si hay varios puertos, establece `PGPORT` consistentemente.
- **Rol inexistente:** compara `whoami` con el rol creado en el paso 4.
- **Peer authentication failed:** no uses `-U postgres` como usuario común ni fuerces `-h localhost`; comprueba rol/usuario. Una instalación personalizada puede necesitar revisión del administrador, no cambiar a trust.
- **Relation does not exist:** verifica `current_database()`, crea estructuras y ejecuta ingesta en esa misma base.
- **ModuleNotFoundError:** activa el entorno Ubuntu y utiliza `python -m pip` del mismo intérprete.
- **HTTP 429, timeout o sin red:** elige offline; no generes datos ficticios ni reintentos masivos.
- **Hash, unidades o fechas inesperadas:** detén la carga y revisa la procedencia. No desactives controles para forzar un resultado.
- **CHECK o clave foránea incumplidos:** la transacción revierte la carga; revisa fuente, unidades y catálogo. No elimines restricciones para pasar la prueba.

Cerrar VS Code no borra tablas. Después de reiniciar WSL comprueba el servicio. No uses `wsl --unregister`: elimina distribución y datos. Las copias originales están en archivos del módulo, las tablas en el almacenamiento interno PostgreSQL, la API en internet y los DataFrames en la RAM de Python.

Para continuar: lee los escenarios A–F del notebook. Lotes, agregaciones cercanas a los datos y sistemas distribuidos responden a límites distintos. Spark, Parquet, almacenamiento de objetos y orquestadores son proyección conceptual, no instalaciones de esta práctica.

Documentación: [WSL](https://learn.microsoft.com/en-us/windows/wsl/install), [VS Code/WSL](https://code.visualstudio.com/docs/remote/wsl), [PostgreSQL](https://www.postgresql.org/docs/current/tutorial-sql.html), [psql](https://www.postgresql.org/docs/current/app-psql.html), [Psycopg](https://www.psycopg.org/psycopg3/docs/basic/usage.html).

## 11. Scripts sencillos y configuración explícita

Las órdenes del pipeline no cambian. Los programas Python ya no reciben opciones --modo, --fase, --db o --carpeta: Bash les comunica esas decisiones con export. Para ejecutarlos individualmente:

```bash
export PGDATABASE=curso_datos
export MODO_DATOS=offline
export FASE_DATOS=inicial
python ampliacion/01_preparar.py
export FASE_DATOS=actualizacion
python ampliacion/01_preparar.py
mkdir -p salidas_pipeline
export CARPETA_SALIDA=$(mktemp -d salidas_pipeline/manual.XXXXXX)
python ampliacion/03_informar.py
```

Python usa offline/inicial/curso_datos si sus variables no existen. El informe exige CARPETA_SALIDA para evitar escribir en una ubicación no elegida. Las variables siguen definidas en esa terminal; compruébalas o reasígnalas antes de ejecutar otra práctica. El pipeline establece explícitamente modo y fase a partir de sus argumentos. La prueba integral también toma su base de PGDATABASE y sigue exigiendo el prefijo test_meteo_ y esquemas aún inexistentes.

Consulta `ejemplos/README.md`. Allí se explican archivos, JSON, fechas, hashes, export, with, cursores, parámetros SQL, formato de informes y las órdenes Bash conservadas. En Bash retiramos las expresiones regulares, arrays y trap; la exportación opcional usa if para conservar el CSV previo si psql falla. Una interrupción externa podría dejar un temporal, sin reemplazar el resultado válido.
