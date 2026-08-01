"""Punto de partida del laboratorio 6."""

from __future__ import annotations

import os


def main() -> None:
    dsn = os.environ.get("DATABASE_URL")
    if not dsn:
        raise SystemExit("Defina DATABASE_URL sin escribir credenciales en Git")
    # TODO: consultar con psycopg, validar y crear una figura con Matplotlib OO.
    raise NotImplementedError


if __name__ == "__main__":
    main()

