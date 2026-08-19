# Laboratorios del curso

Los seis laboratorios forman una secuencia acumulativa. Cada carpeta contiene una
guía, archivos iniciales y un `README.md`. Las soluciones, datos de contingencia y
claves de calificación se mantienen en `_docente_privado/`.

## Sincronización con las clases

`Cierre de prerrequisitos` es el último encuentro que puede introducir una
técnica exigida. Entre ese cierre y el laboratorio hay al menos un encuentro de
práctica o integración sin requisito nuevo.

| Lab. | Fecha | Cierre de prerrequisitos | Encuentro intermedio | Tema | Peso |
|---:|---|---|---|---|---:|
| 1 | Jueves 3 sep. | Martes 1 sep. | Miércoles 2 sep.: taller | WSL2 documentado, Bash, Git y GitHub | 3,5 % |
| 2 | Jueves 24 sep. | Martes 22 sep. | Miércoles 23 sep.: práctica | Python nativo y datos físicos | 3,5 % |
| 3 | Martes 6 oct. | Miércoles 30 sep. | Jueves 1 oct.: parcial | Modelo modular, algoritmo suministrado y pruebas | 3,5 % |
| 4 | Jueves 15 oct. | Martes 13 oct. | Miércoles 14 oct.: práctica | NumPy, simulación y Matplotlib OO | 3,5 % |
| 5 | Jueves 29 oct. | Martes 27 oct. | Miércoles 28 oct.: práctica | Pandas y datos imperfectos | 3,5 % |
| 6 | Martes 10 nov. | Miércoles 4 nov. | Jueves 5 nov.: integración | PostgreSQL, Python y Docker | 3,5 % |

Si una clase necesaria no se alcanza a realizar, el laboratorio correspondiente
se simplifica o se mueve; no se deja el tema como aprendizaje autónomo obligatorio.

## Forma de trabajo

- Equipos de máximo dos estudiantes, salvo indicación institucional distinta.
- Roles de conductor y revisor rotan durante la sesión.
- Cada estudiante conserva un registro individual de predicciones, decisiones y
  errores encontrados.
- La programación principal ocurre durante la sesión; la documentación puede
  terminarse en el plazo anunciado por el docente.
- Cada laboratorio finaliza con una comprobación individual sin IA.

## Entregables

El laboratorio 1 tiene una entrega corta en Markdown y repositorio; no exige
informe científico PDF. Los laboratorios 2–6 entregan un PDF de 4–7 páginas sin
contar anexos, acompañado del repositorio, salvo ajuste explícito en su guía. La
estructura para esos informes está en
[`plantilla_informe.md`](plantilla_informe.md).

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

En el laboratorio 1, “resultados” significa evidencias textuales y “validación”
significa comprobar entorno, redirecciones, ejecución del script y estado de Git.
Una entrega que no ejecuta desde las instrucciones o carece de datos identificables
no obtiene los puntos de reproducibilidad ni validación.

## Convención de archivos entregados

```text
labNN_apellido1_apellido2/
├── README.md
├── informe.pdf              # laboratorios 2–6
├── datos/
│   ├── raw/
│   └── processed/
├── src/
├── tests/
├── resultados/
├── requirements.txt         # si aplica
└── AI_USAGE.md              # cuando la guía autorice IA
```

Cada guía especifica qué elementos son obligatorios.
