from collections import deque, defaultdict
from itertools import zip_longest

# This is an in-between script that documents some of the exploration I was doing to figure out part 2

with open('sample_input.txt') as fin:
    start_chain, polymers = (x.strip() for x in fin.read().split('\n\n'))
    start_chain =start_chain[2:4]
    print(start_chain)

    poly_dict = {x.strip(): y.strip() for x, y in  (line.split('->') for line in polymers.split('\n'))}

    print(sorted(poly_dict.items()))

chain = start_chain

# count_dict = {}.fromkeys(poly_dict.keys(), 0)
for i in range(10):
    count_dict = {}.fromkeys(poly_dict.keys(), 0)
    window = deque(start_chain[:1], maxlen=2)
    insertion_list = []

    for char in chain[1:]:
        window.append(char)
        count_dict[''.join(window)] += 1
        insertion_list.append(poly_dict[''.join(window)])

    print(count_dict)

    new_chain = ''
    for original, new in zip_longest(chain, insertion_list, fillvalue=''):
        new_chain += original+new
    chain = new_chain
    print(chain)

print([(x, chain.count(x)) for x in set(chain)])

max_char = max(chain.count(x) for x in set(chain))
min_char = min(chain.count(x) for x in set(chain))

print(max_char - min_char)