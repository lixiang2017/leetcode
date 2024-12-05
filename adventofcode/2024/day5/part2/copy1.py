import os
from collections import deque
from pathlib import Path

answer1 = 0
answer2 = 0

def topological_sort_for_nodes(edges: list[list[str]], nodes: list[str]) -> list[str]:
    # Makes a graph based only on the nodes we are interested in.
    # This slice of the total graph makes a topological sort possible, while the total graph is cyclic.
    graph = {node: [] for node in nodes}
    in_degree = {node: 0 for node in nodes}
    for node_a, node_b in edges:
        if node_a in nodes and node_b in nodes:
            graph[node_a].append(node_b)
            in_degree[node_b] += 1

    # Topological sort
    start_nodes = [node for node, id in in_degree.items() if id == 0]
    sorted_nodes = []
    queue = deque(start_nodes)
    while queue:
        current = queue.pop()
        sorted_nodes.append(current)
        for n_node in graph[current]:
            in_degree[n_node] -= 1
            if in_degree[n_node] == 0:
                queue.append(n_node)
    assert len(sorted_nodes) == len(nodes)
    return sorted_nodes


input_path_from_part1 = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'part1'), 'input')
input_data = Path(input_path_from_part1).read_text(encoding="utf-8")
s1, s2 = input_data.split("\n\n")
edges = [line.split("|") for line in s1.splitlines()]
for line in s2.splitlines():
    updates = line.split(",")
    sorted_updates = topological_sort_for_nodes(edges, updates)
    if updates == sorted_updates:
        answer1 += int(updates[len(updates) // 2])
    else:
        answer2 += int(sorted_updates[len(sorted_updates) // 2])

print(answer1, answer2)
