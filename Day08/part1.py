
# How many segments light up for each number
# Segments: Number
digit_dict = {
    2:  1,
    4: 4,
    3: 7,
    7: 8
}

output_signals = []
with open("input.txt") as fin:
    for l in fin:
        outputs = l.split("|")[1]
        output_signals.extend(x.strip() for x in outputs.split() if x.strip())

count = 0
for signal in output_signals:
    if len(signal) in digit_dict.keys():
        count += 1

print(count)