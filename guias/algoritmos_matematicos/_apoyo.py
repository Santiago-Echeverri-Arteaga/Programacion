"""Validación y presentación compartidas; los algoritmos están en cada ejemplo.

Python 3.12+. Las anotaciones documentan tipos: las comprobaciones ejecutables
hacen cumplir las precondiciones. Matplotlib solo se importa al crear figuras.
"""
from __future__ import annotations

import argparse
import math
from collections.abc import Callable, Sequence
from numbers import Real
from pathlib import Path
from typing import TYPE_CHECKING
from types import ModuleType

if TYPE_CHECKING:
    from matplotlib.figure import Figure

Funcion = Callable[[float], float]
# Cada fila: iteración, aproximación, medida de cambio, residuo absoluto.
Historial = list[tuple[int, float, float, float]]


def real_finito(valor: float, nombre: str) -> float:
    """Acepta un real finito (también int), excluye bool; devuelve float.

    Lanza ValueError si el tipo o el valor no cumple el contrato.
    No modifica la entrada y no imprime.
    """
    if isinstance(valor, bool) or not isinstance(valor, Real):
        raise ValueError(f"{nombre} debe ser un número real")
    try:
        numero = float(valor)
    except (OverflowError, ValueError) as error:
        raise ValueError(f"{nombre} no es representable como float finito") from error
    if not math.isfinite(numero):
        raise ValueError(f"{nombre} debe ser finito")
    return numero


def entero_positivo(valor: int, nombre: str, minimo: int = 1) -> int:
    """Devuelve un int >= minimo; rechaza booleanos y lanza ValueError si falla."""
    if isinstance(valor, bool) or not isinstance(valor, int) or valor < minimo:
        raise ValueError(f"{nombre} debe ser entero >= {minimo}")
    return valor


def controles(tolerancia: float, max_iter: int) -> tuple[float, int]:
    """Valida tolerancia real finita > 0 y máximo entero >= 1; devuelve ambos."""
    tolerancia = real_finito(tolerancia, "tolerancia")
    if tolerancia <= 0:
        raise ValueError("tolerancia debe ser positiva")
    return tolerancia, entero_positivo(max_iter, "max_iter")


def evaluar(funcion: Funcion, x: float) -> float:
    """Evalúa una función escalar en x finito; exige resultado real finito.

    Requiere una función determinista sin efectos secundarios. Los fallos de
    dominio/división/desbordamiento se comunican como ValueError con el punto;
    otros errores de programación no se ocultan.
    """
    x = real_finito(x, "punto de evaluación")
    try:
        valor = funcion(x)
    except (ValueError, OverflowError, ZeroDivisionError) as error:
        raise ValueError(f"No se pudo evaluar la función en x={x}: {error}") from error
    return real_finito(valor, "resultado de la función")


def tabla(titulo: str, columnas: Sequence[str], filas: Sequence[Sequence[object]]) -> None:
    """Imprime una tabla alineada sin alterar datos; cada fila debe tener igual ancho.

    Los float se muestran con diez cifras significativas; el formato no cambia
    la precisión de los valores calculados. Lanza ValueError si faltan columnas.
    """
    texto = [[f"{v:.10g}" if isinstance(v, float) else str(v) for v in fila] for fila in filas]
    if any(len(fila) != len(columnas) for fila in texto):
        raise ValueError("Las filas deben coincidir con las columnas")
    anchos = [max(len(c), max((len(f[i]) for f in texto), default=0)) for i, c in enumerate(columnas)]
    print(f"\n{titulo}\n{'=' * len(titulo)}")
    print(" | ".join(c.ljust(a) for c, a in zip(columnas, anchos)))
    print("-+-".join("-" * a for a in anchos))
    for fila in texto:
        print(" | ".join(c.rjust(a) for c, a in zip(fila, anchos)))


def opciones() -> argparse.Namespace:
    """Lee opciones de presentación; por defecto guarda PNG sin abrir ventanas."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sin-grafica", action="store_true", help="Solo tabla, sin Matplotlib")
    parser.add_argument("--mostrar", action="store_true", help="Abrir la figura además de guardarla")
    parser.add_argument("--salida", type=Path, default=Path(__file__).resolve().parent / "figuras",
                        help="Carpeta para PNG; por defecto figuras junto a las guías")
    return parser.parse_args()


def preparar_grafica(mostrar: bool = False) -> ModuleType:
    """Devuelve pyplot configurado; requiere Matplotlib solo en modo gráfico.

    Si falta la dependencia, indica el comando de instalación o modo sin gráfica.
    El modo predeterminado usa Agg y no necesita escritorio gráfico.
    """
    try:
        import matplotlib
    except ImportError as error:
        raise RuntimeError("Instala matplotlib: python -m pip install matplotlib; o usa --sin-grafica") from error
    if not mostrar:
        matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "axes.grid": True,
                         "grid.alpha": 0.18, "figure.facecolor": "#f6f8fc",
                         "axes.facecolor": "white", "axes.titleweight": "bold"})
    return plt


def guardar_figura(figura: Figure, carpeta: Path, nombre: str, mostrar: bool = False) -> Path:
    """Guarda PNG de una figura en carpeta (la crea); opcionalmente muestra y cierra.

    Devuelve la ruta absoluta. Los errores de escritura se propagan.
    """
    import matplotlib.pyplot as plt
    carpeta.mkdir(parents=True, exist_ok=True)
    ruta = (carpeta / nombre).resolve()
    figura.savefig(ruta, dpi=160, bbox_inches="tight")
    print(f"\nFigura guardada: {ruta}")
    if mostrar:
        plt.show()
    plt.close(figura)
    return ruta
