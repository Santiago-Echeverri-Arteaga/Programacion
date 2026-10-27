#!/usr/bin/env bash
# Ejecutar desde la raíz del material: bash ampliacion/ejecutar_resumen.sh
set -euo pipefail
mkdir -p salidas_sql
temporal=$(mktemp salidas_sql/resumen.XXXXXX)
trap 'rm -f -- "$temporal"' EXIT
psql -X -v ON_ERROR_STOP=1 -d curso_datos --csv -f sql/resumen_isla.sql > "$temporal"
# Reemplaza solo el resultado del ejercicio si la consulta terminó correctamente.
mv -- "$temporal" salidas_sql/resumen_isla.csv
printf '%s\n' 'Resultado guardado en salidas_sql/resumen_isla.csv'
