class BingoBoard:
    def __init__(self, size) -> None:
        self.bingoed = False
        self.size = size
        self.numbers = []
    def add_numbers(self, numbers):
        self.numbers.append(numbers)
    def get_number(self, i, j):
        return self.numbers[i][j]
    def remove_number(self, number):
        for i in range(self.size):
            for j in range(self.size):
                if self.numbers[i][j] == number:
                    self.numbers[i][j] = -1
                    break
    def check_rows(self):
        return self.numbers.count([-1]*5) > 0
    def check_columns(self):
        transposed = []
        for i in range(self.size):
            transposed.append([self.get_number(j, i) for j in range(self.size)])
        return transposed.count([-1]*5) > 0
    def check_bingo(self):
        return self.check_rows() or self.check_columns() 
    def sum_unmarked(self):
        total_sum = 0
        for line in self.numbers:
            total_sum += sum(line) + line.count(-1)
        return total_sum

class BoardAssistant:
    def __init__(self, numbers) -> None:
        self.boards = []
        self.numbers = numbers
    def add_board(self, board):
        self.boards.append(board)
    def start_bingo(self):
        boards_bingoed = [i for i in range(len(self.boards))]
        winner = False
        for number in self.numbers:
            for i in range(len(self.boards)):
                self.boards[i].remove_number(number)
                if self.boards[i].check_bingo():
                    unmarked_sum = self.boards[i].sum_unmarked()
                    #Last to win------------------------------------------------
                    if len(boards_bingoed) == 1 and not self.boards[i].bingoed:
                        unmarked_sum_2 = self.boards[boards_bingoed[0]].sum_unmarked()
                        print("Part2: ", unmarked_sum_2*number)
                        return
                    #-----------------------------------------------------------
                    #First to win-----------------------------------------------
                    if not winner:
                        print("Part1: ", unmarked_sum*number)
                        winner = True
                    #-----------------------------------------------------------
                    if i in boards_bingoed:
                        boards_bingoed.remove(i)
                    self.boards[i].bingoed = True
        return

def main():
    file = open("day4.txt", "r")
    called_numbers = list(map(lambda x: int(x), file.readline().split(",")))
    assistant = BoardAssistant(called_numbers)

    lines = file.readlines()
    i = 0
    while i < len(lines):
        if lines[i] == "\n":
            i+=1
            continue

        board = BingoBoard(5)
        for j in range(5):
            number_line = filter(lambda y: y != "", lines[j+i].split(" "))
            board_row = list(map(lambda x: int(x), list(number_line)))
            board.add_numbers(board_row)

        assistant.add_board(board)
        i += 5
    
    assistant.start_bingo()

if __name__ == "__main__":
    main()
