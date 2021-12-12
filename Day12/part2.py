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

def traverse_caves(node, path, visited, has_visited_twice):
    if (node in visited and has_visited_twice) or ('start' in visited and node == 'start'):
        return

    path.append(node)

    if node == 'end':
        paths.append(path)
        return

    # Visit our smaller caves
    if set(node) < set(string.ascii_lowercase):
        visited[node] += 1
        if visited[node] >= 2:
            has_visited_twice = True


    for neighbor in node_graph[node]:
        traverse_caves(neighbor, copy(path), copy(visited), has_visited_twice)



traverse_caves('start', [], defaultdict(int), False)

print(len(paths))