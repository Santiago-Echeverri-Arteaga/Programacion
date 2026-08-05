import pytest

from estadistica import promedio


def test_un_valor() -> None:
    assert promedio([4.2]) == pytest.approx(4.2)


def test_valores_con_signo() -> None:
    assert promedio([-1.0, 1.0]) == pytest.approx(0.0)


def test_lista_vacia() -> None:
    with pytest.raises(ValueError, match="vacía"):
        promedio([])

