# Guía 01 — Computador, WSL2, Linux y Bash básico

## Ficha

- Realización: clase inicial ya realizada y encuentros del 25 al 27 de agosto.
- Aplicación: taller del 2 de septiembre y laboratorio del 3 de septiembre.
- Nivel de IA: 0 en el diagnóstico; 1 en práctica documental.
- Resultados: RA 1 y RA 2.

## Alcance reducido

La clase sobre funcionamiento del computador ya ocurrió antes de la interrupción.
Al reanudar, se recupera ese modelo y se prepara un entorno Linux reproducible en
WSL2. El estudiante aprende rutas, directorios, ayuda, búsqueda, flujos,
redirecciones, tuberías y ejecución de un script secuencial.

No se enseñan todavía condicionales, ciclos, funciones, arreglos, administración
del sistema ni expresiones regulares avanzadas. Tampoco se usan en el laboratorio
`set -euo pipefail`, variables o sustitución de comandos.

## Martes 25 de agosto — Sistema operativo y preparación de WSL2

### Resultados

- recuperar la relación entre almacenamiento, memoria, CPU, sistema operativo y
  proceso;
- distinguir Windows, WSL2 y una distribución Linux;
- instalar o verificar WSL2 sin borrar instalaciones existentes;
- explicar dónde viven los archivos de Linux y de Windows.

### Secuencia

| Tiempo | Actividad |
|---:|---|
| 0–20 | Recuperación de la clase previa y diagnóstico después de la interrupción |
| 20–45 | Windows, WSL2, Ubuntu, terminal y Bash |
| 45–65 | Demostración `wsl --install`, `wsl --status` y `wsl --list --verbose` |
| 65–85 | Primer usuario, actualización de paquetes e instalación de Git |
| 85–105 | Rutas `~/...`, `/mnt/c/...` y ubicación recomendada del proyecto |
| 105–120 | Inicio de `CONFIGURACION_WSL2.md` y salida individual |

La instalación que exija permisos o reinicio se termina antes del laboratorio. No
se usa `wsl --unregister` en esta unidad.

## Miércoles 26 de agosto — Sistema de archivos y terminal

```bash
pwd
ls
ls -lah
cd
cd ..
mkdir practica_linux
mkdir -p practica_linux/resultados
man ls
ls --help
```

Ideas evaluables:

- rutas absolutas y relativas;
- directorio actual y directorio personal;
- distinción entre archivo y directorio;
- nombres con espacios;
- lectura de ayuda antes de probar opciones;
- diferencia entre una ruta Windows y una ruta Linux.

No se realizan eliminaciones recursivas en la práctica inicial.

## Jueves 27 de agosto — Flujos, búsqueda y scripts secuenciales

```bash
grep -n "sensor" datos/mediciones.txt
grep -n "sensor" datos/mediciones.txt | wc -l
ls -lah > resultados/listado.txt
ls -lah >> resultados/listado.txt
grep -n "sensor" datos/mediciones.txt 2> resultados/errores.log
grep -n "temperatura" datos/mediciones.txt 2>> resultados/errores.log
bash comandos_basicos.sh
chmod u+x comandos_basicos.sh
./comandos_basicos.sh
```

Conceptos evaluables:

- salida estándar y salida de error;
- `>` frente a `>>`;
- `2>` frente a `2>>`;
- tubería `|`;
- búsqueda literal básica con `grep`;
- *shebang* y permiso de ejecución.

La sintaxis para anexar errores es `2>> archivo`. `>>2` anexa la salida estándar a
un archivo llamado `2`; no es una forma alternativa de escribir `2>>`.

## Taller del miércoles 2 de septiembre

El taller no introduce comandos nuevos. Cada pareja debe:

1. verificar WSL2 y Git;
2. crear la estructura del laboratorio;
3. predecir las salidas de cuatro redirecciones;
4. ejecutar un `.sh` de las dos formas enseñadas;
5. revisar la plantilla de documentación y los criterios del laboratorio.

## Errores previsibles

| Error | Aprendizaje esperado |
|---|---|
| Confundir `/` con `\` | Las rutas dependen del entorno |
| Trabajar sin saber el directorio actual | `pwd` precede el diagnóstico |
| Usar `>` cuando se quería anexar | La redirección puede reemplazar contenido |
| Escribir `>>2` para errores | El descriptor debe ir antes del operador: `2>>` |
| Ejecutar `./archivo.sh` sin permiso | Puede usarse `bash archivo.sh` o agregar permiso |
| Copiar un token al README | Las credenciales nunca se versionan |

## Salida individual

Sin ejecutar, predecir qué queda en pantalla y en cada archivo tras una tubería
con redirección separada de salida y error.
