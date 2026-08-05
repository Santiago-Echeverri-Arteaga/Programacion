# Laboratorio 1 — Estación científica reproducible

## 1. Identificación

| Campo | Especificación |
|---|---|
| Duración presencial | 120 min |
| Trabajo | Parejas con roles rotativos |
| Herramientas | Linux, Bash, Git y editor de texto |
| IA | Nivel 1: documentación y ayuda de comandos; no generación de la solución |
| Archivo inicial | [`resumir_mediciones.sh`](resumir_mediciones.sh) |

## 2. Pregunta de trabajo

¿Puede otra persona reconstruir qué archivos se procesaron y qué comandos
produjeron un resumen sin recibir instrucciones orales?

## 3. Marco teórico breve

Un resultado computacional es reproducible si están identificados sus datos de
entrada, procedimiento, ambiente y salida, y si el proceso puede repetirse. En
Linux, archivos y procesos se manipulan mediante rutas, permisos y flujos de
texto. Las tuberías conectan la salida estándar de un programa con la entrada de
otro; las redirecciones guardan o separan salidas. Un script conserva la secuencia
de comandos. Git registra estados mediante commits, pero un commit local no es por
sí mismo una copia remota ni prueba que el resultado sea correcto.

## 4. Objetivos

- construir una estructura de proyecto que se ejecute desde su raíz;
- procesar archivos con tuberías y un script Bash seguro;
- registrar cambios pequeños y explicativos en Git;
- verificar repetibilidad desde una copia limpia.

## 5. Materiales y datos

- sala Linux con Bash y Git;
- conjunto de archivos suministrado por el docente;
- guía de Linux/Bash y Git del repositorio;
- archivo inicial de esta carpeta.

No renombre ni modifique los datos originales. No se requieren privilegios de
administrador.

## 6. Procedimiento

1. Registre `uname -a`, `bash --version`, `git --version` y la ruta del proyecto.
2. Cree `datos/raw`, `scripts` y `resultados`; documente cada carpeta.
3. Copie los datos suministrados a `datos/raw` y calcule una suma de verificación
   con la herramienta indicada por el docente.
4. Inspeccione tipo, tamaño, número de líneas y encabezado sin alterar archivos.
5. Use `find`, `grep`, `sort`, `uniq`, `wc`, tuberías y redirecciones para localizar
   registros marcados y producir un resumen preliminar.
6. Complete y traslade `resumir_mediciones.sh` a `scripts/`. Active `set -euo
   pipefail`, use comillas y rutas independientes del usuario.
7. Ejecute dos veces y compare los resúmenes. Explique cualquier diferencia.
8. Inicialice Git. Produzca al menos tres commits coherentes: estructura/datos,
   script y documentación/corrección.
9. Prepare `.gitignore` para temporales y salidas regenerables justificadas.
10. Clone o copie la versión entregable en un directorio limpio y siga solamente
    el README para reproducir el resumen.

## 7. Registro y análisis

Conserve los comandos relevantes, códigos de salida, suma de verificación,
historial abreviado y comparación de resultados. Responda:

1. ¿Qué información se perdería si solo se entregara `resumen.txt`?
2. ¿Qué archivos deben versionarse y cuáles pueden regenerarse?
3. ¿Por qué un commit no equivale a una copia de seguridad remota?
4. ¿Qué parte del procedimiento depende todavía del sistema operativo?

## 8. Qué se debe presentar

- informe PDF según [`../plantilla_informe.md`](../plantilla_informe.md), de 4–6
  páginas sin anexos;
- repositorio con README, datos originales, `scripts/resumir_mediciones.sh`,
  `.gitignore` e historial solicitado;
- `resultados/resumen.txt` y evidencia de comparación de dos ejecuciones;
- registro individual de roles y decisiones.

El README debe contener requisitos, estructura, entrada, ejecución, salida y
problemas conocidos. El informe incluye diagrama o descripción del flujo, tabla
de comprobaciones y discusión sobre reproducibilidad.

## 9. Criterios particulares

Además de la rúbrica común, se revisan rutas portables, uso seguro de Bash,
commits comprensibles y reproducción desde limpio. Un script que solo funciona en
la cuenta de su autor no cumple el objetivo central.

## 10. Evidencia individual

Sin equipo ni IA: interpretar un `git status`, explicar una tubería suministrada
por el docente y proponer una comprobación de repetibilidad.
