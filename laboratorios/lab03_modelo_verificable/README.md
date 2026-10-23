# Laboratorio 3 — Cálculo y simulación verificables con NumPy

Unifica los anteriores laboratorios 3 (biblioteca verificable) y 4 (caminata aleatoria). Es una sola entrega con un informe y una suite de pruebas; no son dos laboratorios completos concatenados.

| Campo | Especificación |
|---|---|
| Inicio | Jueves 22 de octubre de 2026 |
| Entrega | Jueves 5 de noviembre de 2026 |
| Dedicación por estudiante | 6–7 horas totales, incluidas 2 horas acompañadas |
| Trabajo | Máximo dos estudiantes; evidencia individual escrita |
| Herramientas | Python, NumPy, Matplotlib, pytest y pip |
| Evaluación | Sin sustentación oral ni video; rúbrica escrita de los laboratorios integrados |

## Pregunta y fundamento

¿Cómo distinguir un error de programación, un error de discretización y una fluctuación estadística? Construyan una pequeña biblioteca con dos experimentos que permitan responderlo.

Para puntos medios, se divide [a,b] en n intervalos iguales y se aproxima la integral sumando el valor en cada centro multiplicado por el ancho. En una caminata unidimensional, cada paso independiente vale −1 o +1 con igual probabilidad. Para caminantes que parten de cero, en el paso k se cumple E[x]=0 y E[x²]=k. Son predicciones de conjunto, no igualdades exactas de una muestra finita. Usen cantidades adimensionales en ambos experimentos.

## Alcance y objetivos

- Integrar funciones, módulos, contratos, pruebas e instalación local con arreglos, ejes, vectorización y azar reproducible.
- Usar el NumPy trabajado en clase: formas, indexación, operaciones por ejes y máscaras; justificar vistas/copias cuando intervengan. No es necesario utilizar toda la API vista para demostrar dominio.
- Comparar resultados con referencias independientes y comunicar error y variabilidad.
- Se permiten clases propias si ayudan a organizar el código; no son obligatorias. No se exige álgebra lineal avanzada (QR, SVD o autovalores), SciPy, Pandas, EDO, publicación en PyPI ni wheel.

## Reto 1. Una referencia determinista breve

1. Elijan **un** polinomio de grado 2 o 3, un intervalo con a < b y una integral exacta distinta de cero. Obtengan y documenten la referencia analítica y el cálculo manual con n=1.
2. Implementen puntos medios con Python y con NumPy. Pueden adaptar su función propia desarrollada en clase, identificando su procedencia. La segunda versión debe evaluar y sumar arreglos sin ciclos sobre subintervalos.
3. Definan contratos: n entero positivo (rechacen booleanos), límites numéricos finitos y a < b. Se admiten funciones específicas para el polinomio elegido; no se exige una interfaz genérica.
4. Comparen ambas versiones para n=10, 20, 40 y 80: aproximación, referencia, error absoluto y relativo. Justifiquen una tolerancia para comparar implementaciones. Calculen las razones de error sucesivas; si el denominador es cero, reporten «no aplicable».

**Incluyan:** una tabla compacta, referencia independiente y explicación de la tendencia del error. **Eviten:** un segundo integrando, benchmarks extensos o atribuir todo desacuerdo al redondeo.

## Reto 2. Simulación de un conjunto de caminantes

1. Definan los ejes y formas antes de programar. Simulen 200 pasos por caminante para N=100 y N=1000, con semillas 7 y 21: **cuatro configuraciones**.
2. Usen `numpy.random.default_rng` y operaciones vectorizadas; no recorran caminante por caminante. Incluyan la posición inicial. Se permiten ciclos sobre las cuatro configuraciones.
3. Obtengan por tiempo la posición media y el desplazamiento cuadrático medio. Construyan una tabla con N, semilla, media final, media cuadrática final y una medida de discrepancia respecto a E[x²]=k. Definan su fórmula y eviten divisiones por k=0.
4. Exporten **una figura de dos paneles** con Matplotlib OO: unas pocas trayectorias de una configuración y las cuatro curvas de media cuadrática junto con la predicción. Indiquen ejes, leyendas y qué configuración se usa para las trayectorias.
5. Interpreten el efecto de N y la semilla. Dos semillas permiten comparar realizaciones, pero no demostrar una ley estadística ni garantizar que cada resultado mejore al aumentar N.

**Incluyan:** formas y tipos de arreglos, semillas y significado físico de las reducciones por eje. **Eviten:** caminatas en 2D, ajustes de difusión o condiciones aleatorias arbitrarias que hagan fallar las pruebas ocasionalmente.

## Reto 3. Verificación y entrega reproducible

Organicen módulos el cálculo, los experimentos y la presentación. El núcleo devuelve resultados sin imprimir ni generar figuras. Entreguen al menos **seis pruebas**:

1. puntos medios contra el caso manual n=1;
2. rechazo de entradas inválidas del integrador (parametrizar varios casos es válido);
3. acuerdo Python/NumPy con tolerancia justificada;
4. acumulación de una secuencia fija corta de pasos, calculada a mano, incluido el origen;
5. formas y origen correctos, con diferencias sucesivas únicamente −1 o +1;
6. repetibilidad con la misma semilla y configuración.

La comprobación manual no debe calcular el valor esperado llamando a la función que se evalúa. No prueben que la media aleatoria sea exactamente cero.

Configuren una distribución local mínima con `pyproject.toml`. Desde un entorno limpio instalen normalmente con `python -m pip install /ruta/al/proyecto`; importen desde una carpeta externa y registren la ruta del módulo. Reutilicen la configuración practicada en clase. No se exige subir el paquete a ningún servicio.

## Entregables y preguntas del informe

Suban a GitHub código, dependencias, pruebas, las dos tablas, figura, informe único (Markdown o PDF) e instrucciones de ejecución. Entreguen URL y commit evaluable. Registren comandos y resultado de las pruebas e instalación; un notebook, si se usa, debe ejecutar de principio a fin sin estado oculto. No se proporciona un esqueleto de solución.

El informe debe responder:

1. ¿Qué evidencia separa error de implementación y discretización en el primer experimento?
2. ¿Qué eje reduce cada promedio y por qué la media de los cuadrados no es el cuadrado de la media?
3. ¿Qué demuestra fijar una semilla y qué no demuestra?
4. ¿Por qué un resultado aleatorio distinto de su esperanza no implica código incorrecto?
5. ¿Qué prueba podría detectar un origen omitido o un eje equivocado? ¿Qué prueba no lo detectaría?
6. ¿Cómo verificaron que el módulo se importó de la instalación y no de la carpeta fuente?

Cada integrante añade una nota escrita propia: una predicción previa, una prueba explicada y un error encontrado o plausible. No hay defensa oral, video ni actividad individual adicional presencial. IA nivel 1; notas individuales nivel 0, según la [política](../../programa/politica_ia.md).

## Tiempo y evaluación

Distribución orientativa: referencia y contratos 60 min; simulación y figura 120; pruebas e instalación 90; análisis, informe y revisión 90–150. Las dos horas acompañadas están incluidas, no se suman. Se aplica la [rúbrica de laboratorios integrados](../README.md#rúbrica-de-los-laboratorios-integrados-3-y-4). Una sola entrega sustituye las dos anteriores; no se exige trabajo retroactivo.
