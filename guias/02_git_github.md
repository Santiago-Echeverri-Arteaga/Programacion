# Guía 02 — Git y GitHub para trabajo científico

## Ficha

- Semana: 2.
- Duración: un encuentro de 120 minutos más aplicación en el laboratorio 1.
- Nivel de IA: 1.
- Resultado: RA 3.

## Modelo mental

Antes de usar GitHub, el estudiante debe distinguir:

1. archivos de trabajo;
2. área de preparación;
3. commit local;
4. rama;
5. repositorio remoto.

Git no es sinónimo de GitHub y un commit no es lo mismo que “guardar”.

## Secuencia

| Tiempo | Actividad |
|---:|---|
| 0–15 | Ordenar tarjetas que representan trabajo, `add`, `commit` y `push` |
| 15–35 | Crear un repositorio y observar el estado |
| 35–55 | Primer ciclo pequeño de cambio, preparación y commit |
| 55–70 | Leer el historial y comparar versiones |
| 70–90 | Rama corta, conflicto preparado y resolución guiada |
| 90–108 | Conectar un remoto y discutir GitHub, permisos y colaboración |
| 108–120 | Salida individual: reconstruir el estado a partir de `git status` |

## Comandos mínimos

```bash
git init
git status
git diff
git add archivo.py
git diff --staged
git commit -m "Valida unidades de entrada"
git log --oneline --graph --decorate --all
git switch -c nombre-rama
git remote -v
git push
git pull --ff-only
```

## Criterios de commits científicos

Un buen commit:

- representa una modificación coherente;
- tiene un mensaje que explica la intención;
- no contiene credenciales, resultados enormes ni archivos temporales;
- deja el proyecto en un estado comprensible;
- permite revisar por qué cambió una conclusión.

Mensajes como `actualiza`, `cambios` o `final final` no sirven como evidencia de
proceso.

## Actividad

En parejas, una persona modifica el cálculo y otra agrega una prueba. Deben
integrar ambos cambios, revisar el diff y redactar un commit cuyo mensaje permita
entender la decisión sin abrir los archivos.

## Salida individual

Se entrega una captura textual de `git status`. El estudiante indica qué archivos
están modificados, cuáles están preparados y qué acciones son necesarias antes de
crear un commit limpio.

