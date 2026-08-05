"""Ejemplo de limpieza y resumen sin librerías externas."""

registros = [" Caida,9.72 ", "caida,9.81", "PENDULO,1.99", "caida,9.78"]
por_experimento: dict[str, list[float]] = {}

for registro in registros:
    nombre_crudo, valor_crudo = registro.strip().split(",")
    nombre = nombre_crudo.strip().lower()
    por_experimento.setdefault(nombre, []).append(float(valor_crudo))

for nombre, valores in sorted(por_experimento.items()):
    print(nombre, len(valores), sum(valores) / len(valores))
