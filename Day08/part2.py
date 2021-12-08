from collections import defaultdict

unique_segment_lengths = {2, 4, 3, 7}

def get_unique(inputs):
    return {
        1: set([x for x in inputs if len(x) == 2][0]),
        4: set([x for x in inputs if len(x) == 4][0]),
        7: set([x for x in inputs if len(x) == 3][0]),
        8: set([x for x in inputs if len(x) == 7][0]),
    }

def get_num_occurrences(inputs, include_unique = True):
    if not include_unique:
        inputs = {x for x in inputs if len(x) not in unique_segment_lengths}

    res_dict = defaultdict(int)
    for input in inputs:
        for letter in input:
            res_dict[letter] += 1

    # Messily overwrites values, but we're only interested in unique ones anyway
    inverted = {count: segment for segment, count in res_dict.items()}

    return inverted

digit_map = {
    "abcefg": '0',
    "cf": '1',
    "acdeg": '2',
    "acdfg": '3',
    "bcdf": '4',
    "abdfg": '5',
    "abdefg": '6',
    "acf": '7',
    "abcdefg": '8',
    "abcdfg": '9'
}

def get_output_num(seg_map, outputs):
    lookup_map = {v: k for k,v in seg_map.items()}

    output_num = ""
    for digit_string in outputs:
        decoded = [lookup_map[x] for x in digit_string]
        search_string = ''.join(sorted(decoded))
        output_num += digit_map[search_string]

    return int(output_num)

total_sum = 0

# with open("sample_input.txt") as fin:  # For testing against the example
# with open("large_sample_input.txt") as fin:  # For testing against the example
with open("input.txt") as fin:
    for l in fin:
        segment_map = {}

        input_string, output_string = [x.strip() for x in l.split("|")]
        inputs = [set(x.strip()) for x in input_string.split()]
        outputs = [x.strip() for x in output_string.split()]

        unique = get_unique(inputs)

        occ_map = get_num_occurrences(inputs)

        segment_map["a"] = (unique[7] - unique[1]).pop()

        segment_map["f"] = occ_map[9]
        segment_map["b"] = occ_map[6]
        segment_map["e"] = occ_map[4]

        segment_map["c"] = (unique[1] - {segment_map["f"]}).pop()

        segment_map["d"] = (unique[4] - {segment_map[x] for x in "cbf"}).pop()

        segment_map["g"] = (set(unique[8]) - set(segment_map.values())).pop()

        total_sum += get_output_num(segment_map, outputs)

print(total_sum)

# Let's look at the digit in the original configuration
#   aaaa
#  b    c
#  b    c
#   dddd
#  e    f
#  e    f
#   gggg

# Now, out of the 9 digits, how many numbers are shared between each segment
# a: 0, 2, 3, 5, 6, 7, 8, 9
# b: 0, 4, 5, 6, 8, 9
# c: 0, 1, 2, 3, 4, 7, 8, 9
# d: 2, 3, 4, 5, 6, 8, 9
# e: 0, 2, 6, 8
# f: 0, 1, 3, 4, 5, 6, 7, 8, 9
# g: 0, 2, 3, 5, 6, 8, 9

# And without the unique segmented numbers
# a: 0, 2, 3, 5, 6, 9
# b: 0, 5, 6, 9
# c: 0, 2, 3, 9
# d: 2, 3, 5, 6, 9
# e: 0, 2, 6
# f: 0, 3, 5, 6, 9
# g: 0, 2, 3, 5, 6, 9

# Segment A: Find 1 and 7, whichever segment is in 7 and not 1 is A
# Segment A alt: Remove 1, 4, 7, and 8: Whichever segment is in exactly 6 digits is A
# Segment F: Find the only common segment between exactly 9 of the digits
# Segment E: Find the only common segment between exactly 4 of the digits
# Segment B: Find the only common segment between exactly 6 of the digits
# Segment C: Find 1, whichever segment is not F from above is C
# Segment D: Find 4, whichever segment that is not mapped to C, B, or F is D
# Segment G:Whatever remains
