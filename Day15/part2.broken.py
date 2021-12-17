# Hell yeah something I remember from college
# We'll use A* this time
# https://www.youtube.com/watch?v=eSOJ3ARN5FM
import math
import queue

map_width = 0
map_height = 0
map_list = []
with open("sample_input.txt") as fin:
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

#https://softwareengineering.stackexchange.com/questions/212808/treating-a-1d-data-structure-as-2d-grid
def get_straigh_line_dist(idx1, idx2):
    x1, x2 = (idx%map_width for idx in (idx1, idx2))
    y1, y2 = (idx//map_width for idx in (idx1, idx2))

    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


start_idx = 0
end_idx = len(map_list) - 1

dist_map = {idx: math.inf for idx in range(len(map_list))}
dist_map[start_idx] = 0

heuristic_map = {idx:get_straigh_line_dist(idx, end_idx) for idx in range(len(map_list))}

previous_node = {}

q = queue.PriorityQueue()

weight_map = {}
open_indices = {start_idx}
closed_indices = set()
current_idx = start_idx
weight = dist_map[current_idx] + heuristic_map[current_idx]
weight_map[current_idx] = weight

while current_idx != end_idx:
    open_indices.remove(current_idx)
    closed_indices.add(current_idx)
    adj = get_adjacent_risks(current_idx)
    for i in adj:
        if i in closed_indices or i in open_indices:
            continue
        else:
            open_indices.add(i)
            dist_map[i] = dist_map[current_idx] + map_list[i]
            temp = dist_map[i] + heuristic_map[i]
            q.put((temp, i))
            # In case we want to animate this later
            previous_node[i] = current_idx

    next_val = q.get()
    current_idx = next_val[1]

print(next_val)