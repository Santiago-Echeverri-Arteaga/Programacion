# Laboratorio 5 — Datos de enfriamiento imperfectos

## 1. Identificación

| Campo | Especificación |
|---|---|
| Duración presencial | 120 min |
| Trabajo | Parejas con evidencia individual |
| Herramientas | Pandas, NumPy y Matplotlib |
| IA | Nivel 1; ocurre antes de la clase formal de IA |
| Datos | `datos/enfriamiento_sintetico_sucio.csv` |

## Sincronización

- Realización: jueves 29 de octubre de 2026.
- Último contenido requerido: martes 27 de octubre; el miércoles 28 es práctica.
- `groupby`, combinaciones entre tablas y ajustes de curvas pueden mostrarse en la
  práctica, pero no son requisitos de la entrega.

## 2. Pregunta de trabajo

¿Qué puede concluirse sobre el enfriamiento de dos zonas de una placa después de
documentar y tratar problemas de calidad de los datos?

## 3. Marco teórico breve

La ley de enfriamiento de Newton propone que la rapidez de cambio de temperatura
es proporcional a la diferencia con el ambiente, bajo supuestos que deben
declararse. Antes de ajustar o comparar, una tabla se audita por tipos, faltantes,
duplicados, rangos, unidades y categorías. Limpiar no significa eliminar todo lo
inusual: una observación sospechosa puede ser error, evento real o dato que exige
metadatos adicionales. Los datos crudos son inmutables; cada transformación debe
ser reproducible y cuantificada.

## 4. Objetivos

- auditar sistemáticamente un conjunto tabular imperfecto;
- definir reglas de transformación basadas en evidencia;
- conservar procedencia, unidades y conteos antes/después;
- comparar dos zonas sin exceder lo que permiten los datos.

## 5. Datos y precauciones

El archivo contiene intencionalmente una fila duplicada, una medición faltante,
unidades mezcladas, un valor físicamente sospechoso y etiquetas de calidad. No
sobrescriba el original. Trabaje con una copia lógica y conserve columnas de
origen. Una etiqueta no se ignora ni se toma como verdad sin discutirla.

## 6. Procedimiento

1. Lea procedencia y diccionario; formule una predicción para las dos zonas.
2. Cargue el archivo desde `datos/raw` sin modificarlo.
3. Registre forma, columnas, tipos, nulos, duplicados, categorías y rangos.
4. Prepare una tabla de incidencias: fila, problema, evidencia y acción propuesta.
5. Convierta temperaturas a una unidad común conservando valor/unidad originales.
6. Distinga duplicado exacto de posible réplica. Defina tratamiento de faltantes
   y valores sospechosos sin eliminación silenciosa.
7. Implemente transformaciones encadenadas o funciones reproducibles.
8. Registre cuántas filas se conservan, marcan, convierten o excluyen en cada etapa.
9. Valide claves, tipos, unidades, rangos y unicidad esperada después de limpiar.
10. Compare zonas mediante selección, resúmenes y una figura con incertidumbre o
    dispersión. No se exige `groupby`.
11. Reinicie el kernel, ejecute todo de principio a fin y exporte resultados.

## 7. Resultados y discusión

Incluya auditoría inicial, registro de decisiones, flujo de conteos, tabla limpia
resumida y figura final. Responda:

1. ¿Cómo cambia la conclusión bajo una regla alternativa razonable?
2. ¿Excluir el valor sospechoso introduce un sesgo posible?
3. ¿Qué metadato adicional resolvería la decisión más incierta?
4. ¿Los datos permiten afirmar una diferencia física o solo descriptiva?

## 8. Qué se debe presentar

- informe PDF de 5–7 páginas según
  [`../plantilla_informe.md`](../plantilla_informe.md);
- notebook reiniciable y funciones auxiliares en `src/` cuando corresponda;
- datos crudos, tabla procesada, diccionario, figura y registro de limpieza;
- README con orden exacto de ejecución y versión de dependencias;
- registro individual previo a la limpieza.

El informe debe diferenciar datos crudos, decisiones, resultados e inferencias.
No se acepta una tabla «limpia» sin trazabilidad.

## 9. Evidencia individual

Analizar una regla de limpieza propuesta por otra persona, identificar un sesgo
posible y señalar qué evidencia se necesitaría para aceptarla.
