# Laboratorio 3 — Péndulo modular y verificable

| Campo | Especificación |
|---|---|
| Fecha de realización/entrega | Martes 6 de octubre de 2026 |
| Modalidad | Tarea; no reemplaza la clase regular de ese día |
| Tiempo estimado | 120 minutos |
| Trabajo | Parejas con evidencia individual |
| Herramientas | Python, `pytest` y biblioteca estándar |

## Teoría breve

El péndulo ideal sin amortiguamiento satisface
`θ''=-(g/L) sin(θ)`. Para ángulos pequeños, `sin(θ)≈θ` y
`T₀=2π√(L/g)`. Euler-Cromer actualiza primero la velocidad angular y luego
el ángulo. El resultado depende del paso temporal: comparar varios pasos permite
distinguir comportamiento físico de error numérico.

## Objetivos

- traducir una ecuación diferencial a un algoritmo suministrado en clase;
- organizar el modelo en funciones y módulos con responsabilidades claras;
- comprobar signos, entradas, límites conocidos y sensibilidad temporal;
- comparar el periodo simulado con la aproximación de ángulo pequeño;
- comunicar qué parte del error procede del modelo y cuál del método.

## Requerimientos y límites

- usar Python nativo, `math` y `pytest`;
- trabajar internamente en radianes y unidades SI;
- implementar el paso Euler-Cromer practicado en clase;
- crear la organización y el código desde cero, sin esqueleto suministrado;
- no usar NumPy, SciPy, SymPy, clases, herencia ni `dataclass`;
- no usar variables globales para parámetros del modelo.

## Procedimiento

1. Deriven el sistema de primer orden y predigan qué ocurre con el periodo si se
   duplica la longitud.
2. Decidan cómo separar validación de parámetros, aceleración angular, paso
   numérico, simulación y análisis.
3. Implementen Euler-Cromer para la ecuación no lineal y conserven tiempo,
   ángulo y velocidad angular.
4. Definan un criterio reproducible para estimar el periodo y compruébenlo a
   amplitud pequeña frente a `T₀`.
5. Repitan para tres amplitudes iniciales y tres pasos temporales razonables.
6. Calculen la energía cinética y potencial y midan su variación relativa.
7. Escriban pruebas para entradas inválidas, signo de aceleración, tendencia con
   la longitud, un valor analítico y una propiedad de la salida temporal.
8. Ejecuten las pruebas y el análisis desde instrucciones escritas por el equipo.

## Resultados puntuales que deben obtener

1. historial de tiempo, ángulo y velocidad para una configuración identificada;
2. tabla con amplitud, paso, periodo simulado, `T₀` y diferencia relativa;
3. comparación de al menos tres pasos temporales;
4. variación relativa de la energía para cada paso;
5. suite de pruebas con casos identificables y resultado de ejecución;
6. criterio cuantitativo que diga cuándo la aproximación es adecuada;
7. conclusión que diferencie error de modelo y error numérico.

La guía no impone nombres de archivos o funciones ni anticipa los resultados
numéricos. Esas decisiones deben poder justificarse.

## Explicación escrita y video

El texto debe desarrollar la transformación a primer orden, justificar la
separación del programa, explicar el criterio de periodo, interpretar la
sensibilidad al paso y responder cómo se detectaría un signo incorrecto sin leer
la implementación.

El video de YouTube, de 3 a 5 minutos, debe mostrar una ejecución, una prueba, la
comparación de periodos y el efecto de cambiar el paso. Ambas personas deben
explicar una parte. Puede ser no listado y no exige mostrar el rostro.

## Evidencia individual

Cada estudiante predice el efecto de duplicar la longitud, traza a mano un paso
del algoritmo y explica una prueba que detecte el signo incorrecto.
