from collections import defaultdict
from itertools import islice, chain

with open("input.txt") as fin:
    bingo_numbers = [int(x.strip()) for x in next(fin).split(',')]
    boards = defaultdict(list)
    for i, board_string in enumerate(fin.read().split('\n\n')):
        # We'll add the boards as a single list and math them into individual sets.
        board = [int(x.strip()) for x in board_string.split()]
        # https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
        boards[i].extend([set(board[j : j + 5]) for j in range(0, len(board), 5)]) # Rows
        boards[i].extend([set(islice(board, j, None, 5)) for j in range(5)]) # Columns

def check_boards(sublist):
    subset = set(sublist)
    for board_num, board_sets in boards.items():
        if any(board_set < subset for board_set in board_sets):
            # Grab all the unchecked numbers
            unchecked = set()
            for board_set in board_sets:
                unchecked |= {x for x in board_set - subset}
            score = sum(unchecked) * sublist[-1]
            print(board_num, sum(unchecked), sublist[-1], score)
            quit()

for i in range(4, len(bingo_numbers)):
    sublist = bingo_numbers[:i]
    result = check_boards(sublist)