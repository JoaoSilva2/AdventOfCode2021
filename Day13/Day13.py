import sys

max_x = 0 
max_y = 0

def parse_input(file):
    global max_x, max_y
    paper = set()
    folds = []
    for line in file:
        if line == "\n":
            break
        x,y = line.split(",")
        if int(x) > max_x:
            max_x = int(x)
        if int(y) > max_y:
            max_y = int(y)
        paper.add((int(x),int(y)))

    for line in file:
        line = line.split(" ")
        axis,value = line[-1].split("=")
        folds.append((axis,int(value)))
    return (paper, folds)

def count_points(paper, folds, number_folds):
    global max_x, max_y
    for i in range(number_folds):
        axis, axis_value = folds[i]
        aux = list(paper)
        for coord in aux:
            if axis == "x":
                max_x = axis_value - 1
                if coord[0] > axis_value:
                    new_x = -coord[0] + 2*axis_value
                    if new_x >= 0: 
                        paper.add((new_x, coord[1]))
                    paper.remove(coord)
            elif axis == "y":
                max_y = axis_value - 1
                if coord[1] > axis_value:
                    new_y = -coord[1] + 2*axis_value
                    if new_y >= 0: 
                        paper.add((coord[0], new_y))
                    paper.remove(coord)
        if i == 0:
            print("Part 1: {}".format(len(paper)))

    for y in range(max_y+1):
        for x in range(max_x):
            if (x,y) in paper:
                print("#", end="")
            else:
                print(".", end="")
        print("")

    return len(paper)

if __name__ == "__main__":
    file = open(sys.argv[1], "r")
    paper, folds = parse_input(file)
    print("Part 2: {}".format(count_points(paper, folds, len(folds))))
