from collections import defaultdict

fish_dict = defaultdict(int)

with open("input.txt") as fin:
    for fish in fin.read().split(','):
        fish_dict[int(fish.strip())] += 1

for i in range(256):
    new_dict = defaultdict(int)
    for time, count in fish_dict.items():
        # Shift each fish count down one
        time -= 1
        # Wrap around if a time has reached 0
        if time < 0:
            new_dict[6] += count
            new_dict[8] += count
        else:
            new_dict[time] += count

        # print(i, new_dict, fish_dict)

    fish_dict = new_dict

print(sum(new_dict.values()))
