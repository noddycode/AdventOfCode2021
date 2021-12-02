depth = 0
pos = 0

with open('input.txt') as fin:
    for l in fin:
        instruction, value = (x.lower() for x in l.split() if x)
        value = int(value)

        if instruction.startswith("f"):
            pos += value
        elif instruction.startswith("d"):
            depth += value
        elif instruction.startswith("u"):
            depth -= value

print(depth, pos, depth*pos)