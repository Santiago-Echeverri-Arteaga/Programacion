# Secuencia de demostración

```bash
git status
bash generar_datos.sh
git diff
git add mediciones_demo.csv
git diff --staged
git commit -m "Agrega datos mínimos de movimiento"
git log --oneline --decorate
git branch -M main
git remote add origin URL_DEL_REPOSITORIO
git remote -v
git push -u origin main
```

Antes de cada comando, predecir qué estado cambiará.

La configuración del remoto se realiza sobre un repositorio vacío. No se
incluyen ramas adicionales, conflictos, `merge` ni reescritura de historial.
