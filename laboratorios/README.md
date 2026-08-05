# Laboratorios del curso

Los seis laboratorios forman una secuencia acumulativa. Cada carpeta contiene una
guía tradicional completa, archivos iniciales y un `README.md` que explica su
contenido. Las soluciones, datos de contingencia y claves de calificación se
mantienen en `_docente_privado/`.

| Lab. | Semana | Tema | Modalidad de IA | Peso |
|---:|---:|---|---|---:|
| 1 | 2 | Linux, Bash, Git y reproducibilidad | Nivel 1 | 3,5 % |
| 2 | 5 | Python nativo y datos físicos | Nivel 1 | 3,5 % |
| 3 | 8 | Modelo modular y verificable | Nivel 1 | 3,5 % |
| 4 | 10 | NumPy, simulación y Matplotlib OO | Nivel 1 | 3,5 % |
| 5 | 13 | Pandas y datos imperfectos | Nivel 1 | 3,5 % |
| 6 | 15 | PostgreSQL, Python y Docker | Nivel 2 declarado | 3,5 % |

Los laboratorios 1–2, 3–4 y 5–6 aportan respectivamente 7 % a los tres primeros
cortes. Consulte [`../programa/evaluacion.md`](../programa/evaluacion.md).

## Forma de trabajo

- Equipos de máximo dos estudiantes, salvo indicación institucional distinta.
- Roles de conductor y revisor rotan durante la sesión.
- Cada estudiante conserva un cuaderno o registro individual de predicciones,
  decisiones y errores encontrados.
- La programación principal ocurre durante la sesión; el informe puede terminarse
  en el plazo anunciado por el docente.
- Cada laboratorio finaliza con una comprobación individual sin IA.

## Informe tradicional

Salvo que la guía indique algo adicional, se entrega un PDF de 4–7 páginas sin
contar anexos, acompañado del repositorio. La estructura obligatoria está en
[`plantilla_informe.md`](plantilla_informe.md): portada, resumen, objetivos, marco
teórico, metodología, resultados, discusión, conclusiones, referencias y anexos.
El código no se pega completo en el cuerpo: se citan módulos, funciones, versión
de Git y figuras relevantes.

## Rúbrica común de cada laboratorio

| Dimensión | Puntos |
|---|---:|
| Pregunta, fundamento y predicciones | 10 |
| Procedimiento, código y cumplimiento técnico | 25 |
| Resultados y calidad de figuras/tablas | 15 |
| Validación, pruebas y tratamiento del error | 20 |
| Discusión física o algorítmica | 15 |
| Reproducibilidad, Git y documentación | 10 |
| Evidencia individual | 5 |
| **Total** | **100** |

Una entrega que no ejecuta desde las instrucciones presentadas o carece de datos
identificables no puede obtener los puntos de reproducibilidad ni validación.
La rúbrica puede particularizarse en cada guía sin cambiar el total.

## Convención de archivos entregados

```text
labNN_apellido1_apellido2/
├── README.md
├── informe.pdf
├── datos/
│   ├── raw/                 # originales inmutables
│   └── processed/           # si aplica
├── src/                     # .py, .sh o .sql
├── tests/                   # comprobaciones automatizadas
├── resultados/              # tablas y figuras finales
├── requirements.txt         # si aplica
└── AI_USAGE.md              # solo cuando la guía autorice IA
```

Cada guía especifica qué elementos de esta estructura son obligatorios.
