#!/usr/bin/env bash

# Ejecutar desde la raíz del repositorio.
mkdir -p tmp/bash_apoyo

grep -n "sospechosa" datos/enfriamiento_sintetico_sucio.csv > tmp/bash_apoyo/sospechosas.txt 2> tmp/bash_apoyo/errores.log
grep -n "sospechosa" datos/enfriamiento_sintetico_sucio.csv | wc -l > tmp/bash_apoyo/conteo.txt
ls -lah tmp/bash_apoyo >> tmp/bash_apoyo/listado.txt 2>> tmp/bash_apoyo/errores.log

