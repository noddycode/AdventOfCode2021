from collections import deque
from itertools import zip_longest

with open('input.txt') as fin:
    start_chain, polymers = (x.strip() for x in fin.read().split('\n\n'))

    poly_dict = {x.strip(): y.strip() for x, y in  (line.split('->') for line in polymers.split('\n'))}

    print(poly_dict)

chain = start_chain
for i in range(10):
    window = deque(start_chain[0], maxlen=2)
    insertion_list = []

    for char in chain[1:]:
        window.append(char)
        insertion_list.append(poly_dict[''.join(window)])

    new_chain = ''
    for original, new in zip_longest(chain, insertion_list, fillvalue=''):
        new_chain += original+new
    chain = new_chain

print(chain)

max_char = max(chain.count(x) for x in set(chain))
min_char = min(chain.count(x) for x in set(chain))

print([(x, chain.count(x)) for x in set(chain)])
print(max_char - min_char)