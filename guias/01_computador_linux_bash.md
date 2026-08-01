# Guía 01 — Computador, Linux y Bash

## Ficha

- Semana: 1 y comienzo de la 2.
- Duración: cuatro encuentros de 120 minutos, incluido el inicio del laboratorio 1.
- Nivel de IA: 0 en el diagnóstico; 1 en la práctica.
- Resultados: RA 1 y RA 2.

## Alcance

El objetivo no es memorizar comandos ni impartir un curso de administración de
sistemas. El estudiante debe construir un modelo mental suficiente para entender
dónde está un archivo, qué programa ejecuta una orden, qué es un proceso y cómo
combinar herramientas pequeñas de forma reproducible.

## Encuentro 1 — Del hardware al programa

### Resultados

- Diferenciar almacenamiento, memoria, procesador y periféricos.
- Explicar qué servicios presta el sistema operativo.
- Distinguir programa, proceso, archivo y flujo de datos.

### Secuencia

| Tiempo | Actividad |
|---:|---|
| 0–20 | Diagnóstico individual: dibujar qué ocurre desde que se escribe `python experimento.py` hasta que aparece una salida |
| 20–45 | Reconstrucción colectiva: CPU, RAM, almacenamiento, kernel, procesos y dispositivos |
| 45–65 | Demostración de procesos y archivos abiertos |
| 65–95 | Comparación entre Windows, Linux y contenedor sin entrar en detalles de implementación |
| 95–112 | Análisis de tres fallas: archivo inexistente, permiso negado y programa no encontrado |
| 112–120 | Salida: explicar cada falla con vocabulario del modelo |

## Encuentro 2 — Sistema de archivos y terminal

Comandos esenciales:

```bash
pwd
ls -lah
cd
mkdir
cp
mv
rm
file
head
tail
less
man
```

Ideas que se evalúan:

- rutas absolutas y relativas;
- directorio actual y directorio personal;
- nombres con espacios;
- diferencia entre archivo de texto y archivo binario;
- expansión de comodines por el shell;
- lectura de ayuda antes de probar opciones al azar.

No se realizarán eliminaciones recursivas durante la primera práctica.

## Encuentro 3 — Flujos, búsqueda y composición

```bash
wc -l datos/*.csv
head -n 5 datos/mediciones.csv
grep -n "sospechosa" datos/mediciones.csv
cut -d, -f2 datos/mediciones.csv | sort | uniq -c
find . -type f -name "*.py"
```

Conceptos:

- entrada estándar, salida estándar y salida de error;
- redirección `>` y `>>`;
- tubería `|`;
- códigos de salida;
- variables y comillas;
- un script Bash pequeño con `set -euo pipefail`.

## Ejercicio integrador

Entregar un directorio con archivos de medición desordenados. El estudiante debe:

1. identificar los tipos de archivo;
2. contar registros y localizar valores marcados;
3. crear un resumen usando una tubería;
4. guardar los comandos en `resumir.sh`;
5. explicar qué parte hace cada programa de la tubería.

## Errores previsibles

| Error | Aprendizaje esperado |
|---|---|
| Confundir `/` con `\` | Las rutas dependen del entorno, no de Python |
| Ejecutar un archivo desde otro directorio | El proceso tiene un directorio de trabajo |
| Escribir rutas sin comillas | El shell separa argumentos antes de ejecutar el programa |
| Usar `>` cuando se quería anexar | La redirección puede reemplazar contenido |
| Copiar comandos destructivos sin leerlos | Todo comando debe interpretarse antes de ejecutarse |

## Salida individual

Sin ejecutar comandos, predecir el contenido de `resumen.txt` después de una
tubería dada y explicar en qué orden se ejecutan sus componentes.

