import statistics

with open("input.txt") as fin:
    crab_list = [int(x.strip()) for x in fin.read().split(',')]

# crab_list = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

# Summation of a series of natural numbers:
# https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF
# So we just need to plug each fuel number into
# (n(n+1))/2
# Then we'll just brute force it and narrow down results until we find the smallest value
def get_lowest(test_target, previous_best):
    test_points = (test_target - 1, test_target+1)
    results = []
    # Get fuel cost on either side of the test point
    for test_point in test_points:
        sum = 0
        for crab in crab_list:
            dist = abs(crab - test_point)
            sum += (dist * (dist + 1))/2 # (n(n+1))/2
        results.append(sum)

    if previous_best < min(results):  # Nothing on either side of our goal is better than what we had
        print(int(previous_best))
    else:
        get_lowest(test_points[results.index(min(results))], min(results))  # Convoluted way of returning the index of the lowest value test target


# Starting with our best guess: the median of all values
get_lowest(statistics.median(crab_list), float('inf'))