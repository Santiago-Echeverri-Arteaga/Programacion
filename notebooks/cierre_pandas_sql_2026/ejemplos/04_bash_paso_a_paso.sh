#!/usr/bin/env bash
# Ejemplo 4. Ejecuta: bash ejemplos/04_bash_paso_a_paso.sh inicial
# No usa PostgreSQL, no modifica datos y no necesita red.
set -euo pipefail
# -e: detener ante una orden fallida fuera de contextos como if.
# -u: detectar una variable usada sin definir.
# pipefail: si una orden de una tubería falla, no ocultarlo por éxito de la última.
# No constituyen una transacción ni revierten archivos ya escritos.

# $0: nombre/ruta del script; $#: cantidad de argumentos; $1: primer argumento.
fase=inicial
if [ "$#" -ge 1 ]; then
    fase="$1"
fi
if [ "$fase" != inicial ] && [ "$fase" != actualizacion ]; then
    echo 'Escribe inicial o actualizacion.' >&2
    exit 2  # Un código distinto de cero informa un error.
fi
# && exige que ambas comparaciones sean verdaderas. No es una expresión regular.
echo "Fase elegida: $fase"

# $(orden) guarda el texto que produce una orden.
carpeta=$(dirname "$0")
echo "Los ejemplos están en: $carpeta"
# Comillas dobles conservan rutas con espacios como un único argumento.

# Una variable normal pertenece al shell. export la transmite a programas hijos.
export FASE_DATOS="$fase"
# ${VARIABLE:-valor} usa valor si VARIABLE no existe o está vacía.
echo "Base elegida: ${PGDATABASE:-curso_datos}"
python -c 'import os; print("Python recibió:", os.environ.get("FASE_DATOS"))'
# -c ejecuta un fragmento corto Python; el pipeline lo usa para comprobar imports.

# command -v comprueba que un programa se puede encontrar.
# >/dev/null descarta la salida normal; >&2 escribe mensajes en el canal de errores.
if command -v python >/dev/null; then
    echo 'Python está disponible.'
else
    echo 'Activa el entorno virtual.' >&2
    exit 1
fi

# mktemp elige una carpeta nueva. Esta demostración solo escribe en ella.
carpeta_temporal=$(mktemp -d)
echo "Carpeta temporal de ejemplo: $carpeta_temporal"
echo 'Primera línea' > "$carpeta_temporal/ejemplo.txt"
echo 'Segunda línea' >> "$carpeta_temporal/ejemplo.txt"
# > crea/reemplaza el archivo; >> agrega al final. cat permite leerlo.
cat "$carpeta_temporal/ejemplo.txt"

# Un if permite tratar un fallo esperado sin que set -e detenga el ejemplo.
# false es una orden que siempre devuelve un código de error.
if false; then
    echo 'Esta línea no se ejecuta.'
else
    echo 'Se detectó el fallo y se eligió la rama else.'
fi

# Limpiar SOLO los archivos creados por este ejemplo, sin borrado recursivo.
rm "$carpeta_temporal/ejemplo.txt"
rmdir "$carpeta_temporal"
# En el pipeline, COMPLETADO.txt solo se escribe después de todas las etapas.
# Si una falla, las etapas siguientes no corren y ese marcador no aparece.
