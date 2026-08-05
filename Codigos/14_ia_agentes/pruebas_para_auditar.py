"""Pruebas iniciales: algunas fallan y otras verificaciones aún faltan.

Se ejecuta de forma explícita durante la clase:
    pytest Codigos/14_ia_agentes/pruebas_para_auditar.py
"""

import math

import pytest

from caida_ia_defectuosa import energia_cinetica, tiempo_caida


def test_tiempo_caida_desde_20_metros() -> None:
    esperado = math.sqrt(2 * 20.0 / 9.81)
    assert tiempo_caida(20.0) == pytest.approx(esperado)


def test_energia_cinetica() -> None:
    assert energia_cinetica(2.0, 3.0) == pytest.approx(9.0)


def test_altura_cero() -> None:
    assert tiempo_caida(0.0) == 0.0
