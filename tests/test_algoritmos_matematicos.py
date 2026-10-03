"""Controles independientes de ejemplos públicos; no contienen claves del taller."""
import math
import subprocess
import sys
from pathlib import Path

import pytest

CARPETA = Path(__file__).resolve().parents[1] / "guias" / "algoritmos_matematicos"
sys.path.insert(0, str(CARPETA))
from biseccion import biseccion
from punto_fijo import punto_fijo
from secante import secante
from derivadas import derivada
from integracion import integrar
from euler import euler
from recurrencia import integrales_recurrentes


@pytest.mark.parametrize("f,a,b,esperado", [
    (lambda x: x - 1, 0, 2, 1),
    (lambda x: x, 0, 2, 0),
    (lambda x: x - 2, 0, 2, 2),
    (lambda x: x*x - 2, 1, 2, math.sqrt(2)),
])
def test_biseccion_raices_y_ancho(f, a, b, esperado):
    resultado, historial = biseccion(f, a, b, tolerancia=1e-10)
    assert resultado == pytest.approx(esperado, abs=1e-10)
    assert historial[-1][2] <= 1e-10 or historial[-1][3] == 0


def test_biseccion_rechaza_intervalo_sin_cambio():
    with pytest.raises(ValueError, match="signo"):
        biseccion(lambda x: x*x + 1, -1, 1)


def test_biseccion_no_confunde_agotamiento_con_raiz():
    resultado, historial = biseccion(lambda x: x*x - 2, 1, 2, max_iter=1)
    assert resultado is None
    assert len(historial) == 1


@pytest.mark.parametrize("valor", [0, -1, math.nan, math.inf, True])
def test_tolerancia_invalida(valor):
    with pytest.raises(ValueError):
        biseccion(lambda x: x, -1, 1, tolerancia=valor)


@pytest.mark.parametrize("valor", [0, -1, 2.5, True])
def test_limite_invalido(valor):
    with pytest.raises(ValueError):
        punto_fijo(lambda x: x / 2, 1, max_iter=valor)


def test_punto_fijo_cero_y_contraccion():
    assert punto_fijo(lambda x: 0, 2)[0] == 0
    assert punto_fijo(lambda x: (x+2)/2, 0)[0] == pytest.approx(2, abs=1e-8)


def test_punto_fijo_no_acepta_solo_cambio_pequeno():
    def g(x):
        return 1e-10 if x == 0 else 10
    resultado, historial = punto_fijo(g, 0, max_iter=1)
    assert resultado is None
    assert historial[0][2] < 1e-8 and historial[0][3] > 1
    assert punto_fijo(lambda x: x+1, 0, max_iter=4)[0] is None


def test_secante_raiz_cero_y_referencia():
    assert secante(lambda x: x, -1, 1)[0] == 0
    resultado, historial = secante(lambda x: x*x - 2, 1, 2)
    assert resultado == pytest.approx(math.sqrt(2), abs=1e-10)
    assert historial[-1][3] <= 1e-8


def test_secante_denominador_nulo_y_agotamiento():
    with pytest.raises(ValueError, match="secante"):
        secante(lambda x: x*x + 1, -1, 1)
    assert secante(lambda x: x*x - 2, 1, 2, max_iter=1)[0] is None


@pytest.mark.parametrize("funcion", [lambda x: float("nan"), lambda x: math.sqrt(-1)])
def test_evaluaciones_invalidas_no_se_presentan_como_exito(funcion):
    with pytest.raises(ValueError):
        secante(funcion, 1, 2)


def test_derivadas_con_funciones_analiticas():
    assert derivada(lambda x: x*x, 3, .2, "adelantada") == pytest.approx(6.2)
    assert derivada(lambda x: x*x, 3, .2) == pytest.approx(6)
    assert derivada(lambda x: 4, 3, .2) == 0


@pytest.mark.parametrize("h", [0, -1, math.nan, 1e-30])
def test_derivada_rechaza_paso_invalido_o_indistinguible(h):
    with pytest.raises(ValueError):
        derivada(lambda x: x*x, 3, h)


@pytest.mark.parametrize("metodo,esperado", [("rectangulos", 1.75), ("trapecios", 2.75), ("simpson", 8/3)])
def test_integracion_tabla_manual(metodo, esperado):
    assert integrar(lambda x: x*x, 0, 2, 5, metodo) == pytest.approx(esperado)
    assert integrar(lambda x: 3, -1, 2, 5, metodo) == pytest.approx(9)


@pytest.mark.parametrize("n", [1, 4, 3.5, True])
def test_simpson_rechaza_numero_de_puntos(n):
    with pytest.raises(ValueError):
        integrar(lambda x: x*x, 0, 1, n, "simpson")


def test_euler_no_evalua_paso_extra():
    llamadas = []
    def pendiente(t, y):
        llamadas.append(t)
        if t >= 1:
            raise ValueError("No debe evaluar aquí")
        return -y
    trayectoria = euler(pendiente, 0, 1, 5, 2)
    assert len(llamadas) == 4
    assert trayectoria == [(0, 2), (.25, 1.5), (.5, 1.125), (.75, .84375), (1, .6328125)]


def test_euler_conserva_constante_y_sigue_recta():
    assert all(y == 7 for _, y in euler(lambda t, y: 0, 0, 2, 9, 7))
    for t, y in euler(lambda t, y: 3, 1, 2, 5, 2):
        assert y == pytest.approx(2+3*(t-1))
    with pytest.raises(ValueError):
        euler(lambda t, y: float("inf"), 0, 1, 5, 2)


def test_recurrencia_indices_y_referencias_independientes():
    valores = integrales_recurrentes(4)
    assert [n for n, _ in valores] == [0, 1, 2, 3]
    # Integrales exactas obtenidas analíticamente para n=0,1,2,3.
    referencias = [1-math.exp(-1), 1-2*math.exp(-1), 2-5*math.exp(-1), 6-16*math.exp(-1)]
    assert [v for _, v in valores] == pytest.approx(referencias)
    with pytest.raises(ValueError):
        integrales_recurrentes(0)


def test_importar_no_imprime_ni_necesita_matplotlib(tmp_path):
    codigo = ("import sys; sys.path.insert(0, " + repr(str(CARPETA)) + "); "
              "import biseccion, punto_fijo, secante, derivadas, integracion, euler, recurrencia; "
              "assert 'matplotlib' not in sys.modules")
    resultado = subprocess.run([sys.executable, "-S", "-c", codigo], cwd=tmp_path,
                               capture_output=True, text=True, check=True)
    assert resultado.stdout == ""
    assert resultado.stderr == ""


@pytest.mark.parametrize("script", ["biseccion.py", "derivadas.py", "integracion.py", "euler.py"])
def test_demo_sin_dependencias_ni_directorio_de_trabajo_fijo(script, tmp_path):
    resultado = subprocess.run([sys.executable, "-S", str(CARPETA/script), "--sin-grafica"],
                               cwd=tmp_path, capture_output=True, check=True)
    assert resultado.stdout
    assert not list(tmp_path.iterdir())
