import pytest

from Libreria import leer_posiciones


def test_archivo_valido(tmp_path):
    ruta = tmp_path / "mediciones.csv"
    ruta.write_text("tiempo_s,posicion_m\n0.0,0.0\n0.1,0.05\n", encoding="utf-8")
    assert leer_posiciones(ruta) == [(0.0, 0.0), (0.1, 0.05)]


@pytest.mark.parametrize("fila,causa", [
    ("0.0,error", "no numérico"),
    ("0.0", "dos columnas"),
    ("0.0,1,2", "dos columnas"),
    ("0.0,nan", "finitos"),
])
def test_fila_invalida(tmp_path, fila, causa):
    ruta = tmp_path / "mediciones.csv"
    ruta.write_text(f"tiempo_s,posicion_m\n{fila}\n", encoding="utf-8")
    with pytest.raises(ValueError, match=f"línea 2:.*{causa}"):
        leer_posiciones(ruta)


def test_sin_mediciones(tmp_path):
    ruta = tmp_path / "mediciones.csv"
    ruta.write_text("tiempo_s,posicion_m\n", encoding="utf-8")
    with pytest.raises(ValueError, match="no contiene"):
        leer_posiciones(ruta)


def test_encabezado_invalido(tmp_path):
    ruta = tmp_path / "mediciones.csv"
    ruta.write_text("tiempo,posicion\n0,0\n", encoding="utf-8")
    with pytest.raises(ValueError, match="línea 1"):
        leer_posiciones(ruta)


def test_archivo_inexistente(tmp_path):
    with pytest.raises(FileNotFoundError):
        leer_posiciones(tmp_path / "ausente.csv")
