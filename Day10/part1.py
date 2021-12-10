from collections import deque

right_chars = "([{<"
left_chars = ")]}>"

char_dict = {r: l for r, l in zip(right_chars, left_chars)}

illegal_chars = []

with open("input.txt") as fin:
    for l in fin:
        l = l.strip()
        char_stack = deque()
        for char in l:
            if char in right_chars:
                char_stack.append(char)
            else:
                chunk_start = char_stack.pop()
                if char_dict[chunk_start] != char:
                    illegal_chars.append(char)
                    break

point_dict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

print(sum(point_dict[c] for c in illegal_chars))
