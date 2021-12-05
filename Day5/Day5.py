import sys

def check_line_intersection(file_lines, diagonal):
    positions = {}
    count = 0
    for line in file_lines:
        coordinates = line.split(" -> ")
        x1, y1 = [int(k) for k in coordinates[0].split(",")]
        x2, y2 = [int(k) for k in coordinates[1].split(",")]
        step_y = (y2-y1)//max(abs(y2-y1), 1)
        step_x = (x2-x1)//max(abs(x2-x1), 1)
        if x1 == x2:
            for i in range(y1, y2+step_y, step_y):
                if (x1, i) not in positions.keys():
                    positions[(x1, i)] = 1
                else:
                    positions[(x1, i)] += 1
        elif y1 == y2:
            for i in range(x1, x2+step_x, step_x):
                if (i, y1) not in positions.keys():
                    positions[(i, y1)] = 1
                else:
                    positions[(i, y1)] += 1
        elif diagonal:
            while x1 != x2+step_x:
                if (x1, y1) not in positions.keys():
                    positions[(x1, y1)] = 1
                else:
                    positions[(x1, y1)] += 1
                x1 += step_x 
                y1 += step_y
    

    for key in positions.keys():
        if positions[key] > 1:
            count += 1
    return count



if __name__ == "__main__":
    file = open(sys.argv[1], "r")
    file_lines = file.readlines()
    print("Part1: ", check_line_intersection(file_lines, False))
    print("Part2: ", check_line_intersection(file_lines, True))
    file.close()
