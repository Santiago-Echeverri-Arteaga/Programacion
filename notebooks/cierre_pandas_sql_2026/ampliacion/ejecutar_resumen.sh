#!/usr/bin/env bash
set -euo pipefail
raiz=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
export PGDATABASE=${PGDATABASE:-curso_datos}
mkdir -p "$raiz/salidas_sql"
temporal=$(mktemp "$raiz/salidas_sql/resumen.XXXXXX")
trap 'rm -f -- "$temporal"' EXIT
psql -X -v ON_ERROR_STOP=1 --csv -f "$raiz/sql/resumen_mensual.sql" > "$temporal"
mv -- "$temporal" "$raiz/salidas_sql/resumen_mensual.csv"
printf '%s\n' 'Resultado guardado en salidas_sql/resumen_mensual.csv'
