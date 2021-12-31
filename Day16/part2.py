import itertools
import operator


def hex_to_binary(hex_string):
    # Custom comprehension to maintain leading 0s
    return ''.join((format(int(x, 16), '04b') for x in hex_string))

def get_version_type(binary_string):
    version, type = (int(x, 2) for x in (binary_string[:3], binary_string[3:6]))
    return version, type, binary_string[6:]

def type_4(input):
    res = ''
    i = 0
    while True:
        indicator = input[i]
        bits = input[i+1: i+5]
        res += bits
        i+=5
        if indicator == '0':
            break


    return int(res, 2), input[i:]

def get_length_subpackets(input):
    return int(input[:15], 2), input[15:]

def get_num_subpackets(input):
    return int(input[:11], 2), input[11:]


version_count = 0

def process_packet(input):
    val = None
    vals = []
    if not input:
        return 0
    start_length = len(input)  # Keep track of how many bits we process
    global version_count
    version, type, input = get_version_type(input)
    version_count += version

    if type == 4:
        val, input = type_4(input)

    else:
        length_type = input[0]
        input = input[1:]
        total_bits = 0
        if length_type == '0':
            sublength, input = get_length_subpackets(input)
            while total_bits < sublength:
                bits_read, val = process_packet(input[total_bits:sublength])
                vals.append(val)
                total_bits += bits_read
            input = input[sublength:]
        else:
            num_packets, input = get_num_subpackets(input)
            for i in range(num_packets):
                bits_read, val = process_packet(input)
                vals.append(val)
                input = input[bits_read:]

        if type == 0:
            val = sum(vals)
        elif type == 1:
            # https://stackoverflow.com/questions/51715051/cumulative-product-in-python
            val = list(itertools.accumulate(vals, operator.mul))[-1]
        elif type == 2:
            val = min(vals)
        elif type == 3:
            val = max(vals)
        elif type == 5:
            val = int(vals[0] > vals[1])
        elif type == 6:
            val = int(vals[0] < vals[1])
        elif type == 7:
            val = int(vals[0] == vals[1])


    return start_length - len(input), val

# with open("input.txt") as fin:
#     res = process_packet(hex_to_binary(fin.read().strip()))

# for str in (("C200B40A82", "04005AC33890", "880086C3E88112", "CE00C43D881120", "D8005AC2A8F0", "F600BC2D8F", "9C005AC2F8F0", "9C0141080250320F1802104A08")):
#     res = process_packet(hex_to_binary(str))
#
#     print(res[1])

with open('input.txt') as fin:
    res = process_packet(hex_to_binary(fin.read().strip()))

    print(res[1])
