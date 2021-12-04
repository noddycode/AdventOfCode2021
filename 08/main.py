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

remaining_boards = set(range(len(boards)))

def check_boards(sublist):
    subset = set(sublist)

    for board_num, board_sets in boards.items():
        if board_num not in remaining_boards:
            continue
        if any(board_set < subset for board_set in board_sets):
            # Check if the current winner is the last board before removing it from the set
            if len(remaining_boards) == 1:
                unchecked = set()
                last_board_num = remaining_boards.pop()
                for board_set in boards[last_board_num]:
                    unchecked |= {x for x in board_set - subset}
                score = sum(unchecked) * sublist[-1]
                print(last_board_num, sum(unchecked), sublist[-1], score)
                quit()

            remaining_boards.discard(board_num)

for i in range(4, len(bingo_numbers)):
    sublist = bingo_numbers[:i]
    result = check_boards(sublist)