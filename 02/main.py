from itertools import islice
from collections import deque

# Based on sliding window recipe
# https://docs.python.org/3/library/itertools.html#itertools-recipes
with open("input.txt") as fin:
    # As we add new values to the deque, the first value is pushed out the other end
    window = deque((int(x) for x in islice(fin, 3)), maxlen=3)
    last = sum(window)
    count = 0
    for l in fin:
        l = int(l)
        window.append(l)
        if sum(window) > last:
            count += 1
        last = sum(window)

print(count)