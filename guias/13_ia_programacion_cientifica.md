# Guía 13 — IA, agentes y responsabilidad científica

## Ficha

- Realización: miércoles 21 de octubre de 2026, integrada con la clínica del
  proyecto y la propuesta.
- Duración: 120 minutos.
- Nivel de IA: 3 durante la demostración; 0 en la salida individual.
- Resultados: RA 6, RA 10 y RA 11.
- Archivos: `Codigos/14_ia_agentes/` y `proyecto_final/AI_USAGE.md`.

## Propósito

Mostrar un flujo profesional de colaboración humano-IA sin presentar la IA como
fuente de verdad ni como reemplazo de la programación. La pregunta central es:
“¿Qué evidencia necesito antes de confiar en este cambio?”.

## Preparación

- Usar un repositorio desechable con una versión confirmada antes de la demo.
- Desactivar cualquier acceso a credenciales o datos personales.
- Preparar el ejemplo defectuoso y sus pruebas.
- Tener capturas de la interacción por si el servicio no está disponible.
- No introducir un agente en el repositorio real del curso durante la demo.

## Secuencia

| Tiempo | Actividad |
|---:|---|
| 0–10 | Predicción: ¿qué puede demostrar que un programa se ejecuta? |
| 10–25 | Modelo conceptual de un LLM: generación plausible, contexto limitado y ausencia de garantía física |
| 25–40 | Riesgos: errores, sesgos, privacidad, licencias, dependencia y falsa autoridad |
| 40–60 | Demostración de agente: inspeccionar, proponer plan, editar y ejecutar pruebas |
| 60–70 | Pausa y recolección de observaciones |
| 70–98 | Auditoría en grupos del código generado defectuoso |
| 98–110 | Discusión: qué aceptó el humano, qué rechazó y qué evidencia faltaba |
| 110–115 | Cómo diligenciar `AI_USAGE.md` |
| 115–120 | Salida individual sin IA |

## Protocolo de trabajo con agentes

1. Definir el problema y los criterios de aceptación antes de pedir código.
2. Limitar explícitamente archivos, datos y acciones permitidas.
3. Pedir inspección y plan antes de editar.
4. Revisar el diff, no solo la respuesta conversacional.
5. Ejecutar pruebas existentes y agregar pruebas independientes.
6. Verificar unidades, signos, casos límite y plausibilidad física.
7. Rechazar cambios no comprendidos.
8. Registrar la asistencia utilizada.

## Actividad forense

Los grupos reciben una solución aparentemente limpia para caída libre. Deben
clasificar sus defectos como:

- sintáctico;
- lógico;
- numérico;
- físico o dimensional;
- de pruebas;
- de reproducibilidad;
- de seguridad o privacidad.

Cada afirmación debe acompañarse de un caso que la pueda refutar o confirmar.

## Salida individual

Se presenta un fragmento nuevo. El estudiante debe escribir:

1. una afirmación que aún no está demostrada;
2. una prueba concreta;
3. un riesgo físico o numérico;
4. la decisión de aceptar, modificar o rechazar el fragmento.

## Mensaje docente central

Que una IA haya producido el código no es argumento para aceptarlo ni para
rechazarlo. El criterio es la evidencia. Quien entrega el resultado conserva la
responsabilidad de comprenderlo y defenderlo.
