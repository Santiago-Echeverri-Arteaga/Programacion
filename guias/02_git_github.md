# Guía 02 — Git y GitHub básico

## Ficha

- Realización: martes 1 de septiembre de 2026.
- Duración: un encuentro de 120 minutos, taller el miércoles 2 y aplicación en el
  laboratorio del jueves 3 de septiembre.
- Nivel de IA: 1.
- Resultado: RA 3.

## Modelo mental

Antes de usar GitHub, el estudiante distingue:

1. archivos del directorio de trabajo;
2. área de preparación;
3. commit local;
4. repositorio remoto en GitHub.

Git no es sinónimo de GitHub, un commit no es lo mismo que guardar y `push` no
demuestra que el código sea correcto.

## Secuencia

| Tiempo | Actividad |
|---:|---|
| 0–15 | Ordenar tarjetas que representan trabajo, `add`, `commit` y `push` |
| 15–35 | Crear un repositorio y observar el estado |
| 35–55 | Primer ciclo pequeño de cambio, preparación y commit |
| 55–70 | Leer historial y distinguir commit local de remoto |
| 70–95 | Crear repositorio remoto vacío y conectarlo sin exponer credenciales |
| 95–108 | `push`, verificación en GitHub y errores comunes |
| 108–120 | Salida individual: reconstruir el estado a partir de `git status` |

## Comandos mínimos

```bash
git config --global user.name "Nombre Apellido"
git config --global user.email "correo@example.com"
git init
git status
git diff
git add archivo.md
git diff --staged
git commit -m "Documenta la configuración de WSL2"
git log --oneline
git branch -M main
git remote add origin URL_DEL_REPOSITORIO
git remote -v
git push -u origin main
```

No se requieren ramas adicionales, `merge`, conflictos, `rebase`, `reset` ni
reescritura de historial. `clone` y `pull` se introducen después, cuando exista un
repositorio remoto preparado por el docente.

## Criterios de commits

Un buen commit:

- representa una modificación coherente;
- tiene un mensaje que explica la intención;
- no contiene credenciales ni archivos temporales;
- deja el proyecto en un estado comprensible;
- permite revisar por qué cambió la documentación o el script.

Mensajes como `actualiza`, `cambios` o `final final` no describen la intención.

## Actividad

En parejas, una persona completa la documentación de WSL2 y otra completa el
script secuencial. Revisan el diff, crean dos commits coherentes y publican el
repositorio. El 2 de septiembre se reserva para repetir el flujo y resolver
errores; no añade
comandos evaluables.

## Salida individual

Se entrega una salida textual de `git status`. El estudiante identifica archivos
sin seguimiento, modificados y preparados, y decide qué comando básico procede.
