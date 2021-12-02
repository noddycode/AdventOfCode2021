depth = 0
pos = 0
aim = 0

with open('input.txt') as fin:
    for l in fin:
        instruction, value = (x.lower() for x in l.split() if x)
        value = int(value)

        if instruction.startswith("f"):
            pos += value
            depth += aim*value
        elif instruction.startswith("d"):
            aim += value
        elif instruction.startswith("u"):
            aim -= value

print(depth, pos, aim, depth*pos)