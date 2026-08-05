"""Ejemplo deliberadamente pequeño de entrada, cálculo y salida."""

longitud_cm = float(input("Longitud [cm]: "))
longitud_m = longitud_cm / 100
print(f"Longitud = {longitud_m:.4f} m")
print(f"Tipo del resultado: {type(longitud_m).__name__}")
