import sys

def simulate(lines, n_days):
    day = 0
    generation = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for value in lines.split(","):
        number = int(value)
        generation[number] += 1
    for i in range(1, n_days+1):
        temp = list(generation)
        for j in range(1, 9):
            generation[j-1] += generation[j]
            generation[j] = 0
        generation[0] -= temp[0]
        generation[6] += temp[0]
        generation[8] += temp[0]
    
    return sum(generation)




if __name__ == "__main__":
    file = open(sys.argv[1], "r")
    file_lines = file.readline()
    print("Part1: ", simulate(file_lines, 80))
    print("Part2: ", simulate(file_lines, 256))
    file.close()
