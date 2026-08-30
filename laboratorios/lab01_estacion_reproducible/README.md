# Laboratorio 1 — Una estación de trabajo reproducible

| Campo | Especificación |
|---|---|
| Fecha de realización/entrega | Jueves 10 de septiembre de 2026 |
| Modalidad | Tarea en parejas; no reemplaza la clase regular de ese día |
| Tiempo estimado | 120 minutos |
| Herramientas | WSL2/Ubuntu, Bash, Python 3, Git, GitHub y editor de texto |

## Teoría breve

La terminal recibe un comando y separa dos flujos: la salida normal, descriptor
`1`, y los errores, descriptor `2`. Una tubería (`|`) conecta la salida normal de
un comando con la entrada del siguiente. `>` y `1>` reemplazan un archivo;
`>>` y `1>>` anexan la salida normal; `2>` y `2>>` hacen lo mismo con los errores.

El orden de los caracteres importa: `1>> salida.txt` y `2>> errores.txt` son
redirecciones. En cambio, `>>1` y `>>2` anexan la salida normal a archivos
literalmente llamados `1` y `2`; no significan «flujo 1» y «flujo 2».

`grep` selecciona líneas que contienen un patrón; `wc -l` cuenta líneas;
`mkdir` crea directorios. Un archivo de Python es texto y puede ejecutarse con
`python3 nombre.py`. Para este laboratorio basta saber que
`print("texto")` envía texto a la salida normal. No se necesitan variables,
condicionales, ciclos ni funciones.

Un script Bash es un archivo de texto que comienza normalmente con
`#!/usr/bin/env bash` y guarda comandos en el orden en que deben ejecutarse.
`bash archivo.sh` pide a Bash que lo interprete aunque no tenga permiso de
ejecución. Para ejecutarlo directamente como `./archivo.sh`, se concede permiso
al propietario con:

```bash
chmod u+x archivo.sh
ls -l archivo.sh
./archivo.sh
```

La letra `x` visible en `ls -l` confirma el permiso. Un script puede llamar a
otro con `./otro.sh`; ese segundo archivo también necesita permiso de ejecución.
Si se invoca como `bash otro.sh`, el permiso no es necesario, pero en este
laboratorio se practicará explícitamente la primera forma.

Git registra versiones locales mediante `status`, `add`, `commit` y `log`.
GitHub almacena una copia remota; no reemplaza los commits locales.

## Objetivos

- crear y recorrer una estructura sencilla de directorios;
- construir tuberías pequeñas con `grep` y comandos de conteo;
- diferenciar y redirigir la salida normal y los errores;
- escribir y ejecutar un script `.sh` secuencial;
- conceder permisos con `chmod` y llamar un `.sh` desde otro `.sh`;
- crear y ejecutar un archivo de Python elemental;
- registrar el trabajo con el flujo básico de Git y publicarlo en GitHub;
- explicar por escrito y en video qué hizo cada comando importante.

## Requerimientos y límites

- usar el archivo [`datos/mediciones.txt`](datos/mediciones.txt) sin modificarlo;
- estudiar [`demo_filtrar_temperaturas.sh`](demo_filtrar_temperaturas.sh) y
  [`demo_contar_temperaturas.sh`](demo_contar_temperaturas.sh) como ejemplos, sin
  copiarlos como solución;
- crear desde cero un script principal llamado `analizar_mediciones.sh`;
- utilizar solamente comandos secuenciales;
- no usar variables de Bash, ciclos, condicionales, funciones, `awk`, `sed` ni
  características avanzadas de Git;
- no incluir contraseñas, tokens, claves privadas ni capturas que los revelen.

## Procedimiento

1. Comprueben con `pwd` y `ls` dónde están. Creen con `mkdir` una carpeta para
   datos, otra para resultados y otra para errores. Copien el archivo de
   mediciones a la ubicación que hayan decidido.
2. Inspeccionen el archivo y describan con sus palabras qué representa cada
   línea. Antes de ejecutar cada orden, predigan si verán algo en pantalla o si
   quedará escrito en un archivo.
3. Ejecuten primero `bash demo_filtrar_temperaturas.sh`. Después concedan permiso
   a los dos demos, compruébenlo y ejecuten el segundo directamente:

   ```bash
   chmod u+x demo_filtrar_temperaturas.sh demo_contar_temperaturas.sh
   ls -l demo_filtrar_temperaturas.sh demo_contar_temperaturas.sh
   ./demo_contar_temperaturas.sh
   ```

   Expliquen por qué el segundo demo necesita que el primero también sea
   ejecutable.
4. Construyan una tubería que seleccione con `grep` las líneas de un sensor y
   cuente cuántas hay. Construyan otra que seleccione un tipo de medición y
   conserve el resultado en un archivo.
5. Ejecuten una búsqueda válida y anéxenla dos veces a un archivo mediante
   `1>>`. Expliquen por qué el contenido crece.
6. Provoquen de forma controlada un error buscando en un archivo inexistente y
   anéxenlo mediante `2>>` a un registro de errores. La terminal no debe mezclar
   ese mensaje con los resultados correctos.
7. Creen por su cuenta un archivo `presentacion.py` que produzca al menos tres
   líneas de texto: nombre de la actividad, archivo analizado y una frase sobre
   el resultado. Ejecútenlo con `python3` y redirijan una ejecución a un archivo.
8. Escriban `analizar_mediciones.sh` con *shebang* y comandos secuenciales. Debe:

   - crear los directorios necesarios con `mkdir -p`;
   - llamar directamente con `./` al menos uno de los demos `.sh`;
   - contener una tubería propia con `grep`;
   - anexar salida normal con `1>>` y un error controlado con `2>>`;
   - ejecutar `presentacion.py` con `python3`.

   No se admiten variables, ciclos, condicionales ni funciones. Concedan permiso
   y ejecútenlo así:

   ```bash
   chmod u+x analizar_mediciones.sh
   ls -l analizar_mediciones.sh
   ./analizar_mediciones.sh
   ```

9. Inicialicen un repositorio. Usen `git status` antes y después de `git add`;
   creen al menos dos commits con mensajes que describan cambios reales y
   compruébenlos con `git log --oneline`.
10. Publiquen el repositorio en GitHub mediante el mecanismo de autenticación
   autorizado por la Universidad. Verifiquen que no contiene secretos ni
   archivos llamados accidentalmente `1` o `2`.
11. Una pareja diferente debe seguir la explicación escrita y repetir una
   tubería, la ejecución del `.sh` y la ejecución del archivo de Python sin ayuda
   oral.

## Resultados puntuales que deben obtener

La entrega debe mostrar, sin imponer una estructura de carpetas específica:

1. una estructura creada con `mkdir` que se entienda al verla con `ls`;
2. un archivo con las coincidencias de un sensor;
3. el conteo verificable de esas coincidencias;
4. un archivo donde dos usos sucesivos de `1>>` sean visibles;
5. un registro que contenga al menos un error real capturado con `2>>`;
6. `analizar_mediciones.sh` ejecutable, sin variables, ciclos, condicionales o
   funciones, que llame otro `.sh`;
7. evidencia de permisos de ejecución y una ejecución directa correcta;
8. la salida guardada de `presentacion.py` y una ejecución correcta en pantalla;
9. un historial Git con al menos dos commits y un `git status` final limpio;
10. una URL funcional del repositorio remoto.

No se entrega una lista de comandos resuelta. Cada equipo debe decidir las
tuberías exactas, ejecutarlas, comprobar sus archivos y explicar por qué producen
esos resultados.

## Explicación escrita y video

La explicación escrita debe incluir los comandos elegidos, la función del
*shebang*, `chmod`, `|`, `1>>` y `2>>`, la diferencia entre `bash archivo.sh` y
`./archivo.sh`, la diferencia entre Git y GitHub, un error encontrado y la forma
en que se verificó cada resultado.

El video de YouTube, de 3 a 5 minutos, debe mostrar los permisos con `ls -l`, la
ejecución directa de `analizar_mediciones.sh`, la llamada entre scripts, una
tubería, la ejecución de `presentacion.py` y el historial Git. Ambas personas
deben explicar al menos una decisión. Puede publicarse como no listado y no exige
mostrar el rostro.

## Evidencia individual

Sin equipo ni IA, cada estudiante interpreta una tubería, predice dónde termina
la salida de una orden con `1>>` y `2>>`, explica qué cambia con `chmod u+x`,
distingue `bash archivo.sh` de `./archivo.sh`, interpreta un `git status` sencillo
y dice cómo ejecutaría un archivo `.py` desde la terminal.
