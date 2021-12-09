
map_width = 0
map_height = 0
map_list = []
with open("input.txt") as fin:
    for l in fin:
        l = l.strip()
        map_width = len(l)
        map_height += 1
        map_list.extend([int(c) for c in l])

def get_adjacent_heights(idx):
    adjacent_indices = [
        idx + 1,
        idx - 1,
        idx + map_width,
        idx - map_width
    ]

    # Make sure to check left and right boundaries
    if (idx)%100 == 0:
        adjacent_indices.pop(1)
    elif (idx + 1)%100 == 0:
        adjacent_indices.pop(0)

    return [map_list[i] for i in adjacent_indices if 0 <= i < len(map_list)]

minima = [x for i, x in enumerate(map_list) if x < min(get_adjacent_heights(i))]
risk = sum((x + 1) for x in minima)