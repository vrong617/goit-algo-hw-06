import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

stations = ['Station A', 'Station B', 'Station C', 'Station D', 'Station E', 'Station F', 'Station G']
G.add_nodes_from(stations)

routes = [
    ('Station A', 'Station B'),
    ('Station A', 'Station C'),
    ('Station B', 'Station C'),
    ('Station C', 'Station D'),
    ('Station D', 'Station E'),
    ('Station E', 'Station F'),
    ('Station F', 'Station G'),
    ('Station G', 'Station A'),
    ('Station C', 'Station F')
]
G.add_edges_from(routes)

plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold', edge_color='gray')
plt.title("Транспортна мережа міста")
plt.show()

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_of_nodes = dict(G.degree())

info = {
    "Кількість вершин": num_nodes,
    "Кількість ребер": num_edges,
    "Ступінь кожної вершини": degree_of_nodes
}

for key, value in info.items():
    print(f"{key}:")
    if isinstance(value, dict):
        for node, degree in value.items():
            print(f"  - {node}: {degree}")
    else:
        print(f"  {value}")
