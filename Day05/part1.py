from collections import defaultdict

point_dict = defaultdict(int)

with open("input.txt") as fin:
    for l in fin:
        pairs = l.strip().split()
        x1, y1 = [int(p.strip()) for p in pairs[0].split(',')]
        x2, y2 = [int(p.strip()) for p in pairs[-1].split(',')]

        # Throw out diagonal lines
        if x1 != x2 and y1 != y2:
            continue

        # x1 and x2 OR y1 and y2 will be the same, so we don't have to worry about splitting up our points
        start_x, end_x = sorted((x1, x2))
        start_y, end_y = sorted((y1, y2))

        for x in range(start_x, end_x+1):
            for y in range(start_y, end_y+1):
                point_dict[(x, y)] += 1


print(len([x for x in point_dict.values() if x > 1]))