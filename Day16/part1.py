def hex_to_binary(hex_string):
    # Custom comprehension to maintain leading 0s
    return ''.join((format(int(x, 16), '04b') for x in hex_string))

def get_version_type(binary_string):
    version, type = (int(x, 2) for x in (binary_string[:3], binary_string[3:6]))
    print(binary_string[:3], binary_string[3:6])
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
                bits_read = process_packet(input[total_bits:sublength])
                total_bits += bits_read
            input = input[sublength:]
        else:
            num_packets, input = get_num_subpackets(input)
            for i in range(num_packets):
                bits_read = process_packet(input)
                input = input[bits_read:]

    return start_length - len(input)

with open("input.txt") as fin:
    process_packet(hex_to_binary(fin.read().strip()))
print(version_count)
