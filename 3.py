import networkx as nx


def dijkstra_shortest_path(graph, start):
    return nx.single_source_dijkstra_path_length(graph, start)


G = nx.Graph()

stations = ['Station A', 'Station B', 'Station C', 'Station D', 'Station E', 'Station F', 'Station G']
G.add_nodes_from(stations)

weighted_routes = [
    ('Station A', 'Station B', 2),
    ('Station A', 'Station C', 1),
    ('Station B', 'Station C', 4),
    ('Station C', 'Station D', 7),
    ('Station D', 'Station E', 3),
    ('Station E', 'Station F', 2),
    ('Station F', 'Station G', 5),
    ('Station G', 'Station A', 6),
    ('Station C', 'Station F', 3)
]

G.add_weighted_edges_from(weighted_routes)

shortest_paths_from_all_nodes = {node: dijkstra_shortest_path(G, node) for node in G.nodes()}

for key, value in shortest_paths_from_all_nodes.items():
    print(f"{key}:")
    if isinstance(value, dict):
        for node, degree in value.items():
            print(f"  - {node}: {degree}")
    else:
        print(f"  {value}")
