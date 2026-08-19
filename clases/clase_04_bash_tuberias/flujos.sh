#!/usr/bin/env bash

# Ejecutar desde la raíz del repositorio. Ejemplo secuencial para R1-C.
mkdir -p tmp/bash_clase

grep -n "sospechosa" datos/enfriamiento_sintetico_sucio.csv > tmp/bash_clase/sospechosas.txt 2> tmp/bash_clase/errores.log
grep -n "valida" datos/enfriamiento_sintetico_sucio.csv >> tmp/bash_clase/sospechosas.txt 2>> tmp/bash_clase/errores.log
grep -n "sospechosa" datos/enfriamiento_sintetico_sucio.csv | wc -l > tmp/bash_clase/conteo.txt
ls -lah tmp/bash_clase >> tmp/bash_clase/listado.txt 2>> tmp/bash_clase/errores.log
