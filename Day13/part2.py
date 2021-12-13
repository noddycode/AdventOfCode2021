def fold_horizontal(point_set, y_fold):
    for point in list(filter(lambda point: point[1] > y_fold, point_set)):
        point_set.remove(point)
        new_point = (point[0], y_fold-abs(y_fold-point[1]))
        point_set.add(new_point) # Naturally overwrites duplicate points

def fold_vertical(point_set, x_fold):
    for point in list(filter(lambda point: point[0] > x_fold, point_set)):
        point_set.remove(point)
        new_point = (x_fold-abs(x_fold-point[0]), point[1])
        point_set.add(new_point) # Naturally overwrites duplicate points

def print_grid(point_set):

    for y in range(max(point[1] for point in point_set)+1):
        line = ''
        for x in range(max(point[0] for point in point_set)+1):
            if (x, y) in point_set:
                line += '#'
            else:
                line += ' '
            line += ' ' # make things a bit more readable

        print(line)

    print('\n')


point_set = set()

with open("input.txt") as fin:
    text = fin.read()
    points, folds = (x.strip() for x in text.split('\n\n'))
    for point in points.split():
        x, y = point.split(',')
        point_set.add((int(x), int(y)))

    for fold in folds.split('\n'):
        fold_eq = fold.split()[-1]
        axis, point = fold_eq.split('=')
        point = int(point)
        if axis == 'y':
            fold_horizontal(point_set, point)
        else:
            fold_vertical(point_set, point)


print_grid(point_set)



print(len(point_set))

