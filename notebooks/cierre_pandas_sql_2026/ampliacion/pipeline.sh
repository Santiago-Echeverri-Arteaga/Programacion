#!/usr/bin/env bash
# Uso: bash ampliacion/pipeline.sh [offline|online] [inicial|actualizacion]
# Cada etapa aparece en una línea. Ejemplos explicados en ejemplos/.
set -euo pipefail

# Buscar el módulo aunque se lance el script desde otra carpeta.
carpeta_script=$(dirname "$0")
cd "$carpeta_script/.."
raiz=$(pwd)

# $1 y $2 son las dos palabras escritas después del nombre del script.
# Solo usamos condicionales; no hay expresiones regulares ni parser de opciones.
modo=offline
fase=inicial
if [ "$#" -gt 2 ]; then
    echo 'Uso: pipeline.sh [offline|online] [inicial|actualizacion]' >&2
    exit 2
fi
if [ "$#" -ge 1 ]; then
    modo="$1"
fi
if [ "$#" -eq 2 ]; then
    fase="$2"
fi
if [ "$modo" != offline ] && [ "$modo" != online ]; then
    echo 'El modo debe ser offline u online.' >&2
    exit 2
fi
if [ "$fase" != inicial ] && [ "$fase" != actualizacion ]; then
    echo 'La fase debe ser inicial o actualizacion.' >&2
    exit 2
fi

# export permite que los programas Python reciban estos valores.
export MODO_DATOS="$modo"
export FASE_DATOS="$fase"
export PGDATABASE="${PGDATABASE:-curso_datos}"
command -v psql >/dev/null
command -v python >/dev/null
python -c 'import psycopg, pandas, numpy, matplotlib'

# mktemp crea una carpeta NUEVA. No se sobreescriben informes anteriores.
mkdir -p "$raiz/salidas_pipeline"
ejecucion=$(mktemp -d "$raiz/salidas_pipeline/ejecucion.XXXXXX")
export CARPETA_SALIDA="$ejecucion"
echo "Carpeta de esta ejecución: $ejecucion"

# 1. Preparar estructuras persistentes.
psql -X -v ON_ERROR_STOP=1 -f sql/00_crear_y_cargar.sql
# 2. Cargar Bronze y preparar Silver (transacción dentro de Python).
python ampliacion/01_preparar.py > "$ejecucion/carga.txt"
cat "$ejecucion/carga.txt"
# 3. Consultar Gold.
psql -X -v ON_ERROR_STOP=1 -f sql/resumen_mensual.sql > "$ejecucion/consulta.txt"
# 4. Recuperar Gold directamente y crear el análisis, figura e informe.
python ampliacion/03_informar.py
# Si alguna etapa falla, set -e detiene el script antes de esta línea.
echo 'Ingesta, preparacion, consulta y analisis completados.' > "$ejecucion/COMPLETADO.txt"
echo "Resultados: $ejecucion"
