import pytest

from Libreria import integrar_cuadrado, primos, velocidad


def test_velocidad_y_signo():
    assert velocidad(20, 5) == pytest.approx(4.0)
    assert velocidad(-20, 5) == pytest.approx(-4.0)


@pytest.mark.parametrize("intervalo", [0, -5, float("nan")])
def test_intervalo_invalido(intervalo):
    with pytest.raises(ValueError):
        velocidad(20, intervalo)


def test_primos_en_frontera():
    assert primos(1) is False
    assert primos(2) is True
    assert primos(4) is False


def test_punto_medio_manual():
    assert integrar_cuadrado(0, 1, 1) == pytest.approx(0.25)


def test_reduccion_error_en_caso_conocido():
    error_4 = abs(integrar_cuadrado(0, 1, 4) - 1 / 3)
    error_8 = abs(integrar_cuadrado(0, 1, 8) - 1 / 3)
    assert error_8 < error_4


@pytest.mark.parametrize("n", [0, -1, 2.5])
def test_subintervalos_invalidos(n):
    with pytest.raises(ValueError):
        integrar_cuadrado(0, 1, n)
