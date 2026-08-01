# Laboratorio 4 — Caminata aleatoria y difusión

## Pregunta

¿Cómo crece el desplazamiento cuadrático medio de un conjunto de caminantes
aleatorios bidimensionales?

## Restricciones

- NumPy para generación, almacenamiento y operaciones masivas.
- Matplotlib mediante `fig, ax = plt.subplots()`.
- Semilla controlable desde la interfaz del programa.
- Nivel de IA 1.

## Tareas

1. Generar pasos para muchos caminantes sin ciclos sobre cada partícula.
2. Calcular posiciones acumuladas y desplazamiento cuadrático medio.
3. Verificar forma, tipo y reproducibilidad de los arreglos.
4. Comparar el resultado con la dependencia teórica esperada.
5. Repetir para distintos números de caminantes y cuantificar la variabilidad.
6. Crear una figura con trayectoria de ejemplo y promedio de conjunto.
7. Guardar la figura con etiquetas, unidades conceptuales y leyenda pertinente.

## Pruebas mínimas

- misma semilla, mismo resultado;
- forma correcta del arreglo;
- posición inicial nula;
- incremento de cada eje perteneciente al conjunto permitido;
- ausencia de modificación accidental por vistas.

## Salida individual

Explicar la diferencia entre el promedio de posiciones y el promedio de
desplazamientos cuadrados, y predecir sus comportamientos.

