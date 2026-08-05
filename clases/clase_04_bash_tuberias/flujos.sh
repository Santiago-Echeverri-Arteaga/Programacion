#!/usr/bin/env bash
set -euo pipefail

directorio_script="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ruta="$directorio_script/../../datos/enfriamiento_sintetico_sucio.csv"
echo "Conteo por sensor de filas marcadas como sospechosas:"
grep ',sospechosa$' "$ruta" | cut -d, -f2 | sort | uniq -c
