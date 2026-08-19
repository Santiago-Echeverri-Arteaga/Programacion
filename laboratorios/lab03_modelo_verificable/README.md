# Laboratorio 3 — Péndulo modular y verificable

## 1. Identificación

| Campo | Especificación |
|---|---|
| Duración presencial | 120 min |
| Trabajo | Parejas con roles rotativos |
| Herramientas | Python, pytest y biblioteca estándar |
| IA | Nivel 1: documentación; no generación de solución |
| Archivo inicial | [`pendulo.py`](pendulo.py) |

## Sincronización

- Realización: martes 6 de octubre de 2026.
- Último contenido requerido: miércoles 30 de septiembre (casos límite, `pytest`
  y el paso numérico suministrado).
- El parcial del jueves 1 de octubre queda como encuentro intermedio y no agrega
  una API ni un paradigma.
- No se requieren clases, herencia, `dataclass`, SciPy ni SymPy.

## 2. Pregunta de trabajo

¿En qué condiciones la aproximación de ángulo pequeño describe adecuadamente un
péndulo simulado?

## 3. Marco teórico breve

El péndulo ideal sin amortiguamiento satisface
`θ''=-(g/L) sin(θ)`. Para `|θ|` pequeño, `sin(θ)≈θ` y el periodo es
`T_0=2π√(L/g)`. Euler-Cromer actualiza primero la velocidad angular y luego el
ángulo; su resultado depende del paso temporal. La energía ideal es constante,
pero un método discreto introduce error. Validar exige revisar dimensiones,
signos, límites conocidos, sensibilidad al paso y propiedades físicas.

## 4. Objetivos

- implementar un modelo no lineal con responsabilidades separadas;
- justificar funciones, módulos y estructuras de datos simples;
- comparar periodos para distintas amplitudes con el límite analítico;
- cuantificar sensibilidad temporal y comportamiento de la energía.

## 5. Materiales y condiciones

- archivo inicial y Python 3.12;
- valores de gravedad, longitud, amplitudes y duración indicados por el docente;
- ángulos internos en radianes y unidades SI;
- no usar variables globales; organizar el trabajo con funciones pequeñas.

## 6. Procedimiento

1. Derive el sistema de primer orden y prediga el efecto de duplicar `L`.
2. Defina contratos para parámetros, aceleración, paso e integración usando
   números, tuplas, listas o diccionarios sencillos.
3. Implemente un paso Euler-Cromer para la ecuación no lineal.
4. Separe el modelo físico del ciclo temporal y del análisis de resultados.
5. Estime el periodo con un criterio explícito y valídelo a amplitud pequeña
   frente a `T_0`.
6. Repita para al menos tres amplitudes iniciales.
7. Repita con tres pasos temporales y documente un criterio de convergencia.
8. Calcule energía cinética y potencial; cuantifique su variación relativa.
9. Pruebe entradas inválidas, signo de aceleración, tendencia con longitud y un
   caso analítico.
10. Separe el modelo, la integración y el análisis en funciones o módulos con
    responsabilidades claras.

## 7. Resultados y discusión

Incluya tabla de amplitud, periodo simulado, `T_0`, diferencia relativa y paso;
tabla o figura de sensibilidad; y energía frente al tiempo. Discuta:

1. ¿Qué criterio define «adecuadamente» y por qué?
2. ¿El error observado proviene del modelo, del método o de ambos?
3. ¿Cómo detectaría un signo incorrecto sin leer la implementación?
4. ¿Qué separación entre funciones facilitó una prueba y cuál habría sido innecesaria?

## 8. Qué se debe presentar

- informe PDF de 5–7 páginas según
  [`../plantilla_informe.md`](../plantilla_informe.md);
- módulos en `src/`, pruebas en `tests/`, resultados y README;
- comandos de prueba y versión exacta de Git;
- registro individual de predicciones y decisiones.

Se valorará más una comparación pequeña y bien validada que una jerarquía extensa
o una simulación larga sin criterio físico.

## 9. Evidencia individual

Predecir el efecto de duplicar la longitud, trazar un paso del algoritmo y
explicar una prueba que detecte el signo incorrecto de la ecuación.
