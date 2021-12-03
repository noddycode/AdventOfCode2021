from statistics import mean

with open("input.txt") as fin:
    lines = list(fin)
    # For i in range [0, 12):
    # Create a list of the ith character in the line
    # Take the mean of all digits
    # Compare the mean to 0.5 to determine if 0 or 1 was more common
    # Convert resulting binary string to integer
    gamma = int(''.join([('1' if mean(int(l[i]) for l in lines) > 0.5 else '0') for i in range(12)]), 2)
    epsilon = int(''.join([('1' if mean(int(l[i]) for l in lines) < 0.5 else '0') for i in range(12)]), 2)
    print(gamma, epsilon, gamma*epsilon)