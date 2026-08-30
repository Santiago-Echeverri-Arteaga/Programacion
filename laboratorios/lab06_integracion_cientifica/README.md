# Laboratorio 6 — Análisis científico integrado

| Campo | Especificación |
|---|---|
| Fecha de realización/entrega | Jueves 5 de noviembre de 2026 |
| Modalidad | Tarea; no reemplaza la clase regular de ese día |
| Tiempo estimado | 120 minutos |
| Trabajo | Parejas con comprobación individual |
| Herramientas | Python, NumPy, Pandas, Matplotlib, `pytest` y Git |

## Teoría breve

Un flujo reproducible separa entrada, validación, transformación, análisis y
comunicación. Python nativo es adecuado para control y organización; NumPy para
arreglos y operaciones numéricas; Pandas para tablas; Matplotlib para figuras.
Usar más bibliotecas no mejora un análisis si no se justifica su función. Una
ejecución limpia debe reconstruir los resultados sin pasos manuales ocultos.

## Objetivos

- elegir de forma razonada entre Python nativo, NumPy y Pandas;
- construir un flujo completo con datos, validación, resultado y figura;
- comprobar al menos un resultado por un método independiente;
- ejecutar el trabajo desde cero y registrar su versión con Git;
- explicar las decisiones y limitaciones del análisis.

## Requerimientos y límites

- elegir uno de los conjuntos de datos del curso que no haya sido el centro del
  laboratorio 5, o un subconjunto nuevo autorizado por el docente;
- formular una pregunta pequeña que pueda responderse en la sesión;
- usar al menos dos de estas herramientas cuando su uso sea justificable:
  Python nativo, NumPy, Pandas y Matplotlib;
- crear archivos, funciones, pruebas y organización desde cero;
- no usar SciPy, SimPy, scikit-learn, PostgreSQL, Docker ni temas vistos solo en
  recuperaciones;
- no convertir esta actividad en un requisito nuevo del proyecto final.

## Procedimiento

1. Formulen una pregunta que exija seleccionar o transformar datos y producir
   una comparación cuantitativa alcanzable.
2. Identifiquen entradas, unidades, supuestos, problemas de calidad y resultado
   esperado antes de programar.
3. Decidan qué trabajo corresponde a Python nativo, NumPy o Pandas. Expliquen por
   qué una biblioteca elegida aporta algo necesario.
4. Implementen lectura, validación, transformación y análisis en partes que puedan
   comprobarse por separado.
5. Produzcan una tabla resumen y una figura científica relacionadas directamente
   con la pregunta.
6. Verifiquen manualmente un subconjunto pequeño y escriban pruebas para dos
   propiedades o casos límite del flujo.
7. Registren versiones de dependencias y creen un punto identificable en Git.
8. Prueben la ejecución desde un entorno limpio o una copia nueva del repositorio,
   usando solamente la explicación escrita.

## Resultados puntuales que deben obtener

1. pregunta, entradas, unidades y criterio de respuesta claramente identificados;
2. conteos de datos recibidos, aceptados y rechazados o transformados;
3. tabla resumen con al menos una comparación cuantitativa;
4. figura exportada con etiquetas, unidades y pie explicativo;
5. verificación manual de un subconjunto y diferencia frente al programa;
6. resultado de al menos dos pruebas automatizadas pertinentes;
7. instrucciones que reproduzcan los resultados desde una copia limpia;
8. identificador Git y lista de versiones utilizadas;
9. conclusión limitada por la calidad de los datos y los supuestos.

No se suministran conjunto de funciones, arquitectura, consulta, notebook ni
plantilla. Elegir una solución proporcional al problema es parte del laboratorio.

## Explicación escrita y video

El texto debe justificar la pregunta, el reparto de responsabilidades entre
herramientas, las validaciones, el cálculo independiente, el significado de la
figura y al menos una limitación. También debe explicar qué fue necesario corregir
para lograr una ejecución limpia.

El video de YouTube, de 3 a 5 minutos, debe mostrar la ejecución completa, la
tabla o figura principal, una prueba y la verificación independiente. Ambas
personas deben justificar una decisión. Puede ser no listado y no exige mostrar
el rostro.

## Evidencia individual

Cada estudiante explica qué herramienta resolvería una parte elegida del flujo,
predice el efecto de cambiar una entrada y propone una comprobación adicional.
