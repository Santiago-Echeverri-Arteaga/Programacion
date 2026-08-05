"""Ejemplo de pruebas que sí pertenece a la suite automática."""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest

RUTA_MODULO = Path(__file__).parents[1] / "Codigos" / "02_python_basico" / "movimiento.py"
ESPECIFICACION = spec_from_file_location("movimiento", RUTA_MODULO)
assert ESPECIFICACION is not None and ESPECIFICACION.loader is not None
movimiento = module_from_spec(ESPECIFICACION)
ESPECIFICACION.loader.exec_module(movimiento)
energia_cinetica_j = movimiento.energia_cinetica_j
posicion_mru = movimiento.posicion_mru


def test_posicion_mru_en_tiempo_cero() -> None:
    assert posicion_mru(3.0, 8.0, 0.0) == pytest.approx(3.0)


def test_posicion_mru() -> None:
    assert posicion_mru(1.0, 2.5, 4.0) == pytest.approx(11.0)


def test_tiempo_negativo_se_rechaza() -> None:
    with pytest.raises(ValueError, match="tiempo"):
        posicion_mru(0.0, 1.0, -0.1)


def test_energia_cinetica() -> None:
    assert energia_cinetica_j(2.0, 3.0) == pytest.approx(9.0)


def test_masa_negativa_se_rechaza() -> None:
    with pytest.raises(ValueError, match="masa"):
        energia_cinetica_j(-1.0, 2.0)
