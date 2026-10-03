# Cronograma vigente — ajuste del 2 de octubre de 2026

Curso de Programación científica para Física. Encuentros martes, miércoles y jueves de 120 minutos; cierre el 19 de noviembre. Esta versión sustituye las fechas y cortes de la planeación del 30 de septiembre.

## Punto de partida y decisiones

- El registro de avance indica que el encuentro previsto para archivos del jueves anterior se dedicó a cerrar colecciones y funciones con `*args` y `**kwargs`; se registra como 24 de septiembre, fecha inferida del calendario, sin certificar asistencia.
- Los códigos de `2026-2/` muestran funciones, módulos/subpaquetes, puntos medios y lectura CSV con `pathlib`, `with` y excepciones. El avance de la semana 29 sep.–1 oct. se considera conjunto: los archivos no acreditan el día exacto ni el dominio individual. Véase [diagnóstico](ajuste_octubre_2026.md).
- Sesión 2: 6 oct., contratos y pruebas. El 7 oct. se realiza un [taller individual autogestionado de 120 minutos](../guias/taller_07_octubre_integracion/README.md) con nueve ejercicios independientes de análisis y corrección: ciclos, colecciones, recursividad, argumentos, paquetes, archivos, puntos medios, entorno y Git. Usa contenidos ya trabajados hasta el 1 oct., sin exigir las novedades del martes ni construir una aplicación completa. La sesión 3 de error numérico se traslada al 13 oct. (75 min), junto con instalación local (25 min), pregunta del proyecto (10 min) y cierre (10 min). Construir wheel y publicar en PyPI son extensiones, no requisitos evaluables.
- Quedan **cinco laboratorios: 2–6**. Se conserva el registro del lab. 1 y los pesos; no se presupone que los labs. 2 y 3 se hayan abierto en sus antiguas fechas.
- El jueves **8 de octubre** se dedica a iniciar el lab. 2. También habrá acompañamiento para los siguientes; una apertura no exige entrega el mismo día.
- **21 de octubre: parcial 2, sin clase. 12 de noviembre: parcial 3, sin clase. Exposiciones: 17–19 de noviembre.**
- Se propone entrega del proyecto el **lunes 16 de noviembre**, sin sesión adicional, para separar producto y parcial. Requisitos congelados el 5. La hora de recepción y los turnos individuales se anunciarán en clase.
- SQL/PostgreSQL, Docker, POO propia y SciPy permanecen como materiales opcionales. Se priorizan fundamentos, cómputo científico, tratamiento de datos, validación y comunicación; no se agregan herramientas obligatorias al final.

## Calendario

Las semanas 1–3 son registro de planeación, no certificación de ejecución. Las correcciones de septiembre se basan en el registro de avance.

| Semana | Martes | Miércoles | Jueves |
|---|---|---|---|
| 1 | **1 sep.** — Acta; inicio de sistema operativo | **2 sep.** — Sistema operativo, procesos y WSL2 | **3 sep.** — Terminal, rutas y ayuda |
| 2 | **8 sep.** — Bash: tuberías, scripts y permisos | **9 sep.** — Git y GitHub | **10 sep.** — Python: intérprete y entornos; entrega histórica lab. 1 |
| 3 | **15 sep.** — Tipos, operadores y E/S | **16 sep.** — Funciones y contratos | **17 sep.** — Parcial 1; registro de planeación original |
| 4 | **22 sep.** — Booleanos y condicionales | **23 sep.** — Ciclos, acumulación y colecciones | **24 sep.** — Cierre de colecciones y funciones con `*args` y `**kwargs` (registro de avance) |
| 5 | **29 sep.** — Biblioteca propia: módulos, subpaquetes e importaciones | **30 sep.** — Continuación del ejemplo de biblioteca; pruebas reprogramadas al 6 oct. | **1 oct.** — Sesión 1: archivos, validación, excepciones y sys.path; práctica de la guía 03 |
| 6 | **6 oct.** — Sesión 2: contratos, casos límite, pytest e instalación editable | **7 oct.** — Taller individual: ejercicios por tema, lectura/corrección de código e integración (120 min) | **8 oct.** — Taller de inicio del laboratorio 2: lectura y análisis con Python |
| 7 | **13 oct.** — Sesión 3: error y convergencia; instalación local y pregunta del proyecto | **14 oct.** — NumPy: arreglos, formas, tipos, indexación y vistas | **15 oct.** — NumPy: ejes, vectorización y azar; entrega lab. 2 y apertura lab. 3 |
| 8 | **20 oct.** — Matplotlib OO, unidades, leyendas y variabilidad; sin entrega | **21 oct.** — Parcial 2; sin clase; corte obligatorio del 13 oct. | **22 oct.** — Taller NumPy/Matplotlib e inicio acompañado del lab. 4 |
| 9 | **27 oct.** — Pandas: lectura, selección y auditoría; entrega lab. 3 | **28 oct.** — Pandas: tipos, faltantes, duplicados y unidades; propuesta del proyecto | **29 oct.** — Taller de limpieza e inicio del lab. 5; agrupación simple guiada |
| 10 | **3 nov.** — Integración y auditoría reproducible; entrega lab. 4 y apertura lab. 6 | **4 nov.** — Pandas: combinación con claves y validación; crítica de IA sobre código propio | **5 nov.** — Clínica de proyecto y verificación científica; congelamiento de requisitos |
| 11 | **10 nov.** — Repaso y ejecución limpia; entrega lab. 5 | **11 nov.** — Ensayo y consultas; entrega breve lab. 6, sin contenido nuevo | **12 nov.** — Parcial 3; sin clase ni entrega de proyecto |
| 12 | **17 nov.** — Exposiciones I | **18 nov.** — Exposiciones II | **19 nov.** — Exposiciones III y cierre |

## Cinco laboratorios pendientes

| Lab. | Inicio | Entrega | Prerrequisitos | Dedicación estimada por estudiante |
|---|---|---|---|---|
| [1](../laboratorios/lab01_estacion_reproducible/README.md) | 10 sep. | 10 sep. | Linux, Bash y Git | histórico |
| [2](../laboratorios/lab02_python_nativo/README.md) | 8 oct. | 15 oct. | Python, funciones, archivos y validación | 2 h acompañadas + 3–4 h autónomas |
| [3](../laboratorios/lab03_modelo_verificable/README.md) | 15 oct. | 27 oct. | Puntos medios, pytest, módulos e instalación local (13 oct.) | 4–5 h autónomas |
| [4](../laboratorios/lab04_numpy_matplotlib/README.md) | 22 oct. | 3 nov. | NumPy, azar y Matplotlib (20 oct.) | 2 h acompañadas + 3–4 h autónomas |
| [5](../laboratorios/lab05_pandas/README.md) | 29 oct. | 10 nov. | Pandas: lectura y limpieza (28 oct.) | 75 min acompañados + 3–4 h autónomas |
| [6](../laboratorios/lab06_integracion_cientifica/README.md) | 3 nov. | 11 nov. | Validación y ejecución limpia; trabajo previo | 45 min acompañados + 1,5–2 h autónomas |

Cada laboratorio pesa 3,5 %. Código e informe se suben a GitHub; las guías precisan resultados, pruebas y evidencia individual. El tiempo incluye informe y video. Se admiten parejas; la estimación es dedicación por persona, no suma de horas de dos integrantes. Las ventanas permiten distribuir trabajo; no se exige trabajar todos los días. No hay entrega el día de un parcial. El lab. 6 reutiliza un trabajo previo para no convertirse en otro proyecto.

Si un prerrequisito no se practica, se reduce el alcance o se desplaza la actividad. Las recuperaciones no suplen prerrequisitos obligatorios.

## Cortes evaluables

| Hito | Fecha | Corte y alcance | Exclusiones |
|---|---|---|---|
| Parcial 1 | Registro original: 17 sep. | Se conserva el alcance previamente anunciado y el acta institucional | Sin cambios retroactivos |
| Parcial 2 | 21 oct. | Hasta 13 oct.: Python, colecciones, funciones, args/kwargs, módulos, archivos, excepciones, contratos, pruebas, puntos medios, error y concepto de instalación local | NumPy desde el 14, Matplotlib, Pandas; memorizar metadatos de empaquetado; wheel/PyPI y extensiones |
| Parcial 3 | 12 nov. | Hasta 5 nov.: fundamentos aplicados, NumPy, Matplotlib, Pandas con limpieza, agrupación y combinación practicadas, validación y reproducibilidad | Temas opcionales, APIs no practicadas y novedades posteriores al corte |
| Proyecto | 16 nov. | Alcance aprobado y requisitos congelados el 5 nov. | SQL, Docker, POO, SciPy y recuperaciones no son requisitos |

Los cortes son explícitos: el parcial 2 termina el martes 13, antes de NumPy, y el parcial 3 el jueves 5. La evaluación solo incluye contenidos efectivamente practicados dentro del corte; no se presupone una separación fija de tres semanas entre exámenes.

## Proyecto y carga

- 13 oct.: elección de pregunta y fuente/modelo (breve, en clase).
- 28 oct.: propuesta y criterio de validación; retroalimentación de alcance antes del 5 nov.
- 5 nov.: demostración mínima, primera ejecución y congelamiento de requisitos.
- 16 nov.: subir código e informe definitivos a GitHub e identificar commit evaluable.
- 17–19 nov.: exposiciones y comprobación individual; después de la entrega solo cambios solicitados en la defensa.

Las ventanas de labs. 3–5 se superponen parcialmente, pero sus entregas están separadas. El lab. 3 no exige trabajar el 20–21 oct.; el lab. 6 es una auditoría corta que puede completarse antes del 10 nov. El 10–11 nov. no introduce materia nueva. Se mantienen 21 % de laboratorios, 54 % de parciales y 25 % de proyecto.

## Ocho clases de recuperación en los dos primeros meses

Esta tabla conserva las ventanas previstas, no acredita realización. No se añade
una deuda de ocho sesiones al tramo final; las pendientes siguen siendo complementarias.
Las recuperaciones se habían previsto en **septiembre y octubre**, en el primer espacio
adicional disponible dentro de la ventana indicada. No tienen una fecha exacta
en el cronograma regular y no reemplazan encuentros. Cada una posee una demo y
una práctica en [`../recuperaciones/README.md`](../recuperaciones/README.md).

| Recuperación | Ventana | Tema diferente de la ruta regular | Producto breve |
|---:|---|---|---|
| 1 | Septiembre, después de la introducción a Python | SymPy: expresiones, sustitución y derivación simbólica | Verificación simbólica de una relación física |
| 2 | Septiembre, después de colecciones | NetworkX: grafos, caminos y conectividad | Grafo pequeño de una red física |
| 3 | Septiembre, después de funciones y ciclos | SimPy I: eventos, procesos y reloj simulado | Secuencia reproducible de eventos |
| 4 | Septiembre, después de la recuperación 3 | SimPy II: recursos, colas y tiempos de espera | Comparación de dos capacidades |
| 5 | Octubre, después de NumPy básico | xarray: dimensiones y coordenadas etiquetadas | Campo pequeño con selección por coordenadas |
| 6 | Octubre, después de NumPy básico | scikit-image: imagen como arreglo, umbral y medición | Segmentación elemental de una imagen sintética |
| 7 | Octubre, después de NumPy y funciones | scikit-learn I: regresión y separación de datos | Predicción con error de prueba |
| 8 | Octubre, después de la recuperación 7 | scikit-learn II: escalado, clasificación y matriz de confusión | Evaluación de un clasificador pequeño |

SymPy, NetworkX, SimPy, xarray, scikit-image y scikit-learn no se desarrollan en
las clases regulares. Las recuperaciones son complementarias y no amplían el
alcance de parciales, laboratorios ni proyecto.
