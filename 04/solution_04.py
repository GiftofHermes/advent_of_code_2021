class BingoBoard:
    def __init__(self, board):
        self.board = board
        self.matches_row = [0 for row in board]
        self.matches_column = [0 for column in zip(*board)]

    def get_number(self, number):
        for i, row in enumerate(self.board):
            if number in row:
                self.matches_row[i] += 1
        for i, column in enumerate(zip(*self.board)):
            if number in column:
                self.matches_column[i] += 1

    def check_win(self):
        for i, row in enumerate(self.board):
            if len(row) == self.matches_row[i]:
                return True
        for i, column in enumerate(zip(*self.board)):
            if len(column) == self.matches_column[i]:
                return True
        return False


    def total_unmarked_numbers(self, numbers):
        return sum([num for row in self.board for num in row if num not in numbers])

    def __repr__(self):
        return f'row: {self.matches_row} - column: {self.matches_column}'

def parse_line(line, seperator):
    return list(map(lambda x: int(x.strip()), line.split(seperator)))

boards = []
board = None
board_data = []
with open('data/input.txt') as f:
    line = f.readline()
    numbers = parse_line(line, seperator=',')
    f.readline() # skip first line
    for line in f.readlines():
        if line.strip() == '' and board_data:
            board = BingoBoard(board_data)
            boards.append(board)
            board_data = []
        else:
            board_data.append(parse_line(line, None))
    board = BingoBoard(board_data)
    boards.append(board)
def solution1(numbers, boards):
    def find_winning_board(numbers, boards):
        for i, number in enumerate(numbers):
            for board in boards:
                board.get_number(number)
                if board.check_win():
                    last_number = number
                    break
                    if board.check_win():
                        break
        return last_number, board, i
    last_number, board, i  = find_winning_board(last_number, board)
    sum_of_unmarked_numbers = board.total_unmarked_numbers(numbers[0:i+1])

    return sum_of_unmarked_numbers * last_number

def solution2(numbers, boards):
    def find_losing_board(numbers, boards):
        num_boards = len(boards)
        winning_boards = []
        for i, number in enumerate(numbers):
            for board in boards:
                if board in winning_boards:
                    continue
                board.get_number(number)
                if board.check_win():
                    winning_boards.append(board)
                    num_boards -= 1
                if num_boards == 0:
                    last_number = number
                    break
            if num_boards == 0:
                break
        return last_number, board, i
    last_number, board, i = find_losing_board(numbers, boards)
    sum_of_unmarked_numbers = board.total_unmarked_numbers(numbers[0:i+1])

    return sum_of_unmarked_numbers * last_number

print(solution2(numbers, boards))
