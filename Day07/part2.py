import statistics

with open("input.txt") as fin:
    crab_list = [int(x.strip()) for x in fin.read().split(',')]

# The example target position of "2" matches the median of the example numbers, so let's try that
target_pos = int(statistics.median(crab_list))

fuel = sum([abs(x - target_pos) for x in crab_list])

print(target_pos, fuel)