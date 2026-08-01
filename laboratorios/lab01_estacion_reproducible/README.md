# Laboratorio 1 — Estación científica reproducible

## Pregunta

¿Puede otra persona reconstruir qué archivos se procesaron y qué comandos
produjeron un resumen sin recibir instrucciones orales?

## IA

Nivel 1. Se permite documentación y ayuda de comandos; no se permite generación
automática de la solución.

## Tareas

1. Crear la estructura `datos/`, `scripts/`, `resultados/` y `README.md`.
2. Copiar a `datos/` un conjunto de archivos suministrado por el docente.
3. Usar Bash para identificar tipos, contar filas y localizar registros marcados.
4. Completar `resumir_mediciones.sh` para generar `resultados/resumen.txt`.
5. Inicializar Git y producir al menos tres commits coherentes.
6. Excluir resultados regenerables y archivos temporales mediante `.gitignore`.
7. Clonar o entregar el repositorio en un directorio limpio y ejecutar de nuevo.

## Criterios de aceptación

- El script funciona desde la raíz del proyecto.
- Las rutas no dependen del nombre del usuario.
- Repetir el script produce el mismo resumen.
- El README distingue requisitos, entrada, ejecución y salida.
- El historial permite identificar cuándo se agregó el script y cuándo se corrigió.

## Preguntas

1. ¿Qué información se perdería si solo se entregara `resumen.txt`?
2. ¿Qué archivos deben versionarse y cuáles pueden regenerarse?
3. ¿Por qué un commit no equivale a una copia de seguridad remota?

## Salida individual

Interpretar un `git status` y una tubería Bash suministrados por el docente.

