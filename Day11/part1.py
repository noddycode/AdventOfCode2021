map_width = 0
map_height = 0
map_list = []
with open("input.txt") as fin:
    for l in fin:
        l = l.strip()
        map_width = len(l)
        map_height += 1
        map_list.append([int(c) for c in l])

def get_adjacent(row_idx, col_idx):
    adjacent_indices = [
        (row_idx, col_idx+1), # right
        (row_idx, col_idx-1),  # left
        (row_idx-1, col_idx),  # up
        (row_idx+1, col_idx),  # down
        (row_idx-1, col_idx+1), #upper-right
        (row_idx-1, col_idx-1), #upper-left
        (row_idx+1, col_idx+1), #lower-right
        (row_idx+1, col_idx-1) #lower-left
    ]

    return [(i, j) for i, j in adjacent_indices if 0 <= i < map_height and 0 <= j < map_width]

flashed = set()

def resolve_flash(row_idx, col_idx, num_flashes):
    if (row_idx, col_idx) in flashed:
        return

    if map_list[row_idx][col_idx] > 9:
        flashed.add((row_idx, col_idx))
        for i, j in get_adjacent(row_idx, col_idx):
            map_list[i][j] += 1
            resolve_flash(i, j, num_flashes)

def print_map():
    for row in map_list:
        print(' '.join(str(x) for x in row))
    print('\n')

flashes = 0
for _ in range(100):
    flashed = set()
    map_list = [[y+1 for y in x] for x in map_list]
    for i in range(map_height):
        for j in range(map_width):
            resolve_flash(i, j, 0)
    for i, j in flashed:
        map_list[i][j] = 0

    flashes += len(flashed)



print(flashes)