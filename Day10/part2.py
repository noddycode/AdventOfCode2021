from collections import deque

char_dict = {r: l for r, l in zip("([{<", ")]}>")}

completions = []

with open("input.txt") as fin:
    for l in fin:
        l = l.strip()
        char_stack = deque()
        is_corrupted = False
        for char in l:
            if char in char_dict.keys():
                char_stack.append(char)
            else:
                char_start = char_stack.pop()
                if char != char_dict[char_start]:
                    is_corrupted = True
                    break

        if not is_corrupted:
            char_stack.reverse() # Reverse it so we run down the stack in order
            completions.append(''.join(char_dict[c] for c in char_stack))

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