CREATE TABLE experimentos (
    id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre text NOT NULL UNIQUE,
    descripcion text NOT NULL,
    fecha_inicio date NOT NULL
);

CREATE TABLE sensores (
    id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    experimento_id integer NOT NULL REFERENCES experimentos(id),
    nombre text NOT NULL,
    magnitud text NOT NULL,
    unidad text NOT NULL,
    ubicacion text,
    UNIQUE (experimento_id, nombre)
);

CREATE TABLE mediciones (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    sensor_id integer NOT NULL REFERENCES sensores(id),
    instante timestamptz NOT NULL,
    valor double precision NOT NULL,
    incertidumbre double precision NOT NULL CHECK (incertidumbre >= 0),
    calidad text NOT NULL DEFAULT 'valida'
        CHECK (calidad IN ('valida', 'sospechosa', 'descartada')),
    UNIQUE (sensor_id, instante)
);

CREATE INDEX mediciones_sensor_instante_idx
    ON mediciones (sensor_id, instante);

COMMENT ON TABLE mediciones IS
    'Datos didácticos sintéticos; no deben presentarse como mediciones reales.';

