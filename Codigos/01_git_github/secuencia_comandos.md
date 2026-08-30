# Secuencia de demostración

```bash
git status
printf "tiempo_s,posicion_m\n0,0\n1,4.9\n" > mediciones_demo.csv
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

La orden `printf` crea un archivo pequeño para la demostración; no es un script
adicional ni un requisito de memorización.

La configuración del remoto se realiza sobre un repositorio vacío. No se
incluyen ramas adicionales, conflictos, `merge` ni reescritura de historial.
