# Laboratorios del curso

El ajuste del **22 de octubre de 2026** reduce la secuencia a cuatro laboratorios. Los laboratorios 1 y 2 conservan sus guías y registro; los nuevos 3 y 4 sustituyen cuatro entregas anteriores. Cada equipo organiza su solución desde cero, sin plantillas resueltas.

## Calendario vigente

Fechas de 2026; hora de recepción anunciada en clase.

| Lab. | Origen | Inicio | Entrega | Dedicación por estudiante |
|---|---|---|---|---|
| [1](lab01_estacion_reproducible/README.md) | Sin cambios | 10 sep. | 10 sep. | Histórico |
| [2](lab02_python_nativo/README.md) | Sin cambios | 8 oct. | 15 oct. | Según guía original |
| [3](lab03_modelo_verificable/README.md) | Antiguos 3 + 4 | **22 oct.** | **5 nov.** | 6–7 h totales, incluidas 2 h acompañadas |
| [4](lab04_pandas_auditoria/README.md) | Antiguos 5 + 6 | **5 nov.** | **19 nov.** | 6–7 h totales, incluidos 45 min acompañados |

La dificultad se concentra en decisiones, validación e interpretación; no se suman todos los ejercicios de las guías anteriores. El lab. 3 estudia un único sistema de dos sensores con dos configuraciones: refuerza sistemas lineales, autovalores, QR, SVD, vectorización y estadísticas. Sustituye puntos medios, caminatas y empaquetado para mantener 6–7 horas. El lab. 4 audita su propio análisis de Pandas. Ambos tienen un solo informe, sin video ni sustentación oral. QR, SVD y autovalores se aplican con NumPy a matrices 2 × 2, con apoyo conceptual, sin implementar los algoritmos. No se exige PyPI, wheel, SQL ni Docker.

Para conservar el **21 % que figura en la evaluación del repositorio**, los pesos de las actividades fusionadas se suman: lab. 1 y lab. 2, 3,5 % cada uno; nuevos labs. 3 y 4, 7 % cada uno. Prevalece el acta institucional; este ajuste no modifica el peso total de laboratorios ni los demás componentes.

## Rúbrica de los laboratorios integrados 3 y 4

| Dimensión | Puntos |
|---|---:|
| Comprensión, fundamento y predicciones | 10 |
| Código y cumplimiento técnico | 25 |
| Resultados y evidencia | 15 |
| Validación, pruebas y tratamiento del error | 20 |
| Informe, decisiones y limitaciones | 15 |
| Reproducibilidad y Git | 10 |
| Evidencia individual escrita | 5 |
| **Total** | **100** |

Se entrega URL del repositorio y commit evaluable, código, informe Markdown o PDF, resultados y pruebas. El README explica cómo reproducirlo. Cada integrante aporta una nota escrita propia conforme a su guía; no se añade una comprobación oral o presencial. En repositorios privados, habilitar acceso de revisión. No subir entornos, cachés, credenciales ni datos personales innecesarios.

## Reglas conservadas para los laboratorios 1 y 2

**Las secciones siguientes conservan los requisitos originales de los laboratorios 1 y 2. No añaden video, sustentación ni otra evidencia presencial a los nuevos laboratorios 3 y 4.**

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

Se entrega la URL del repositorio y el identificador del commit evaluable. El README enlaza el informe (Markdown o PDF), explica instalación y ejecución, y permite localizar datos, resultados, pruebas y video. Un repositorio privado es válido si permite el acceso para su revisión. No basta un archivo ZIP, una captura o un enlace al video. No subir entornos virtuales, cachés ni credenciales. Verificar que los resultados solicitados no quedaron excluidos por `.gitignore`.

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
