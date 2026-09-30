# Laboratorios del curso

Los seis laboratorios forman una secuencia acumulativa. Cada carpeta contiene un
enunciado y, solo cuando hace falta, datos de entrada. No se suministran
plantillas de informe, esqueletos de código ni archivos parcialmente resueltos:
cada equipo debe decidir cómo organizar su solución y justificarla.

## Aperturas, entregas y sincronización

Los laboratorios son tareas fuera de la clase regular. Apertura significa que
ya se practicaron los prerrequisitos; entrega es una fecha posterior. La hora y
el canal los anuncia el docente. El laboratorio 1 conserva su registro histórico.

| Lab. | Apertura después de clase | Entrega | Prerrequisitos practicados | Trabajo estimado | Peso |
|---:|---|---|---|---|---:|
| [1](lab01_estacion_reproducible/README.md) | 10 sep. | 10 sep. | Linux, Bash y Git | histórico | 3,5 % |
| [2](lab02_python_nativo/README.md) | 1 oct. | 13 oct. | Python nativo, archivos, rutas y excepciones | 3 h | 3,5 % |
| [3](lab03_modelo_verificable/README.md) | 7 oct. | 20 oct. | Módulos, pytest, puntos medios y pip/build | 4 h | 3,5 % |
| [4](lab04_numpy_matplotlib/README.md) | 20 oct. | 3 nov. | NumPy, vectorización, azar y Matplotlib OO | 4 h | 3,5 % |
| [5](lab05_pandas/README.md) | 22 oct. | 5 nov. | Pandas: lectura, selección, auditoría y limpieza | 4 h | 3,5 % |
| [6](lab06_integracion_cientifica/README.md) | 28 oct. | 10 nov. | Integración, trazabilidad, pruebas y ejecución limpia | 3 h | 3,5 % |

El trabajo estimado incluye código, validación, informe, video y comprobación
individual; se puede distribuir entre varios días. Si falta una clase necesaria,
se simplifica o mueve la tarea. No se exigen temas futuros ni de recuperaciones.
Lab. 2: sin pytest/empaquetado. Lab. 3: instalación local, sin publicación ni
Euler-Cromer. Lab. 4 y 5: sin agrupaciones/uniones futuras obligatorias. Lab. 6:
sin SQL/Docker ni requisitos nuevos del proyecto. Ver [cronograma](../programa/cronograma.md).

## Estructura común de las guías

Cada enunciado presenta:

- teoría breve limitada a lo necesario para comprender el problema;
- objetivos observables;
- requerimientos y restricciones acordes con lo visto hasta ese momento;
- un procedimiento que define el problema sin dictar la arquitectura del código;
- resultados puntuales que deben obtenerse y comprobarse;
- preguntas que deben responderse por escrito;
- una explicación en video breve.

La ausencia de plantilla es intencional. La organización de carpetas, nombres de
funciones, tablas y narración forman parte de las decisiones que el equipo debe
pensar y explicar.

## Forma de trabajo

- Equipos de máximo dos estudiantes, salvo indicación institucional distinta.
- Roles de conductor y revisor rotan durante la sesión.
- Cada estudiante conserva un registro individual de predicciones, decisiones y
  errores encontrados.
- El trabajo se desarrolla fuera del encuentro magistral, con el tiempo y los
  canales de acompañamiento anunciados por el docente.
- Cada laboratorio finaliza con una comprobación individual sin IA.

## Entrega común

Cada equipo entrega un repositorio propio que contenga el código, los datos
permitidos, los resultados y una explicación escrita en Markdown o PDF. No hay
una estructura predeterminada: el documento debe permitir comprender la pregunta,
el procedimiento, las decisiones, las comprobaciones, los resultados y las
limitaciones sin depender de una explicación oral.

Además se entrega un enlace a un video de **3 a 5 minutos en YouTube**, público o
no listado. Deben participar las dos personas del equipo mediante voz o
explicación de pantalla; no es obligatorio mostrar el rostro. El video debe:

1. presentar la pregunta y la estrategia elegida;
2. ejecutar o mostrar la parte principal del trabajo;
3. señalar un resultado concreto y una comprobación;
4. explicar una decisión o dificultad con palabras propias.

No se acepta un video que solo lea el informe ni un enlace que requiera permiso
individual para visualizarse. No deben aparecer contraseñas, tokens ni datos
personales innecesarios.

## Rúbrica común de cada laboratorio

| Dimensión | Puntos |
|---|---:|
| Comprensión, fundamento y predicciones | 10 |
| Procedimiento, código y cumplimiento técnico | 25 |
| Resultados solicitados y calidad de la evidencia | 15 |
| Validación, pruebas y tratamiento del error | 20 |
| Explicación escrita y discusión | 10 |
| Reproducibilidad y Git | 10 |
| Video breve | 5 |
| Evidencia individual | 5 |
| **Total** | **100** |

Una entrega que no ejecuta desde sus propias instrucciones o no contiene los
resultados puntuales solicitados pierde los puntos de reproducibilidad o
resultados, según corresponda.
