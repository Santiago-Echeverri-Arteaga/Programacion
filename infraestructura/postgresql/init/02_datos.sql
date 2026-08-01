INSERT INTO experimentos (nombre, descripcion, fecha_inicio) VALUES
    ('Enfriamiento', 'Enfriamiento de una placa después de retirar la fuente térmica', '2026-02-10'),
    ('Radiación ambiental', 'Conteos de fondo en intervalos de un minuto', '2026-02-12');

INSERT INTO sensores (experimento_id, nombre, magnitud, unidad, ubicacion) VALUES
    (1, 'termopar_A', 'temperatura', 'degC', 'centro'),
    (1, 'termopar_B', 'temperatura', 'degC', 'borde'),
    (2, 'geiger_01', 'conteos', '1/min', 'laboratorio');

INSERT INTO mediciones (sensor_id, instante, valor, incertidumbre, calidad) VALUES
    (1, '2026-02-10 14:00:00-05', 82.1, 0.4, 'valida'),
    (1, '2026-02-10 14:05:00-05', 70.2, 0.4, 'valida'),
    (1, '2026-02-10 14:10:00-05', 60.8, 0.4, 'valida'),
    (1, '2026-02-10 14:15:00-05', 53.3, 0.4, 'valida'),
    (2, '2026-02-10 14:00:00-05', 61.5, 0.5, 'valida'),
    (2, '2026-02-10 14:05:00-05', 55.1, 0.5, 'valida'),
    (2, '2026-02-10 14:10:00-05', 49.9, 0.5, 'sospechosa'),
    (2, '2026-02-10 14:15:00-05', 45.7, 0.5, 'valida'),
    (3, '2026-02-12 09:00:00-05', 18, 4.2, 'valida'),
    (3, '2026-02-12 09:01:00-05', 22, 4.7, 'valida'),
    (3, '2026-02-12 09:02:00-05', 17, 4.1, 'valida'),
    (3, '2026-02-12 09:03:00-05', 41, 6.4, 'sospechosa');

