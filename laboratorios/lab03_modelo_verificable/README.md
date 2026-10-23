# Laboratorio 3 — Reconstrucción de señales y sensibilidad con NumPy

Replanteamiento de la entrega que integra los antiguos laboratorios 3 y 4. Conserva programación modular, verificación y simulación, y refuerza el álgebra lineal de NumPy vista superficialmente. Sustituye los experimentos de puntos medios y caminatas; no añade un tercer experimento.

| Campo | Especificación |
|---|---|
| Inicio | Jueves 22 de octubre de 2026 |
| Entrega | Jueves 5 de noviembre de 2026 |
| Dedicación por estudiante | 6–7 horas totales, incluidas 2 horas acompañadas |
| Trabajo | Máximo dos estudiantes; evidencia individual escrita |
| Herramientas | Python, NumPy, Matplotlib y pytest |
| Evaluación | Sin sustentación oral ni video; rúbrica de laboratorios integrados |

## Problema único

Dos sensores mezclan las componentes de una señal física. En unidades normalizadas, el modelo es

```text
b = A(c) x + ε,       A(c) = [[1, c],
                             [c, 1]]
```

Aquí x contiene las dos componentes reales, b las dos lecturas y ε el ruido de medición. El parámetro c describe cuánto influye la otra componente en cada sensor.

**Pregunta:** ¿por qué dos sistemas que se resuelven con un residuo pequeño pueden reconstruir las señales con errores muy diferentes?

Comparen únicamente **c=0.2 y c=0.99**, usando las mismas señales y el mismo ruido. El caso c=1 se reserva para discutir y comprobar singularidad, sin simularlo como una tercera configuración.

## Material de partida y apoyo conceptual

Se proporciona el modelo anterior y las siguientes relaciones, no un programa ni resultados calculados:

- Resolver A x = b significa encontrar x; multiplicación elemento a elemento y producto matricial son operaciones diferentes.
- Un autovector cumple A v = λ v. Su dirección permite identificar una combinación de señales amplificada o atenuada por la medición.
- QR expresa A = Q R, con Q ortogonal y R triangular superior.
- SVD expresa A = U Σ Vᵀ. Los valores singulares describen factores de amplificación; para una matriz invertible, κ₂ = σmáx/σmín mide sensibilidad relativa en el peor caso.
- El residuo de la reconstrucción es A x̂ − b; el error de reconstrucción es x̂ − x. En este experimento sintético conocen x y pueden calcular ambos.
- Un valor grande de κ₂ indica posibilidad de amplificación del error relativo; no significa que cada perturbación alcance esa amplificación.
- Para matrices reales simétricas pueden consultar `numpy.linalg.eigh`; QR y SVD se calculan con NumPy, sin implementar sus algoritmos.

Consulten los apuntes y las referencias oficiales al final. El acompañamiento inicial dedica tiempo a las relaciones menos trabajadas. No se exigen demostraciones generales, algoritmos de factorización escritos a mano, mínimos cuadrados, regularización ni teoría de PCA.

## Reto 1. Construcción y recuperación de las señales

1. Generen una malla de 21 × 21 combinaciones de componentes entre −1 y 1 mediante `meshgrid`. Organicen esas señales en un arreglo y documenten qué representa cada eje. Elijan y mantengan una convención de filas o columnas.
2. Generen una única realización de ruido normal con `default_rng(7)`, media cero y desviación estándar 0.01. Debe haber un ruido por lectura y señal. Reutilicen exactamente ese arreglo para los dos valores de c.
3. Calculen las lecturas mediante producto matricial y adición vectorizada. Eviten ciclos por señal; se permite un ciclo sobre las dos configuraciones. Expliquen las formas antes y después de cada operación principal.
4. Recuperen las señales con `numpy.linalg.solve`, resolviendo varias columnas de términos independientes en una llamada según la convención elegida. No calculen explícitamente la inversa.
5. Comprueben primero un caso pequeño sin ruido, elegido y calculado a mano por el equipo. Predigan qué configuración será más sensible antes de observar los resultados.

**Decisiones propias:** organización de funciones, representación de las señales, transposiciones necesarias, contratos y tolerancias. No se entrega una secuencia de llamadas lista para copiar.

## Reto 2. Diagnóstico matricial y estadístico del mismo experimento

1. Para cada una de las dos matrices, obtengan autovalores/autovectores, QR y SVD. Verifiquen numéricamente A v ≈ λ v, QᵀQ ≈ I, QR ≈ A y UΣVᵀ ≈ A. En NumPy la última salida de SVD es Vᵀ para matrices reales; no vuelvan a transponerla sin justificarlo.
2. Calculen κ₂ a partir de los valores singulares. Expliquen qué dirección resulta más difícil de reconstruir y relacionen esa observación con un autovector de esta matriz simétrica. No generalicen la relación entre valores singulares y autovalores a cualquier matriz.
3. Calculen el error de cada señal y el residuo. Obtengan media del error y desviación estándar **por componente**, y la norma euclidiana del error **por señal**. Identifiquen los ejes reducidos y usen broadcasting al centrar los errores para comprobar su desviación estándar con ddof=0.
4. Usen una máscara y `np.where` para clasificar cada señal según si su error euclidiano supera 0.1. Reporten la proporción que supera el umbral y localicen el error máximo con `argmax`. El umbral es un criterio didáctico fijo, no una tolerancia instrumental universal.
5. Exporten **una figura de dos paneles**: mapa del error de reconstrucción sobre la malla para cada c, con la misma escala de colores, ejes y unidades normalizadas. No agreguen otras simulaciones o figuras obligatorias.

Entreguen **dos tablas compactas**: una de diagnóstico matricial (autovalores, valores singulares, κ₂ y discrepancias de verificación) y otra de reconstrucción (estadísticas por componente, error máximo, proporción sobre el umbral y máximo residuo). No impriman todas las señales ni todas las matrices en el informe.

**Precauciones:** conserven intacta la señal de referencia al modificar arreglos; expliquen una decisión concreta de vista frente a copia. No dividan por la norma de la señal en el origen: este laboratorio compara errores absolutos. Un residuo pequeño frente a lecturas ruidosas no garantiza recuperar la señal real.

## Reto 3. Verificación y ejecución reproducible

Separen cálculo, experimento y presentación en funciones y módulos. Las clases propias son opcionales. Incluyan **cinco grupos de pruebas**, parametrizados cuando resulte útil:

1. Recuperación del caso manual sin ruido y verificación del producto matricial contra ese cálculo independiente.
2. Contratos: rechazar formas incompatibles o valores no finitos; reconocer y comunicar el caso singular c=1. No traten c=0.99 como singular solo porque sea sensible.
3. Identidades de autovectores, QR y SVD, con tolerancias justificadas. Comprueben relaciones, no signos concretos de vectores: distintas convenciones pueden ser válidas.
4. Estadísticas, máscara y clasificación contra un arreglo pequeño de errores con resultados calculados a mano.
5. Reproducibilidad del ruido y conservación del arreglo de señales originales después del procesamiento.

No prueben que cada dato ruidoso sea más preciso en una configuración que en otra ni que su media sea exactamente cero. El valor esperado de una prueba independiente no debe obtenerse llamando al mismo cálculo que se evalúa.

Desde una copia y entorno limpios instalen las dependencias, ejecuten el análisis completo y las pruebas siguiendo solo el README. Registren comandos, versiones y resultados. **No se exige crear una distribución, pyproject.toml, wheel ni instalar una biblioteca propia.** Esa carga se reemplaza por el refuerzo matricial.

## Entrega única y discusión

Entreguen URL de GitHub y commit evaluable con código, dependencias, pruebas, dos tablas, una figura e informe Markdown o PDF. Incluyan parámetros y semilla para regenerar los datos sintéticos; no hace falta entregar un CSV grande. El README indica comandos y ubicación de resultados. Un notebook, si se utiliza, debe ejecutar desde cero.

Respondan brevemente, apoyándose en sus resultados:

1. ¿Qué diferencia hay entre `*` y `@` en este problema, y qué errores de formas podrían pasar inadvertidos?
2. ¿Qué aportan autovalores, QR y SVD a la verificación o interpretación? ¿Por qué no basta con imprimir sus salidas?
3. ¿Cómo relacionan la dirección difícil de reconstruir con κ₂ y los errores observados? ¿Por qué κ₂ no es una predicción exacta de cada error absoluto?
4. ¿Por qué el residuo puede ser pequeño aunque la reconstrucción sea mala? ¿Qué cambia en c=1?
5. ¿Qué eje se reduce en cada estadística, cómo usaron broadcasting y cómo protegieron el arreglo original?

Cada integrante agrega una nota propia con una predicción, una prueba explicada y una decisión de implementación. Sin video, sustentación ni actividad presencial adicional. IA nivel 1; notas individuales nivel 0, según la [política](../../programa/politica_ia.md).

## Carga y evaluación

| Bloque | Tiempo orientativo |
|---|---:|
| Modelo, consulta conceptual y predicción | 45 min |
| Malla, ruido y reconstrucción vectorizada | 75 min |
| Diagnóstico matricial, estadísticas y figura | 90 min |
| Pruebas y ejecución limpia | 75 min |
| Informe y revisión | 75–135 min |
| **Total, incluido acompañamiento** | **6–7 h** |

Los primeros 120 minutos acompañados se destinan a modelo y conceptos (45), formas y reconstrucción (45) y orientación sobre identidades matriciales (30). Están incluidos en el total. La estimación supone usar las funciones de NumPy y limitarse a las dos configuraciones; no implementar factorizaciones.

Se aplica la [rúbrica integrada](../README.md#rúbrica-de-los-laboratorios-integrados-3-y-4), sin cambiar fechas ni peso. Sustituir integración, caminatas y empaquetado permite reforzar temas sin acumular entregables. El laboratorio 4 de Pandas conserva su alcance.

## Referencias de consulta

- [Álgebra lineal en NumPy](https://numpy.org/doc/stable/reference/routines.linalg.html).
- [Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html).
- [Copias y vistas](https://numpy.org/doc/stable/user/basics.copies.html).
