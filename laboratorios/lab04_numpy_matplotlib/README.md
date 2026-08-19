# Laboratorio 4 — Caminata aleatoria y difusión

## 1. Identificación

| Campo | Especificación |
|---|---|
| Duración presencial | 120 min |
| Trabajo | Parejas con evidencia individual |
| Herramientas | NumPy, Matplotlib OO y pytest |
| IA | Nivel 1: documentación; no generación de código o informe |
| Archivo inicial | [`caminata.py`](caminata.py) |

## Sincronización

- Realización: jueves 15 de octubre de 2026.
- Último contenido requerido: martes 13 de octubre; el miércoles 14 es práctica.
- No se exige Pandas, SciPy, SymPy ni POO.

## 2. Pregunta de trabajo

¿Cómo crece el desplazamiento cuadrático medio de un conjunto de caminantes
aleatorios bidimensionales?

## 3. Marco teórico breve

En una caminata aleatoria no sesgada, cada incremento tiene media nula e
incrementos independientes. La posición media del conjunto debe permanecer cerca
del origen, mientras el desplazamiento cuadrático medio `⟨r²⟩` crece linealmente
con el número de pasos en el régimen ideal. NumPy representa simultáneamente
caminantes, tiempos y coordenadas; vectorizar significa operar sobre ejes del
arreglo, no ocultar el significado de sus formas. Una semilla permite repetir una
realización, pero no sustituye estudiar la variabilidad entre realizaciones.

## 4. Objetivos

- representar pasos y posiciones con formas explícitas;
- calcular promedios de conjunto mediante operaciones vectorizadas;
- estudiar reproducibilidad y variabilidad estadística;
- construir una figura científica con la API orientada a objetos.

## 5. Materiales y restricciones

- Python, NumPy, Matplotlib y archivo inicial;
- semilla configurable y registrada;
- no usar ciclos sobre cada caminante; se admiten ciclos sobre configuraciones;
- usar `fig, ax = plt.subplots()` y guardar la figura desde el código.

## 6. Procedimiento

1. Dibuje los ejes del arreglo previsto: caminante, paso y coordenada.
2. Prediga `⟨x⟩`, `⟨y⟩` y `⟨r²⟩` antes de simular.
3. Genere incrementos permitidos con `numpy.random.Generator` y semilla explícita.
4. Obtenga posiciones acumuladas incluyendo posición inicial nula.
5. Calcule posición media y desplazamiento cuadrático medio para cada tiempo.
6. Verifique forma, `dtype`, pasos permitidos, origen y repetibilidad de semilla.
7. Compare contra la dependencia teórica y cuantifique la diferencia con un
   indicador definido por el equipo.
8. Repita para al menos tres cantidades de caminantes y varias semillas.
9. Compruebe que ninguna vista modifique accidentalmente el arreglo fuente.
10. Cree una figura de dos paneles: trayectorias seleccionadas y promedio de
    conjunto frente a la predicción.

## 7. Resultados y discusión

Presente una tabla de configuraciones y un resumen de variabilidad, además de la
figura final. Responda:

1. ¿Por qué `⟨r⟩` y `⟨r²⟩` describen comportamientos diferentes?
2. ¿Qué cambia al aumentar caminantes sin aumentar pasos?
3. ¿Qué demuestra repetir una semilla y qué no demuestra?
4. ¿Qué forma de arreglo permitió eliminar un ciclo y por qué?

## 8. Qué se debe presentar

- informe PDF de 5–7 páginas según
  [`../plantilla_informe.md`](../plantilla_informe.md);
- código modular, pruebas, figura en PNG/PDF y README de ejecución;
- tabla de configuraciones, semillas y resultados resumidos;
- registro individual con predicción y explicación de formas.

El pie de figura debe indicar número de caminantes, pasos, regla de movimiento,
semilla o conjunto de semillas y significado de las líneas.

## 9. Evidencia individual

Explicar, sin ejecutar, las formas de tres arreglos y predecir el comportamiento
de posición media y desplazamiento cuadrático medio.
