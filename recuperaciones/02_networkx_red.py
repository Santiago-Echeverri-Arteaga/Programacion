"""Demo de NetworkX: conectividad y camino de menor costo."""

import networkx as nx

red = nx.Graph()
red.add_weighted_edges_from(
    [
        ("fuente", "sensor_a", 2.0),
        ("fuente", "sensor_b", 1.0),
        ("sensor_a", "laboratorio", 2.0),
        ("sensor_b", "laboratorio", 4.0),
    ]
)

camino = nx.shortest_path(red, "fuente", "laboratorio", weight="weight")
costo = nx.shortest_path_length(red, "fuente", "laboratorio", weight="weight")

print("grados:", dict(red.degree()))
print("red conectada:", nx.is_connected(red))
print("camino mínimo:", camino)
print("costo:", costo)
