"""Ejecutar en Ubuntu WSL, después de preparar la base y el entorno virtual."""
import psycopg
# Socket Unix + autenticación peer: usa el usuario actual de Ubuntu, sin contraseña.
# El rol del mismo nombre y la base se crean siguiendo GUIA_POSTGRESQL.md.
with psycopg.connect(dbname="curso_datos") as con:
    with con.cursor() as cur:
        cur.execute(
            "SELECT registro_id, especie, masa_g FROM curso_penguins.observaciones "
            "WHERE especie=%s AND masa_g>=%s ORDER BY registro_id",
            ("Gentoo", 5500),
        )
        print([col.name for col in cur.description])
        for fila in cur.fetchall():
            print(fila)
