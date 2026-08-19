#!/usr/bin/env bash

# Laboratorio 1: script secuencial. No requiere variables ni control de flujo.
mkdir -p resultados

ls -lah > resultados/listado.txt
ls -lah datos >> resultados/listado.txt 2> resultados/errores.log

grep -n "sensor" datos/mediciones.txt > resultados/coincidencias.txt 2>> resultados/errores.log
grep -n "temperatura" datos/mediciones.txt >> resultados/coincidencias.txt 2>> resultados/errores.log

# TODO: contar con una tubería las líneas que contienen "sensor" y guardar el
# resultado en resultados/conteo.txt.

# TODO: anexar a resultados/listado.txt una lista detallada de resultados/.

