import pytest

from modelo import periodo_pendulo


def test_periodo_un_metro():
    assert periodo_pendulo(1.0) == pytest.approx(2.006, rel=1e-3)


def test_rechaza_longitud_no_positiva():
    with pytest.raises(ValueError):
        periodo_pendulo(0.0)
