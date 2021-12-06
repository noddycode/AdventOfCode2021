from collections import deque

with open("input.txt") as fin:
    fish_deque = deque(int(x.strip()) for x in fin.read().split(','))

for i in range(80):
    new_deque = deque()
    for _ in range(len(fish_deque)):
        fish = fish_deque.pop()
        fish -= 1
        if fish < 0:
            fish = 6
            new_deque.append(8)
        new_deque.append(fish)

    fish_deque = new_deque

print(len(fish_deque))
