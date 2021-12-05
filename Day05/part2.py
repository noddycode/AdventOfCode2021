from collections import defaultdict
import math

point_dict = defaultdict(int)

with open("input.txt") as fin:
    for l in fin:
        pairs = l.strip().split()
        x1, y1 = [int(p.strip()) for p in pairs[0].split(',')]
        x2, y2 = [int(p.strip()) for p in pairs[-1].split(',')]

        # Handle diagonals
        if x1 != x2 and y1 != y2:
            # The slope is always going to be 1 or -1, so we can just add or subtract 1 as needed
            step_x = 1 if x2 > x1 else -1
            step_y = 1 if y2 > y1 else -1

            x = x1
            y = y1

            while True:
                point_dict[(x, y)] += 1
                if (x, y) == (x2, y2):
                    break
                x += step_x
                y += step_y

        else:
            # We'll just keep this part the same so we don't have to deal with x1 == x2 or y1 == y2
            start_x, end_x = sorted((x1, x2))
            start_y, end_y = sorted((y1, y2))

            for x in range(start_x, end_x+1):
                for y in range(start_y, end_y+1):
                    point_dict[(x, y)] += 1



print(len([x for x in point_dict.values() if x > 1]))