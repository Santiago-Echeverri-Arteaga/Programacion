#!/usr/bin/env bash
# Usar: bash ampliacion/pipeline.sh [ruta_opcional_al_csv]
set -euo pipefail
raiz=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
entrada=()
if [[ $# -gt 1 ]]; then
  printf '%s\n' 'Uso: bash ampliacion/pipeline.sh [csv_local]' >&2
  exit 2
fi
if [[ $# -eq 1 ]]; then entrada=(--entrada "$(realpath -- "$1")"); fi
mkdir -p "$raiz/salidas_pipeline"
ejecucion=$(mktemp -d "$raiz/salidas_pipeline/ejecucion.XXXXXX")
# Si algo falla se conserva la carpeta para diagnosticar, sin marcador COMPLETADO.
trap 'printf "Pipeline detenido; revisa %s\n" "$ejecucion" >&2' ERR
python "$raiz/ampliacion/01_preparar.py" --salida "$ejecucion" "${entrada[@]}"
# Una sesión mantiene la tabla temporal durante la carga y el resumen.
(cd "$ejecucion" && psql -X -v ON_ERROR_STOP=1 -d curso_datos -f "$raiz/ampliacion/02_resumir.sql")
python "$raiz/ampliacion/03_informar.py" --carpeta "$ejecucion"
printf '%s\n' 'Todas las etapas terminaron correctamente.' > "$ejecucion/COMPLETADO.txt"
printf 'Resultados: %s\n' "$ejecucion"
