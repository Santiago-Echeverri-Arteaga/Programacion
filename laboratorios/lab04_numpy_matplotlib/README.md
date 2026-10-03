# Laboratorio 4 — Caminata aleatoria y difusión

| Campo | Especificación |
|---|---|
| Inicio | Jueves 22 de octubre de 2026 |
| Entrega | Martes 3 de noviembre de 2026 |
| Modalidad | Inicio acompañado y continuación autónoma |
| Dedicación por estudiante | 2 horas acompañadas + 3–4 horas autónomas; incluye informe y video |
| Trabajo | Parejas con evidencia individual |
| Herramientas | NumPy, Matplotlib y `pytest` |

## Teoría breve

En una caminata aleatoria unidimensional no sesgada, la posición media de muchos
caminantes permanece cerca del origen y el desplazamiento cuadrático medio
`⟨x²⟩` crece aproximadamente de forma lineal con el número de pasos. NumPy
permite representar caminantes y tiempos como ejes de un arreglo.
Una semilla reproduce una realización, pero no describe por sí sola la
variabilidad entre realizaciones.

Los pasos son −1 o +1 con igual probabilidad, independientes, en unidades de longitud de paso. En el paso k, E[x]=0 y E[x²]=k; son predicciones de conjunto, no igualdades exactas para una muestra finita. No exigir tolerancias arbitrarias a resultados aleatorios ni que aumentar caminantes mejore cada realización.

## Objetivos

- diseñar arreglos con formas y ejes explícitos;
- simular y resumir un conjunto de caminatas con operaciones vectorizadas;
- comprobar formas, movimientos permitidos y reproducibilidad;
- estudiar la variabilidad entre tamaños de conjunto y semillas;
- producir una figura científica con la interfaz orientada a objetos.

## Requerimientos y límites

- usar NumPy, `numpy.random.Generator`, Matplotlib OO y `pytest`;
- incluir la posición inicial y registrar cada semilla;
- no recorrer caminante por caminante con un ciclo; se permiten ciclos sobre un
  número pequeño de configuraciones;
- crear todo el código desde cero, sin esqueleto ni nombres obligatorios;
- no usar Pandas, SciPy, SymPy ni programación orientada a objetos propia.

## Procedimiento

1. Dibujen los ejes y formas de los arreglos antes de programar. Predigan
   `⟨x⟩` y `⟨x²⟩`.
2. Generen pasos permitidos con un generador y semilla explícita. Obtengan las
   posiciones acumuladas incluyendo el origen.
3. Calculen para cada tiempo la posición media y el desplazamiento cuadrático
   medio mediante operaciones sobre ejes.
4. Comprueben forma, `dtype`, origen, movimientos permitidos, número de pasos y
   repetibilidad de una semilla.
5. Comparen `⟨x²⟩` con la dependencia teórica y definan una medida cuantitativa
   de diferencia.
6. Repitan con dos cantidades de caminantes (100 y 1000) y dos semillas (7 y 21), con 200 pasos por caminata. Resuman
   qué cambia y qué permanece.
7. Construyan con `fig, ax = plt.subplots(1, 2)` una figura de dos paneles:
   trayectorias seleccionadas y promedio del conjunto frente a la predicción.
8. Guarden la figura desde el programa y ejecuten todo desde las instrucciones
   escritas por el equipo.

## Resultados puntuales que deben obtener

1. forma y `dtype` de los arreglos de pasos y posiciones;
2. comprobación visible de que la misma semilla produce la misma realización;
3. tabla de configuraciones con caminantes, pasos, semillas y medida de error;
4. posición media final y `⟨x²⟩` final para cada configuración;
5. figura de dos paneles con ejes, unidades o cantidades adimensionales, leyenda y
   pie explicativo;
6. resultado de pruebas sobre formas, movimientos, origen y repetibilidad;
7. conclusión sobre crecimiento de `⟨x²⟩` y variabilidad estadística.

No se anticipan formas concretas de implementación ni valores finales. El equipo
debe elegirlos, obtenerlos y verificar que sean coherentes.

## Explicación escrita y video

El texto debe explicar el significado de cada eje, qué operación reemplaza un
ciclo, la diferencia entre `⟨x⟩` y `⟨x²⟩`, qué cambia al aumentar caminantes y
qué demuestra repetir una semilla.

El video de YouTube, de 3 a 5 minutos, debe mostrar formas de arreglos, una
prueba, la figura final y una comparación entre dos configuraciones. Puede ser no
listado y no exige mostrar el rostro.

## Evidencia individual

Cada estudiante explica sin ejecutar las formas de tres arreglos y predice el
comportamiento de la posición media y del desplazamiento cuadrático medio.


## Entrega en GitHub

Deben **subir el código y el informe a GitHub**. Entregar URL del repositorio y commit evaluable. El README debe enlazar el informe Markdown o PDF e indicar comandos, dependencias y versiones para reproducirlo. Incluir datos permitidos o su fuente, resultados solicitados, evidencia de comprobaciones y enlace al video de 3–5 minutos. El informe responde las preguntas de esta guía, interpreta resultados y reconoce limitaciones; no es una colección de capturas. Cada integrante identifica su contribución. Si el repositorio es privado, habilitar acceso al docente antes de entregar.

Se aplica la [rúbrica común](../README.md). No subir `.venv`, cachés ni credenciales. Comprobar que código, informe y resultados son visibles en GitHub, no solo en el computador.


## Inicio y distribución

El 22 oct.: modelo 20 min, formas/ejes 25, simulación 40, figura 25 y commit 10. Fuera de clase: 60–90 min de configuraciones y pruebas, 60 de análisis e informe, 60–90 de ajustes, video y GitHub. El paso a dos dimensiones es opcional, no evaluable. IA nivel 1; evidencia individual nivel 0.
