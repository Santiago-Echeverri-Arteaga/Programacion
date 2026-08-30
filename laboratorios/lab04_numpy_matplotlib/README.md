# Laboratorio 4 — Caminata aleatoria y difusión

| Campo | Especificación |
|---|---|
| Fecha de realización/entrega | Martes 20 de octubre de 2026 |
| Modalidad | Tarea; no reemplaza la clase regular de ese día |
| Tiempo estimado | 120 minutos |
| Trabajo | Parejas con evidencia individual |
| Herramientas | NumPy, Matplotlib y `pytest` |

## Teoría breve

En una caminata aleatoria bidimensional no sesgada, la posición media de muchos
caminantes permanece cerca del origen y el desplazamiento cuadrático medio
`⟨r²⟩` crece aproximadamente de forma lineal con el número de pasos. NumPy
permite representar caminantes, tiempos y coordenadas como ejes de un arreglo.
Una semilla reproduce una realización, pero no describe por sí sola la
variabilidad entre realizaciones.

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
   `⟨x⟩`, `⟨y⟩` y `⟨r²⟩`.
2. Generen pasos permitidos con un generador y semilla explícita. Obtengan las
   posiciones acumuladas incluyendo el origen.
3. Calculen para cada tiempo la posición media y el desplazamiento cuadrático
   medio mediante operaciones sobre ejes.
4. Comprueben forma, `dtype`, origen, movimientos permitidos, número de pasos y
   repetibilidad de una semilla.
5. Comparen `⟨r²⟩` con la dependencia teórica y definan una medida cuantitativa
   de diferencia.
6. Repitan con al menos tres cantidades de caminantes y tres semillas. Resuman
   qué cambia y qué permanece.
7. Construyan con `fig, ax = plt.subplots()` una figura de dos paneles:
   trayectorias seleccionadas y promedio del conjunto frente a la predicción.
8. Guarden la figura desde el programa y ejecuten todo desde las instrucciones
   escritas por el equipo.

## Resultados puntuales que deben obtener

1. forma y `dtype` de los arreglos de pasos y posiciones;
2. comprobación visible de que la misma semilla produce la misma realización;
3. tabla de configuraciones con caminantes, pasos, semillas y medida de error;
4. posición media final y `⟨r²⟩` final para cada configuración;
5. figura de dos paneles con ejes, unidades o cantidades adimensionales, leyenda y
   pie explicativo;
6. resultado de pruebas sobre formas, movimientos, origen y repetibilidad;
7. conclusión sobre crecimiento de `⟨r²⟩` y variabilidad estadística.

No se anticipan formas concretas de implementación ni valores finales. El equipo
debe elegirlos, obtenerlos y verificar que sean coherentes.

## Explicación escrita y video

El texto debe explicar el significado de cada eje, qué operación reemplaza un
ciclo, la diferencia entre `⟨r⟩` y `⟨r²⟩`, qué cambia al aumentar caminantes y
qué demuestra repetir una semilla.

El video de YouTube, de 3 a 5 minutos, debe mostrar formas de arreglos, una
prueba, la figura final y una comparación entre dos configuraciones. Puede ser no
listado y no exige mostrar el rostro.

## Evidencia individual

Cada estudiante explica sin ejecutar las formas de tres arreglos y predice el
comportamiento de la posición media y del desplazamiento cuadrático medio.
