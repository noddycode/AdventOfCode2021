import string
from collections import defaultdict
from copy import copy

node_graph = defaultdict(set)

with open("input.txt") as fin:
    for l in fin:
        l = l.strip()
        node_a, node_b = l.split('-')
        node_graph[node_a].add(node_b)
        node_graph[node_b].add(node_a)

paths = []

def traverse_caves(node, path, visited):
    if node in visited:
        return

    path.append(node)

    if node == 'end':
        paths.append(path)
        return

    # Visit our smaller caves
    if set(node) < set(string.ascii_lowercase):
        visited.add(node)

    for neighbor in node_graph[node]:
        traverse_caves(neighbor, copy(path), copy(visited))



traverse_caves('start', [], set())

print(len(paths))