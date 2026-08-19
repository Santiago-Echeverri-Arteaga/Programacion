# Borrador de sílabo — Programación

Este documento contiene la redacción académica propuesta. Debe trasladarse al
formato institucional vigente después de confirmar créditos, horas de trabajo
independiente y demás campos administrativos.

## 1. Identificación

| Campo | Valor propuesto o por confirmar |
|---|---|
| Programa | Física |
| Espacio académico | Programación |
| Código | 120710206 |
| Modalidad | Presencial |
| Naturaleza | Teórico-práctica |
| Créditos | 3 — confirmar equivalencia horaria institucional |
| Docencia directa | 6 horas semanales |
| Duración | Una clase realizada antes de la interrupción y 13 semanas de reanudación, del 25 de agosto al 19 de noviembre de 2026 |
| Requisito | Ecuaciones diferenciales — confirmar con el plan vigente |
| Habilitable, validable y homologable | Confirmar con el programa |

### Revisión administrativa pendiente

El documento anterior declara 196 horas y simultáneamente 6 horas semanales de
docencia y 6 de trabajo independiente. La interrupción extraordinaria obliga a
recalcular las horas efectivamente programadas para las 13 semanas confirmadas.
La versión final no debe conservar cifras incompatibles; el cálculo
debe validarse con la definición institucional de crédito académico.

## 2. Descripción

La asignatura introduce la programación como herramienta de razonamiento y
trabajo científico. Mediante Python, Linux, Git y bibliotecas del ecosistema
científico, el estudiante aprende a traducir problemas físicos a procedimientos
computacionales, leer y escribir código, procesar datos, producir visualizaciones,
depurar, probar y validar resultados. El curso incorpora prácticas de
reproducibilidad, una introducción a PostgreSQL y Docker, y formación explícita
para evaluar críticamente la asistencia de inteligencia artificial.

El énfasis se encuentra en fundamentos transferibles. Los temas avanzados se
seleccionan por su utilidad para la física y la ciencia de datos, evitando cubrir
superficialmente aprendizaje automático, concurrencia u otras áreas que requieren
cursos posteriores.

## 3. Justificación

La computación forma parte de la práctica contemporánea de la física junto con la
teoría y el experimento. Un físico debe poder transformar modelos en código,
trabajar con datos, comparar resultados con casos conocidos, cuantificar errores y
comunicar evidencia. Estas competencias también permiten transitar hacia ciencia
de datos, investigación interdisciplinaria y desarrollo de software científico.

El acceso generalizado a herramientas de IA aumenta la necesidad de que el
estudiante construya competencia autónoma. Por ello, la asignatura combina
evaluaciones individuales protegidas con actividades abiertas donde la IA puede
ser estudiada, auditada y declarada sin reemplazar la responsabilidad humana.

## 4. Unidad de competencia

El estudiante formula y resuelve problemas computacionales relacionados con
fenómenos físicos y datos científicos, seleccionando estructuras, algoritmos y
herramientas pertinentes, y comunicando resultados reproducibles, validados y
éticamente sustentados.

## 5. Resultados de aprendizaje

Se adoptan los resultados definidos en
[`resultados_aprendizaje.md`](resultados_aprendizaje.md). En el formato
institucional pueden agruparse así:

1. Opera un entorno Linux y gestiona versiones para desarrollar trabajo
   computacional reproducible.
2. Diseña, lee, depura y prueba programas en Python para resolver problemas de
   complejidad introductoria.
3. Traduce modelos o preguntas físicas a algoritmos y valida los resultados con
   criterios numéricos, físicos y dimensionales.
4. Procesa y representa arreglos y datos tabulares con herramientas científicas
   apropiadas.
5. Organiza y defiende un proyecto computacional, documentando datos,
   dependencias, decisiones y asistencia de IA.

## 6. Enseñanzas

### Unidad 1 — Entorno computacional y reproducibilidad, clase realizada y 25 de agosto–3 de septiembre

- Componentes funcionales del computador.
- Sistema operativo, procesos y sistema de archivos.
- Linux y Bash: navegación, búsqueda, flujos, tuberías y scripts.
- Git y GitHub: estados, commits, remotos y publicación básica.
- Organización reproducible de un proyecto científico.

### Unidad 2 — Fundamentos de programación, 8 de septiembre–6 de octubre

- Intérprete, scripts, notebooks y entornos virtuales.
- Tipos, operadores, variables, entrada y salida.
- Funciones, contratos, alcance, argumentos y documentación.
- Booleanos, condicionales, ciclos y patrones de acumulación.
- Cadenas y colecciones.
- Archivos, rutas, excepciones, depuración, módulos y dependencias.
- Pruebas, casos límite, algoritmos elementales y error numérico.

### Unidad 3 — Cómputo científico, 7–15 de octubre

- NumPy: arreglos, formas, tipos, indexación, vistas, broadcasting y
  vectorización.
- Aleatoriedad reproducible.
- Matplotlib mediante interfaz orientada a objetos.
- Validación, convergencia, error e interpretación física.

Clases y objetos, herencia, SciPy y SymPy permanecen como extensiones de consulta
y no se evalúan en los parciales del calendario reducido.

### Unidad 4 — Datos, servicios y práctica responsable, 20 de octubre–10 de noviembre

- Lectura de datos con Python nativo, NumPy y Pandas.
- Selección, tipos, faltantes, duplicados, agrupación y combinación.
- Incertidumbre, procedencia y comunicación científica.
- Uso crítico de IA y agentes de programación.
- PostgreSQL: modelo relacional y SQL puro.
- Conexión local y remota desde Python.
- Docker: imágenes, contenedores, redes, volúmenes y reproducibilidad.
- Integración en un flujo científico pequeño.

### Unidad 5 — Integración y comunicación, 11–19 de noviembre

- Demostración y sustentación de proyecto.
- Discusión de límites, validación y reproducibilidad.

## 7. Metodología

La asignatura combina explicaciones breves, programación en vivo, predicción de
resultados, práctica guiada, trabajo en parejas, laboratorios y un proyecto
aplicado. Una sesión típica alterna bloques de explicación de 15 a 25 minutos con
actividades donde los estudiantes deben escribir, ejecutar, depurar o explicar
código.

Los notebooks se usan para exploración y comunicación; los componentes
reutilizables se desarrollan en archivos Python y se prueban por separado. Git se
usa durante todo el semestre, no únicamente como tema inicial.

Se programan seis laboratorios acumulativos. Antes de cada laboratorio se cierra
el contenido requerido y se reserva al menos un encuentro completo para práctica,
integración o evaluación. La última semana, del 17 al 19 de noviembre, se dedica
completa a sustentaciones y no introduce contenidos ni entregables nuevos.

El proyecto se desarrolla mediante propuesta, aprobación de alcance, demostración
mínima, congelamiento de código y sustentación. Los proyectos pueden ser
individuales o en parejas, pero la autenticación y parte de la nota son
individuales.

## 8. Evaluación

Se adopta el sistema descrito en [`evaluacion.md`](evaluacion.md):

- tres parciales escritos de 18 % cada uno;
- seis laboratorios de 3,5 % cada uno;
- proyecto final de 25 %, distribuido entre producto (12 %), sustentación y
  modificación explicada (8 %), y reproducibilidad, Git y declaración de IA (5 %).

Los parciales se realizan en papel. Las hojas de
referencia suministradas por el docente reducen la dependencia de memorización de
APIs y permiten evaluar trazado, diagnóstico, diseño, pruebas e interpretación.
Cada parcial incluye como máximo lo visto el jueves de la semana anterior y
excluye los temas del martes y miércoles de la semana del examen, como se detalla
en [`cronograma.md`](cronograma.md).

La rúbrica del proyecto se encuentra en
[`rubrica_proyecto_final.md`](rubrica_proyecto_final.md).

## 9. Inteligencia artificial

El uso se rige por [`politica_ia.md`](politica_ia.md). Las evaluaciones protegidas
no admiten IA ni autocompletado generativo. Las actividades autorizadas exigen
declaración, revisión y evidencia independiente. Se enseña formalmente el trabajo
con IA y agentes después de que el estudiante haya desarrollado competencias de
prueba, depuración y análisis de datos.

## 10. Procesos integrativos

Los problemas y proyectos podrán vincularse con laboratorios, semilleros y grupos
de investigación del programa, siempre que se mantenga un alcance compatible con
un curso introductorio y se protejan datos, propiedad intelectual y evaluación
individual.

Se recomienda que asignaturas posteriores exijan nuevamente scripts, pruebas,
figuras reproducibles y control de versiones. Una sola asignatura no puede
consolidar por sí misma toda la competencia computacional del físico.

## 11. Bibliografía básica

1. Allen B. Downey. *Think Python*, tercera edición. Green Tea Press.
   <https://greenteapress.com/wp/think-python-3rd-edition/>
2. Jesse M. Kinder y Philip Nelson. *A Student's Guide to Python for Physical
   Modeling*, segunda edición. Princeton University Press, 2021.
3. Wes McKinney. *Python for Data Analysis*, tercera edición. O'Reilly, 2022;
   edición web abierta: <https://wesmckinney.com/book/>
4. Damien Irving et al. *Research Software Engineering with Python*.
   <https://merely-useful.tech/py-rse/>
5. The Carpentries. Lecciones de Shell, Git y Python.
   <https://software-carpentry.org/lessons/>

## 12. Documentación técnica de consulta

- <https://docs.python.org/3/>
- <https://numpy.org/doc/stable/>
- <https://docs.scipy.org/doc/scipy/>
- <https://docs.sympy.org/latest/>
- <https://pandas.pydata.org/docs/>
- <https://matplotlib.org/stable/>
- <https://www.postgresql.org/docs/current/>
- <https://docs.docker.com/>

## 13. Historial propuesto

- Borrador de rediseño integral: 2026-II.
- Próxima revisión: al cierre del primer semestre de implementación.
