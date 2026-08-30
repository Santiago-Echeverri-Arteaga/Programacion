# Demo comentada — rutas y ayuda

Ejecute una orden por vez y prediga la salida antes de continuar:

```bash
pwd
mkdir -p practica_terminal/datos practica_terminal/resultados
cd practica_terminal
printf "sensor_a 20.1\nsensor_b 20.4\n" > datos/mediciones.txt
ls -lah
ls -lah datos
cp datos/mediciones.txt resultados/copia.txt
mv resultados/copia.txt resultados/mediciones_copia.txt
python3 --help
cd ..
```

La secuencia trabaja dentro de una carpeta creada para la demo. No usa comandos
de borrado. Al final, dibuje la ruta relativa entre el directorio actual y cada
archivo creado.
