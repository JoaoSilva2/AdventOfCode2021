import sys

def read_increase_decrease(filename):
    file = open(filename, "r")
    result = 0
    previous_value = int(file.readline())
    for line in file.readlines():
        current_value = int(line)
        if previous_value < current_value:
            result += 1
        previous_value = current_value
    return result

def read_increase_decrease_part2(filename):
    file = open(filename, "r")
    result = 0

    lines = [int(line) for line in file.readlines()]

    counter = 1
    previous_value = lines[0] + lines[1] + lines[2]

    while counter < len(lines) - 2:
        current_value = lines[counter] + lines[counter+1] + lines[counter+2]
        if previous_value < current_value:
            result += 1
        previous_value = current_value
        counter += 1

    print(lines[counter])

    return result



if __name__ == "__main__":
    print(read_increase_decrease(sys.argv[1]))
    print(read_increase_decrease_part2(sys.argv[1]))
