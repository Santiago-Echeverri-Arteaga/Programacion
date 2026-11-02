#!/usr/bin/env bash
# Exportación opcional; el pipeline principal no necesita este CSV intermedio.
set -euo pipefail
carpeta_script=$(dirname "$0")
cd "$carpeta_script/.."
export PGDATABASE="${PGDATABASE:-curso_datos}"
mkdir -p salidas_sql
temporal=$(mktemp salidas_sql/resumen.XXXXXX)

# En un if podemos decidir qué hacer si psql falla. No se reemplaza el CSV válido.
if psql -X -v ON_ERROR_STOP=1 --csv -f sql/resumen_mensual.sql > "$temporal"; then
    mv "$temporal" salidas_sql/resumen_mensual.csv
    echo 'Resultado guardado en salidas_sql/resumen_mensual.csv'
else
    rm "$temporal"
    echo 'Falló la consulta; se conserva el resultado anterior.' >&2
    exit 1
fi
# Una interrupción externa podría dejar el temporal, pero no reemplaza el CSV anterior.
