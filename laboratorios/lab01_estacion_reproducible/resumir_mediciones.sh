#!/usr/bin/env bash
set -euo pipefail

# Complete el script sin escribir rutas absolutas.
directorio_datos="datos"
archivo_salida="resultados/resumen.txt"

mkdir -p "$(dirname "$archivo_salida")"

echo "Resumen de mediciones" > "$archivo_salida"
# TODO: agregar número de archivos, número de filas y registros sospechosos.

