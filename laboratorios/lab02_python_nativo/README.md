# Laboratorio 2 — Caída libre con Python nativo

## 1. Identificación

| Campo | Especificación |
|---|---|
| Duración presencial | 120 min |
| Trabajo | Parejas con evidencia individual |
| Herramientas | Python 3.12 y biblioteca estándar |
| IA | Nivel 1: no se permite generar código ni texto de la entrega |
| Archivos | [`analisis_caida.py`](analisis_caida.py) y datos del curso |

## Sincronización

- Realización: jueves 24 de septiembre de 2026.
- Último contenido requerido: martes 22 de septiembre (archivos, `pathlib`,
  `with` y excepciones).
- El miércoles 23 se dedica a práctica y lectura de errores; no agrega una técnica
  evaluable.
- `pytest` todavía no es prerrequisito. Las comprobaciones se ejecutan con casos
  pequeños y se documentan en una tabla.

## 2. Pregunta de trabajo

¿Son compatibles las posiciones suministradas con un movimiento de caída libre
desde el reposo?

## 3. Marco teórico breve

Para movimiento vertical con aceleración constante y velocidad inicial nula,
`h(t)=h_0-g t²/2`; por tanto, para `t>0`, una estimación puntual es
`g_i=2(h_0-h_i)/t_i²`. El cociente amplifica perturbaciones cuando `t` es pequeño.
La media y la dispersión resumen una serie, pero no demuestran por sí solas que el
modelo sea válido. La lectura computacional debe conservar unidades, validar el
orden temporal y distinguir datos, modelo y estimación.

## 4. Objetivos

- leer y validar un CSV con la biblioteca estándar;
- descomponer el análisis en funciones puras con contratos;
- estimar y resumir `g` con unidades y cifras razonables;
- diseñar casos de prueba normales, de frontera e inválidos sin exigir `pytest`.

## 5. Materiales y restricciones

- `datos/caida_libre_sintetica.csv`;
- módulos estándar `csv`, `pathlib`, `statistics` y `math` si se requieren;
- no usar NumPy, Pandas, SciPy ni IA generativa;
- no modificar el archivo original ni ocultar errores con `except Exception`.

## 6. Procedimiento

1. Lea encabezado, diccionario de datos y procedencia; prediga el orden de `g`.
2. Diseñe funciones separadas para leer, validar, calcular, resumir y presentar.
3. Con `csv`, convierta cada fila a tipos numéricos e informe número de línea ante
   un dato inválido.
4. Valide archivo no vacío, columnas, tiempos estrictamente crecientes, alturas e
   incertidumbres según el diccionario.
5. Calcule `g_i` solamente para tiempos positivos; conserve cada resultado.
6. Calcule media, desviación y rango usando funciones propias o `statistics`.
7. Compare el estimado con el valor de referencia indicado, declarando el criterio
   de compatibilidad que emplea.
8. Ejecute y documente al menos: caso pequeño calculable a mano, archivo vacío,
   fila inválida, tiempo no creciente y límite `t=0`. Puede usar llamadas simples
   y `assert`; no se exige una suite de `pytest`.
9. Ejecute desde la raíz y desde otro directorio para verificar las rutas.

## 7. Resultados y discusión

Presente tabla de `t`, `h` y `g_i`, resumen con unidades, resultados de pruebas y
respuesta a:

1. ¿Por qué los tiempos iniciales producen estimaciones más inestables?
2. ¿Qué supuesto del modelo podría fallar en un experimento real?
3. ¿Compatibilidad significa igualdad exacta? Justifique.
4. ¿Qué validación protege la conclusión y cuál solo protege el programa?

## 8. Qué se debe presentar

- informe PDF de 4–6 páginas con la estructura de
  [`../plantilla_informe.md`](../plantilla_informe.md);
- `src/analisis_caida.py`, datos originales, casos de comprobación y README de ejecución;
- salida textual versionada con unidades y versión de Git;
- registro individual de predicción y casos de prueba.

El informe debe incluir ecuación y supuestos, diagrama breve de funciones, tabla
de resultados, discusión de sensibilidad a tiempos pequeños y conclusión
limitada a la evidencia.

## 9. Evidencia individual

En papel: escribir una función que rechace tiempos no crecientes, proponer dos
casos límite y explicar la diferencia entre `return` y `print` en el análisis.
