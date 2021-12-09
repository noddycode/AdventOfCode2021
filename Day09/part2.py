import math

map_width = 0
map_height = 0
map_list = []
with open("input.txt") as fin:
    for l in fin:
        l = l.strip()
        map_width = len(l)
        map_height += 1
        map_list.extend([int(c) for c in l])


def get_adjacent_indices(idx):
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

seen_indices = set()

def find_basin(idx, basin):
    if idx in seen_indices or map_list[idx] == 9:
        return

    basin.add(idx)
    seen_indices.add(idx)

    for adj_idx in get_adjacent_indices(idx):
        find_basin(adj_idx, basin)

basins = []
for i in range(len(map_list)):
    basin = set()
    find_basin(i, basin)
    if basin:
        basins.append(basin)

biggest_basins = sorted(basins, key=lambda x: len(x), reverse=True)[:3]
print(math.prod(len(b) for b in biggest_basins))

