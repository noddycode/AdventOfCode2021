import math
import queue

map_width = 0
map_height = 0
map_list = []
with open("input.txt") as fin:
    for l in fin:
        l = l.strip()
        map_width = len(l)
        map_height += 1
        map_list.extend([int(c) for c in l])

variations = [map_list]
for i in range(8):  # There are 8 total variations
    temp = [(x+1 if x<9 else 1) for x in variations[-1]]
    variations.append(temp)

new_map_list = []
for i in range(5):
    for j in range(map_height):
        for k in range(i, i+5):
            new_map_list.extend(variations[k][j*map_width:j*map_width+map_width])

map_list = new_map_list
map_width *= 5
map_height *= 5

# for i in range(map_height):
#     print(''.join(str(x) for x in map_list[i*map_width: i*map_width + map_width]))

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


q = queue.PriorityQueue()

start_idx = 0
end_idx = len(map_list) - 1

dist_map = {idx: math.inf for idx in range(len(map_list))}
dist_map[start_idx] = 0
q.put((0, start_idx))
visited = set()


while not q.empty():
    curr_dist, curr_idx = q.get()

    for j in get_adjacent_risks(curr_idx):
        if j in visited:
            continue
        else:
            temp = curr_dist + map_list[j]
            if temp < dist_map[j]:
                dist_map[j] = temp
                q.put((temp, j))

    visited.add(curr_idx)

print(dist_map[end_idx])