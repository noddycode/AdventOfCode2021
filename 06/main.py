from statistics import mean

def filter_inputs (inputs, i, select_most_common):
    if select_most_common:
        bit_criteria = "1" if mean(int(l[i]) for l in inputs) >= 0.5 else "0"
    else:
        bit_criteria = "1" if mean(int(l[i]) for l in inputs) < 0.5 else "0"

    selected = list(filter(lambda v: v[i] == bit_criteria, inputs))
    print(selected)

    if len(selected) == 1:
        return int(selected[0], 2)
    else:
        return filter_inputs(selected, i+1, select_most_common)


with open("input.txt") as fin:
    lines = [l.strip() for l in fin]
    oxygen = filter_inputs(lines, 0, True)
    scrubber = filter_inputs(lines, 0, False)
    print(oxygen, scrubber, oxygen*scrubber)