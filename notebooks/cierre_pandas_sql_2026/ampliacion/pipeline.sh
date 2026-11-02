#!/usr/bin/env bash
# Uso: bash ampliacion/pipeline.sh [offline|online] [inicial|actualizacion]
set -euo pipefail
raiz=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
modo=${1:-offline}
fase=${2:-inicial}
if [[ $# -gt 2 || ! "$modo" =~ ^(offline|online)$ || ! "$fase" =~ ^(inicial|actualizacion)$ ]]; then
  printf '%s\n' 'Uso: pipeline.sh [offline|online] [inicial|actualizacion]' >&2
  exit 2
fi
export PGDATABASE=${PGDATABASE:-curso_datos}
command -v psql >/dev/null
command -v python >/dev/null
python -c 'import psycopg, pandas, numpy, matplotlib'
mkdir -p "$raiz/salidas_pipeline"
ejecucion=$(mktemp -d "$raiz/salidas_pipeline/ejecucion.XXXXXX")
trap 'printf "Pipeline detenido; revisa %s\n" "$ejecucion" >&2' ERR
psql -X -v ON_ERROR_STOP=1 -f "$raiz/sql/00_crear_y_cargar.sql"
python "$raiz/ampliacion/01_preparar.py" --modo "$modo" --fase "$fase" | tee "$ejecucion/carga.txt"
psql -X -v ON_ERROR_STOP=1 -f "$raiz/sql/resumen_mensual.sql" > "$ejecucion/consulta.txt"
python "$raiz/ampliacion/03_informar.py" --carpeta "$ejecucion"
printf '%s\n' 'Ingesta, preparacion, consulta y analisis completados.' > "$ejecucion/COMPLETADO.txt"
printf 'Resultados: %s\n' "$ejecucion"
