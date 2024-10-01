import networkx as nx


def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return path
    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs(graph, neighbor, goal, path)
            if new_path:
                return new_path
    return None


def bfs(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for neighbor in graph[vertex]:
            if neighbor not in path:
                if neighbor == goal:
                    return path + [neighbor]
                else:
                    queue.append((neighbor, path + [neighbor]))
    return None


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

graph_dict = nx.to_dict_of_lists(G)

start_node = 'Station A'
goal_node = 'Station F'

dfs_path = dfs(graph_dict, start_node, goal_node)
bfs_path = bfs(graph_dict, start_node, goal_node)

results = {
    "DFS шлях": dfs_path,
    "BFS шлях": bfs_path
}

for key, value in results.items():
    print(f"{key}:")
    if isinstance(value, dict):
        for node, degree in value.items():
            print(f"  - {node}: {degree}")
    else:
        print(f"  {value}")
