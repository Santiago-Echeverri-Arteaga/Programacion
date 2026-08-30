# Clases de recuperación — septiembre y octubre de 2026

Estas ocho clases adicionales se realizan durante los dos primeros meses de la
reanudación, en el primer espacio institucional disponible dentro de la ventana
indicada. No sustituyen clases regulares y sus temas no se repiten en esa ruta.

Cada encuentro combina una explicación breve, la ejecución comentada de una demo
y una práctica alcanzable. Los ejemplos son puntos de observación: el estudiante
debe predecir, modificar y comprobar; no basta ejecutarlos sin explicación.

## Preparación

```bash
python -m pip install -r requirements.txt
```

## 1. SymPy — relaciones simbólicas

- **Ventana:** septiembre, después de la introducción a Python.
- **Demo:** [`01_sympy_relaciones.py`](01_sympy_relaciones.py).
- **Conceptos:** símbolo, expresión, ecuación, sustitución, derivación y
  verificación dimensional externa.
- **Práctica:** representar la energía cinética, despejar una variable, derivar
  respecto a la velocidad y comprobar el resultado por sustitución numérica.
- **Resultado:** expresión, despeje y comprobación explicados con unidades.

## 2. NetworkX — redes y caminos

- **Ventana:** septiembre, después de colecciones.
- **Demo:** [`02_networkx_red.py`](02_networkx_red.py).
- **Conceptos:** nodo, arista, peso, grado, conectividad y camino mínimo.
- **Práctica:** agregar una estación y dos conexiones a la red de la demo;
  comparar el camino mínimo antes y después y justificar el peso usado.
- **Resultado:** lista de nodos, grados y camino con costo total.

## 3. SimPy I — eventos y reloj simulado

- **Ventana:** septiembre, después de funciones y ciclos.
- **Demo:** [`03_simpy_eventos.py`](03_simpy_eventos.py).
- **Conceptos:** entorno, proceso generador, evento, `timeout` y tiempo simulado.
- **Práctica:** modelar tres mediciones separadas por intervalos distintos y
  predecir el orden temporal antes de ejecutar.
- **Resultado:** cronología de eventos cuya última marca pueda calcularse a mano.

## 4. SimPy II — recursos y colas

- **Ventana:** septiembre, después de SimPy I.
- **Demo:** [`04_simpy_recursos.py`](04_simpy_recursos.py).
- **Conceptos:** recurso limitado, solicitud, espera, servicio y liberación.
- **Práctica:** ejecutar el mismo conjunto de trabajos con capacidad uno y dos;
  registrar tiempos de espera y explicar qué cambia.
- **Resultado:** tabla pequeña de llegada, inicio, salida y espera.

## 5. xarray — arreglos con coordenadas

- **Ventana:** octubre, después de NumPy básico.
- **Demo:** [`05_xarray_campo.py`](05_xarray_campo.py).
- **Conceptos:** dimensión, coordenada, atributo, selección etiquetada y promedio
  por dimensión.
- **Práctica:** agregar un instante al campo de temperatura, seleccionar una
  posición y comparar promedios temporal y espacial.
- **Resultado:** dimensiones, selección y promedio con unidades conservadas.

## 6. scikit-image — medición sobre una imagen

- **Ventana:** octubre, después de NumPy básico.
- **Demo:** [`06_skimage_medicion.py`](06_skimage_medicion.py).
- **Conceptos:** imagen como arreglo, umbral, máscara, componentes y área.
- **Práctica:** modificar tamaño e intensidad de los objetos sintéticos;
  comparar área conocida y área medida tras segmentar.
- **Resultado:** umbral, número de objetos, áreas y error relativo.

## 7. scikit-learn I — regresión y prueba

- **Ventana:** octubre, después de NumPy y funciones.
- **Demo:** [`07_sklearn_regresion.py`](07_sklearn_regresion.py).
- **Conceptos:** variables de entrada, objetivo, partición entrenamiento/prueba,
  ajuste, predicción y error sobre datos no usados al ajustar.
- **Práctica:** cambiar el ruido y el tamaño de prueba; comparar coeficiente,
  intercepto y error sin buscar hiperparámetros.
- **Resultado:** parámetros del modelo y error de prueba con interpretación.

## 8. scikit-learn II — clasificación verificable

- **Ventana:** octubre, después de scikit-learn I.
- **Demo:** [`08_sklearn_clasificacion.py`](08_sklearn_clasificacion.py).
- **Conceptos:** escalado, *pipeline*, clasificación, predicción y matriz de
  confusión.
- **Práctica:** identificar los casos mal clasificados, cambiar una medición
  cercana a la frontera y explicar la nueva predicción.
- **Resultado:** matriz de confusión y análisis de al menos un error.

## Cierre común

Cada práctica entrega un archivo propio, una salida breve y una explicación de
qué se predijo, qué se observó y cómo se comprobó. Estos productos no se
convierten en requisitos de los laboratorios, parciales o proyecto.
