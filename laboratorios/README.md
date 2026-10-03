# Laboratorios del curso

Los seis laboratorios forman una secuencia acumulativa. Cada carpeta contiene un
enunciado y, solo cuando hace falta, datos de entrada. No se suministran
plantillas de informe, esqueletos de código ni archivos parcialmente resueltos:
cada equipo debe decidir cómo organizar su solución y justificarla.

## Calendario vigente

Quedan cinco laboratorios (2–6). El lab. 1 conserva su registro histórico y no se reabre. Los inicios acompañados ocupan clase; el resto se termina de forma autónoma. Fechas de 2026; hora de recepción anunciada por el docente.

| Lab. | Inicio | Entrega | Prerrequisitos | Dedicación estimada por estudiante |
|---|---|---|---|---|
| [1](lab01_estacion_reproducible/README.md) | 10 sep. | 10 sep. | Linux, Bash y Git | histórico |
| [2](lab02_python_nativo/README.md) | 8 oct. | 15 oct. | Python, funciones, archivos y validación | 2 h acompañadas + 3–4 h autónomas |
| [3](lab03_modelo_verificable/README.md) | 15 oct. | 27 oct. | Puntos medios, pytest, módulos e instalación local (13 oct.) | 4–5 h autónomas |
| [4](lab04_numpy_matplotlib/README.md) | 22 oct. | 3 nov. | NumPy, azar y Matplotlib (20 oct.) | 2 h acompañadas + 3–4 h autónomas |
| [5](lab05_pandas/README.md) | 29 oct. | 10 nov. | Pandas: lectura y limpieza (28 oct.) | 75 min acompañados + 3–4 h autónomas |
| [6](lab06_integracion_cientifica/README.md) | 3 nov. | 11 nov. | Validación y ejecución limpia; trabajo previo | 45 min acompañados + 1,5–2 h autónomas |

Cada laboratorio vale 3,5 %. Los tiempos incluyen código, comprobaciones, informe y video; son estimaciones por estudiante. Si falta un prerrequisito, se reduce el alcance o se mueve la actividad. No se exige PyPI, wheel, SQL, Docker ni métodos de recuperaciones. El lab. 6 audita un laboratorio previo con evidencia nueva; no exige otro proyecto.

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
- El trabajo combina inicio acompañado y desarrollo autónomo según el calendario.
- Cada laboratorio finaliza con una comprobación individual sin IA.

## Entrega común

Cada equipo debe **subir el código y el informe a GitHub**, en un repositorio propio que contenga también los datos
permitidos, los resultados y una explicación escrita en Markdown o PDF. No hay
una estructura predeterminada: el documento debe permitir comprender la pregunta,
el procedimiento, las decisiones, las comprobaciones, los resultados y las
limitaciones sin depender de una explicación oral.

Se entrega la URL del repositorio y el identificador del commit evaluable. El README enlaza el informe (Markdown o PDF), explica instalación y ejecución, y permite localizar datos, resultados, pruebas y video. Un repositorio privado es válido si el docente tiene acceso. No basta un archivo ZIP, una captura o un enlace al video. No subir entornos virtuales, cachés ni credenciales. Verificar que los resultados solicitados no quedaron excluidos por `.gitignore`.

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
