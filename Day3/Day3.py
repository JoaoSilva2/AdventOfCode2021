def most_common_bit(line_list, index):
    bit_list = [line[index] for line in line_list]
    n_ones, n_zeros = bit_list.count("1"), bit_list.count("0")
    if n_ones >= n_zeros:
        return 1
    return 0

def part2():
    file = open("day3.txt", "r")
    line_list = file.readlines()

    gamma = epsilon = ""

    o_rating_list = list(line_list)
    co2_rating_list = list(line_list)

    for i in range(len(line_list[0])-1):
        bit = most_common_bit(line_list, i)
        epsilon += str(-bit+1)
        gamma += str(bit)

        if(len(o_rating_list) != 1):
            bit = most_common_bit(o_rating_list, i)
            o_rating_list = [line for line in o_rating_list if line[i] == str(bit)]
        if(len(co2_rating_list) != 1):
            bit = -most_common_bit(co2_rating_list, i) + 1
            co2_rating_list = [line for line in co2_rating_list if line[i] == str(bit)]

    print("part1: ", int(gamma, 2)* int(epsilon,2))
    print("part2: ", int(o_rating_list[0], 2) * int(co2_rating_list[0], 2))
    file.close()

part2()
