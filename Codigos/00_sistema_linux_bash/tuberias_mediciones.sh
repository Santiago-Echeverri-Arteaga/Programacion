#!/usr/bin/env bash
set -euo pipefail

ruta="${1:-datos/enfriamiento_sintetico_sucio.csv}"

if [[ ! -f "$ruta" ]]; then
    echo "No existe el archivo: $ruta" >&2
    exit 2
fi

echo "Filas de datos: $(( $(wc -l < "$ruta") - 1 ))"
echo "Registros sospechosos:"
grep ',sospechosa$' "$ruta" | cut -d, -f2 | sort | uniq -c

