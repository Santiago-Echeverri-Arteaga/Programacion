# Datos del curso

Cada conjunto de datos debe tener procedencia, unidades, licencia o condiciones de
uso y una descripción de las transformaciones realizadas.

## Conjuntos iniciales

- `caida_libre_sintetica.csv`: posiciones simuladas con ruido para una caída
  vertical desde el reposo. Datos didácticos sintéticos, generados para el curso;
  no representan un experimento real.
- `enfriamiento_sintetico_sucio.csv`: mediciones didácticas con duplicados,
  faltantes, unidades mezcladas y un valor sospechoso. Su suciedad es intencional.

Los datos derivados por estudiantes deben guardarse en `datos/generados/`,
directorio que no se versiona.


## Metadatos del laboratorio 4 integrado

`sensores_enfriamiento.csv` es una tabla didáctica creada para el curso, de libre uso en sus actividades: `sensor` es clave única y `zona` identifica la zona sintética asociada. Se une por `sensor` a `enfriamiento_sintetico_sucio.csv`. No representa calibraciones reales ni justifica descartar mediciones. Las etiquetas Zona A y Zona B solo identifican los dos grupos del ejemplo.

En el laboratorio 4 los resultados evaluables sí deben guardarse en GitHub; usen una carpeta de resultados no ignorada. La regla general sobre `datos/generados/` no exime de entregar las tablas solicitadas.
