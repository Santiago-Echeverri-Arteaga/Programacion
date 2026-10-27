# PostgreSQL local con Ubuntu WSL2 y VS Code

## Qué se ejecuta dónde

| Componente | Lugar y función |
|---|---|
| VS Code | Aplicación Windows con extensión WSL; edita archivos de Ubuntu |
| Bash | Terminal de Ubuntu integrada en esa ventana de VS Code |
| PostgreSQL | Servicio en Ubuntu: conserva tablas y evalúa SQL |
| psql | Cliente de terminal que envía archivos `.sql` al servicio |
| Python/Psycopg | Ampliación futura: otro cliente local, en entorno virtual Ubuntu |
| Colab | Solo la parte de Pandas; no se conecta a este PostgreSQL |

Realiza la preparación antes de la segunda clase. Puede requerir reiniciar Windows y permisos de administrador. La instalación no está incluida en los 270 minutos de contenido. No se ejecutan comandos de configuración automáticamente al abrir los notebooks.

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

## 5. Cargar datos reales y verificar

Desde `~/curso_datos`:

```bash
psql -X -v ON_ERROR_STOP=1 -d curso_datos -f sql/00_crear_y_cargar.sql
psql -X -d curso_datos -c 'SELECT COUNT(*) AS filas, COUNT(masa_g) AS masas FROM curso_penguins.observaciones;'
```

Esperado: **344 filas y 342 masas presentes**. La semilla carga el CSV público Palmer Penguins, crea un catálogo de especies y una tabla de observaciones. Crea el esquema dentro de la base que elegiste; no crea otra base. No contiene datos inventados ni borra tablas. Ejecuta la carga una sola vez. Repetirla da un error de tabla existente; conserva tus tablas y continúa con las consultas.

## 6. Trabajar con SQL puro

Abre `sql/01_consultas_clase.sql` en VS Code y lee sus consultas junto al notebook. Puedes ejecutar el archivo completo desde Bash:

```bash
psql -X -v ON_ERROR_STOP=1 -d curso_datos -f sql/01_consultas_clase.sql
```

Para explicar una consulta a la vez, entra a psql:

```bash
psql -X -d curso_datos
```

El prompt cambia a `curso_datos=>`. Pega SQL y termina la sentencia con `;`. Si aparece `curso_datos->`, psql espera que termines la sentencia. `\r` limpia el buffer si te equivocaste. `\dt curso_penguins.*` lista tablas, `\d curso_penguins.observaciones` muestra la estructura, `\q` vuelve a Bash. Si el resultado abre un paginador, sal con `q`; `\pset pager off` lo desactiva. Los comandos con barra invertida pertenecen a psql, no al lenguaje SQL. En una transacción fallida ejecuta `ROLLBACK;` antes de continuar.

También puedes escribir una consulta en `sql/mi_consulta.sql` y ejecutarla con `-f`. No necesitas una extensión de bases de datos en VS Code para este flujo. Los archivos son el historial reproducible de tus preguntas.

## 7. Bash y Python: ampliación fuera de clase

Ejecuta el pequeño flujo SQL → CSV desde Bash:

```bash
bash ampliacion/ejecutar_resumen.sh
head -n 5 salidas_sql/resumen_isla.csv
```

Lee el script: detiene la ejecución ante fallos y solo reemplaza el CSV de salida cuando psql termina correctamente. `set -euo pipefail` es control del script, no una transacción de base de datos.

Para conectar Python local, crea un entorno virtual de Ubuntu:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install 'psycopg[binary]>=3,<4'
python ampliacion/consulta_local.py
```

Psycopg usa el mismo socket local y usuario que psql. No requiere Colab, contraseña ni conexión externa. Abre el archivo y observa los parámetros `%s`: SQL y valores viajan separados. Para leer el CSV desde Python puedes instalar Pandas en ese entorno (`python -m pip install pandas`) y usar `pd.read_csv('salidas_sql/resumen_isla.csv')`. Si ejecutas desde VS Code, selecciona el intérprete `.venv/bin/python` de Ubuntu; un Python de Windows no comparte este socket ni el entorno.

## 8. Errores frecuentes y siguiente sesión

- **No such file / archivo inexistente:** revisa `pwd` y `ls sql`; entra en la carpeta del material.
- **Connection refused / socket no encontrado:** ejecuta `sudo service postgresql start` y `pg_isready` en Ubuntu. Si hay varios clústeres, revisa `pg_lsclusters` y usa el puerto correspondiente con `-p` de manera consistente.
- **role ... does not exist:** revisa `whoami` y crea el rol correspondiente en el paso 4.
- **Peer authentication failed:** no uses `-U postgres` como usuario común ni `-h localhost` con este esquema de conexión; comprueba que el rol coincide con el usuario Linux. Una instalación previamente personalizada puede necesitar revisión de su administrador.
- **relation does not exist:** comprueba la base con `SELECT current_database();`, la carga y el prefijo `curso_penguins`.
- **ModuleNotFoundError psycopg:** activa `.venv` y usa `python -m pip` del mismo intérprete.

Al terminar, `\q` sale del cliente. Cerrar VS Code no borra tablas. Después de reiniciar WSL, verifica `pg_isready` y arranca el servicio si es necesario. No uses `wsl --unregister`: elimina una distribución y sus datos. No necesitas detener ni borrar PostgreSQL para cerrar una práctica.

Documentación: [WSL](https://learn.microsoft.com/en-us/windows/wsl/install), [VS Code y WSL](https://code.visualstudio.com/docs/remote/wsl), [PostgreSQL en Ubuntu](https://ubuntu.com/server/docs/how-to/databases/install-postgresql/), [psql](https://www.postgresql.org/docs/current/app-psql.html), [Psycopg](https://www.psycopg.org/psycopg3/docs/basic/usage.html).


## 9. Pipeline completo: .sh + .py + .sql + informe

Este es el puente local después de practicar Pandas en Colab. No ejecuta ni implementa el trabajo final. Bash coordina procesos, Python prepara e interpreta datos y PostgreSQL hace la agregación.

1. `01_preparar.py` descarga el CSV público (o lee la copia local), valida columnas, tipos y valores positivos, conserva ausencias y exporta `datos.csv` con un orden de columnas definido. Guarda la fuente original y su hash en `procedencia.json`.
2. `02_resumir.sql` carga ese CSV con `\copy` en una tabla temporal, calcula cantidades, medias, dispersión y cobertura por isla y escribe `resumen.csv`. La tabla existe solo durante esa sesión y desaparece al confirmar la transacción. No modifica `curso_penguins`.
3. `03_informar.py` vuelve a calcular el resumen con Pandas para comprobar la salida SQL y genera `informe.md` y `masa_por_isla.png` con Matplotlib orientado a objetos.
4. `pipeline.sh` ordena los pasos y detiene la ejecución si alguno falla. Cada corrida usa una carpeta nueva bajo `salidas_pipeline/`; solo escribe `COMPLETADO.txt` al terminar todas las etapas.

Desde Ubuntu, con la base preparada y la terminal en la carpeta del material:

```bash
source .venv/bin/activate
python -m pip install -r ampliacion/requirements.txt
bash ampliacion/pipeline.sh
```

Si aún no creaste el entorno, primero ejecuta `python3 -m venv .venv`. La primera ejecución necesita internet para instalar dependencias y descargar la fuente. Con dependencias instaladas, puedes repetir sin descargar el CSV:

```bash
bash ampliacion/pipeline.sh datos/penguins.csv
```

Abre la carpeta que imprime el script y, en VS Code, usa la vista previa Markdown de `informe.md`. Comprueba la existencia del marcador final, las 344 filas de la copia incluida, las 342 masas y las tres islas del resumen. Los controles de tipos se aplican a cada fuente; los conteos 344/342 describen esta copia, no todo dataset futuro.

El archivo SQL contiene metaórdenes `\copy`, por lo que se ejecuta con **psql**, no directamente con `cur.execute()` de Psycopg. `consulta_local.py` demuestra por separado una consulta parametrizada desde Python a las tablas permanentes de clase. Esta distinción evita confundir SQL del servidor con funciones del cliente.

Si falla una etapa, consulta el error y conserva la carpeta parcial para diagnosticar. Un CSV exportado no se revierte con ROLLBACK: los archivos son externos a la transacción. Por eso las carpetas son nuevas y el marcador final solo se crea tras verificar el informe. No reutilices una carpeta incompleta como resultado válido.

Lectura sugerida: sigue una fila desde el CSV a la tabla temporal; después sigue un grupo desde SQL al informe. Modificaciones de práctica: cambia el agrupamiento a especie y ajusta SQL y validación Pandas juntos; agrega una comprobación de cobertura; explica por qué editar solo el SQL provoca un fallo de contrato. Son ampliaciones sin nota, no requisitos del proyecto.
