"""Cliente del paquete fisica_utils."""

from fisica_utils import periodo_pendulo_s


if __name__ == "__main__":
    print(f"T = {periodo_pendulo_s(1.0):.3f} s")

