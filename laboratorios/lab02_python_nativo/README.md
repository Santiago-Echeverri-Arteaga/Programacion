# Laboratorio 2 — Caída libre con Python nativo

| Campo | Especificación |
|---|---|
| Inicio | Jueves 8 de octubre de 2026 |
| Entrega | Jueves 15 de octubre de 2026 |
| Modalidad | Inicio acompañado y continuación autónoma |
| Dedicación por estudiante | 2 horas acompañadas + 3–4 horas autónomas; incluye informe y video |
| Trabajo | Parejas con evidencia individual |
| Herramientas | Python 3.12 y biblioteca estándar |

## Teoría breve

Para movimiento vertical con aceleración constante y velocidad inicial nula,
`h(t)=h₀-g t²/2`. Para `t>0`, cada observación permite estimar
`gᵢ=2(h₀-hᵢ)/tᵢ²`. Los tiempos muy pequeños amplifican las perturbaciones.
Una media resume valores, pero no basta para validar el modelo: también se deben
revisar unidades, orden temporal, datos inválidos y sensibilidad.

Para resumir N estimaciones se puede usar acumulación ya conocida:
media = suma(gᵢ)/N; desviación poblacional = raíz(suma((gᵢ-media)²)/N).
La raíz puede calcularse como potencia 0.5. Si usan desviación muestral con
N-1, deben identificarla y comprobar N>1. El rango es máximo menos mínimo;
error relativo = error absoluto / valor de referencia no nulo. No se exige
aprender una biblioteca estadística nueva para realizar estos cálculos.

## Objetivos

- leer y validar un CSV con la biblioteca estándar;
- separar lectura, validación, cálculo y presentación en funciones propias;
- estimar y resumir `g` con unidades;
- comprobar el programa con casos normales, de frontera e inválidos;
- explicar el alcance físico del resultado.

## Requerimientos y límites

- usar [caida_libre_sintetica.csv](../../datos/caida_libre_sintetica.csv) y conservarlo sin cambios; tomar h₀ = 10,00 m y g de referencia = 9,81 m/s². La columna incertidumbre_m expresa incertidumbre de altura; describirla, sin exigir propagación formal;
- utilizar `pathlib` y `with`; la separación manual de campos basta para este CSV
  numérico. `csv`, `statistics` y `math` son opcionales si se explican sus usos;
  también se permiten acumulación y fórmulas con Python nativo;
- crear todo el código desde cero; no se suministra esqueleto ni nombres de
  funciones obligatorios;
- no usar NumPy, Pandas, SciPy ni IA generativa (nivel 1); pytest es opcional, pues se introduce el 6 oct.;
- no ocultar errores mediante `except Exception` sin tratamiento específico.

## Procedimiento

1. Lean el encabezado y documenten columnas, unidades y significado físico.
2. Diseñen antes de programar cómo separarán lectura, validación, cálculo,
   resumen y escritura de resultados.
3. Lean el CSV y conviertan sus campos a tipos numéricos. Un dato inválido debe
   producir un mensaje que permita localizar la fila.
4. Validen archivo no vacío, columnas necesarias, tiempos estrictamente
   crecientes, valores finitos, alturas entre 0 y h₀ e incertidumbres positivas. Para t=0 conservar la fila inicial, sin calcular gᵢ ni incluirla en el resumen de g.
5. Calculen `gᵢ` solo para tiempos positivos y conserven cada estimación.
6. Obtengan media, desviación y rango. Comparen con el valor de referencia y
   definan qué significa «compatible» para el equipo.
7. Comprueben como mínimo un caso calculable a mano, un archivo vacío, una fila
   inválida, tiempos no crecientes y el límite `t=0`. Pueden usar llamadas y resultados esperados a mano. `assert` es opcional;
   no se exige una herramienta que no se haya explicado.
8. Ejecuten el programa desde dos ubicaciones distintas para revisar el manejo de
   rutas y registren cualquier corrección necesaria.

## Resultados puntuales que deben obtener

1. número de filas válidas del archivo original y registro de los casos inválidos
   ensayados por separado; no es obligatorio continuar tras una fila inválida;
2. tabla con `t`, `h` y cada `gᵢ`, incluyendo unidades;
3. media, desviación, mínimo y máximo de las estimaciones válidas;
4. diferencia absoluta y relativa frente al valor de referencia;
5. resultado visible de los cinco casos de comprobación;
6. conclusión explícita sobre compatibilidad y al menos una limitación.

Los valores numéricos no se anticipan en la guía. El equipo debe obtenerlos,
verificarlos y decidir una presentación comprensible.

## Explicación escrita y video

El texto debe explicar la ecuación y sus supuestos, la organización elegida para
el programa, el criterio de compatibilidad, por qué los tiempos iniciales son más
inestables y qué validación protege la conclusión física.

El video de YouTube, de 3 a 5 minutos, debe ejecutar el programa, mostrar la tabla
o resumen principal, demostrar un caso inválido y explicar una decisión del
diseño. Puede ser no listado y no exige mostrar el rostro.

## Evidencia individual

Cada estudiante escribe una función corta de validación, propone dos casos límite
y explica la diferencia entre `return` y `print` en este análisis.


## Entrega en GitHub

Deben **subir el código y el informe a GitHub**. Entregar URL del repositorio y commit evaluable. El README debe enlazar el informe Markdown o PDF e indicar comandos, dependencias y versiones para reproducirlo. Incluir datos permitidos o su fuente, resultados solicitados, evidencia de comprobaciones y enlace al video de 3–5 minutos. El informe responde las preguntas de esta guía, interpreta resultados y reconoce limitaciones; no es una colección de capturas. Cada integrante identifica su contribución. Si el repositorio es privado, habilitar acceso al docente antes de entregar.

Se aplica la [rúbrica común](../README.md). No subir `.venv`, cachés ni credenciales. Comprobar que código, informe y resultados son visibles en GitHub, no solo en el computador.


## Inicio en clase — jueves 8 de octubre, 120 minutos

| Minutos | Producto de trabajo |
|---|---|
| 0–15 | Pregunta física, unidades, predicción y lectura del CSV |
| 15–35 | Diseño en funciones y definición de casos de comprobación |
| 35–65 | Lectura y validación; ejecutar un archivo normal y otro defectuoso |
| 65–95 | Calcular g por fila y un resumen provisional |
| 95–110 | Caso manual, t=0 y revisión entre integrantes |
| 110–120 | Primer commit y lista de pendientes para el 15 oct. |

El taller individual del miércoles 7 practica funciones, colecciones, módulos, rutas, lectura y excepciones mediante ejercicios independientes. El laboratorio aplica esas habilidades a un problema físico completo. El laboratorio no requiere NumPy ni empaquetado. El hito de salida del jueves 8 es lector funcional y un cálculo comprobado, no el informe terminado. Distribución autónoma orientativa: 90 min de implementación, 45 de comprobaciones y 45–105 de informe, video y publicación.
