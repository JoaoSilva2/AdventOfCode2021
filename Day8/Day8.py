import sys

class SevenDigitDisplay:
    def __init__(self) -> None:
        self.top = list()
        self.middle = []
        self.bottom = []
        self.top_left = []
        self.bottom_left = []
        self.top_right = []
        self.bottom_right = []

    def solve(self, unique_p):
        #Number 1
        self.bottom_right = [char for char in unique_p[0]]
        self.top_right = list(self.bottom_right)
        #Number 7
        self.top = [char for char in unique_p[1] if char not in self.bottom_right]
        #Number 4
        self.top_left = [char for char in unique_p[2] if char not in self.bottom_right]
        self.middle = list(self.top_left)
        #Number 8
        self.bottom = [char for char in unique_p[-1] if char not in self.middle and char not in self.top_right and char not in self.top]
        self.bottom_left = list(self.bottom)
    
    def check_digit(self, digit_string):
        if len(digit_string) == 2:
            return 1
        elif len(digit_string) == 3:
            return 7
        elif len(digit_string) == 4:
            return 4
        elif len(digit_string) == 7:
            return 8
        elif len(digit_string) == 5 and all([char in digit_string for char in self.bottom]):
            return 2
        elif len(digit_string) == 5 and all([char in digit_string for char in self.top_right]):
            return 3
        elif len(digit_string) == 5:
            return 5
        elif not all([char in digit_string for char in self.middle]):
            return 0
        elif all([char in digit_string for char in self.top_right]):
            return 9
        return 6

def find_unique_seg_numbers(lines):
    count = 0
    result = 0
    for line in lines:
        info = line.split("|")
        output = [string for string in info[1].split(" ") if string != ""]
        output[-1] = output[-1].replace("\n", "")
        unique = list(filter(lambda x: len(x) in (2, 3, 4, 7), output))
        count += len(unique)

        unique_p = sorted(info[0].split(" "), key=len)[1:]
        sdd = SevenDigitDisplay()
        sdd.solve(unique_p)

        mult = 1000
        for string in output:
            value = sdd.check_digit(string)*mult
            result += value
            mult //= 10
    print("Part1: ", count)
    print("Part2: ", result)
    return count


if __name__ == "__main__":
    file = open(sys.argv[1], "r")
    lines = file.readlines()
    find_unique_seg_numbers(lines)
    file.close()
