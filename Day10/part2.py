from collections import deque

left_chars = "([{<"
right_chars = ")]}>"

char_dict = {r: l for r, l in zip(left_chars, right_chars)}

completions = []

def is_corrupted(line):
    char_stack = deque()
    for char in line:
        if char in left_chars:
            char_stack.append(char)
        else:
            chunk_start = char_stack.pop()
            if char_dict[chunk_start] != char:
                return True

    return False

with open("input.txt") as fin:
    for l in fin:
        l = l.strip()
        # Probably a better way do to this without processing each line twice but...
        # Oh well
        if is_corrupted(l):
            continue
        else:
            char_stack = deque()
            for char in l:
                if char in left_chars:
                    char_stack.append(char)
                else:
                    # Don't need to check because we know it's not corrupted
                    chunk_start = char_stack.pop()

            completion = ''
            char_stack.reverse()  # Reverse it so we run down the stack in order
            for char in char_stack:
                completion += char_dict[char]
            completions.append(completion)


point_dict = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

scores = []

for completion in completions:
    score = 0
    for char in completion:
        score *= 5
        score += point_dict[char]

    scores.append(score)

mid = sorted(scores)[len(scores)//2]

print(mid)