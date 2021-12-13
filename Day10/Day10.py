import sys

def get_error_score(char):
    if char == ")":
        return 3
    elif char == "]":
        return 57
    elif char == "}":
        return 1197
    return 25137

def get_completing_char_score(char):
    if char == "(":
        return 1
    elif char == "[":
        return 2
    elif char == "{":
        return 3
    return 4

def get_completing_score(stack):
    total_score = 0
    for char in stack:
        total_score = total_score*5 + get_completing_char_score(char)
    return total_score

def find_errors(lines):
    score = 0
    completing_scores = []
    for line in lines:
        error_line = False
        stack = []
        for char in line:
            if char == "\n":
                continue
            elif char in ("(", "{", "[", "<"):
                stack.insert(0, char)
            elif stack != [] and (ord(char) == ord(stack[0])+2 or ord(char) == ord(stack[0])+1):
                stack.pop(0)
            else:
                score += get_error_score(char)
                error_line = True
                break
        if not error_line:
            completing_scores.append(get_completing_score(stack))
    
    completing_scores.sort()
    print("Part1 {}".format(score))
    print(completing_scores[len(completing_scores)//2])


if __name__ == "__main__":
    file = open(sys.argv[1], "r")
    lines = file.readlines()
    find_errors(lines)
    file.close()
