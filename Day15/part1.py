# Hell yeah something I remember from college
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Pseudocode
# https://medium.com/omarelgabrys-blog/path-finding-algorithms-f65a8902eb40
import math
from queue import PriorityQueue

map_width = 0
map_height = 0
map_list = []
with open("input.txt") as fin:
    for l in fin:
        l = l.strip()
        map_width = len(l)
        map_height += 1
        map_list.extend([int(c) for c in l])

def get_adjacent_risks(idx):
    adjacent_indices = [
        idx + 1,
        idx - 1,
        idx + map_width,
        idx - map_width
    ]

    # Make sure to check left and right boundaries
    if (idx)%map_width == 0:
        adjacent_indices.pop(1)
    elif (idx + 1)%map_width == 0:
        adjacent_indices.pop(0)

    return [i for i in adjacent_indices if 0 <= i < len(map_list)]

start_idx = 0
end_idx = len(map_list) - 1

dist_map = {idx: math.inf for idx in range(len(map_list))}
dist_map[start_idx] = 0

previous_node = {}

unvisited = {i for i in range(len(map_list))}
visited = set()

def get_smallest():
    sorted_dist = sorted([(k, v) for k,v in dist_map.items() if k not in visited], key=lambda x: x[1])
    return sorted_dist[0]

while unvisited:
    curr_idx, curr_dist = get_smallest()

    for j in get_adjacent_risks(curr_idx):
        if j in visited:
            continue
        else:
            temp = curr_dist + map_list[j]
            if temp < dist_map[j]:
                dist_map[j] = temp
                previous_node[j] = curr_idx

    unvisited.remove(curr_idx)
    visited.add(curr_idx)

print(dist_map[end_idx])