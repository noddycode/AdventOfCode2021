from collections import defaultdict

with open('input.txt') as fin:
    start_chain, polymers = (x.strip() for x in fin.read().split('\n\n'))

    poly_dict = {x.strip(): y.strip() for x, y in  (line.split('->') for line in polymers.split('\n'))}
    tuple_dict = {}
    for pair, value in poly_dict.items():
        # When we insert a letter between a pair, we end up creating two new pairs
        tuple_dict[pair] = (pair[0]+value, value+pair[1])

count_dict = defaultdict(int)

# Set up the counts for the first line
line_count_dict = defaultdict(int)
for pair in [start_chain[i:i+2] for i in range(len(start_chain)-1)]:
    line_count_dict[pair] += 1

print(line_count_dict)
for i in range(40):
    temp = defaultdict(int)
    for pair, count in line_count_dict.items():
        count_dict[pair] += count
        for result_pair in tuple_dict[pair]:
            temp[result_pair] += count

    line_count_dict = temp

letter_count = defaultdict(int)
for pair, count in count_dict.items():
    letter_count[poly_dict[pair]] += count
for c in start_chain:  # I legit don't even know why I need to do this but I do
    letter_count[c] += 1

print(max(letter_count.values()) - min(letter_count.values()))