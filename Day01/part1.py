with open("input.txt") as fin:
    last = int(next(fin))
    count = 0
    for l in fin:
        if int(l) > last:
            count += 1
        last = int(l)

print(count)