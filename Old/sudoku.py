import copy

board = [[2, 0, 0], [0, 0, 1], [0, 3, 0]]
#board = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]

found = False
final_board = []

def print_board(board):
    for x in range(len(board)):
        print(board[x])


def sum_of_row(board, row_number):
    row = board[row_number]
    return sum(row)


def sum_of_column(board, col_number):
    column_numbers = []
    for x in range(len(board)):
        column_numbers.append(board[x][col_number])
    return sum(column_numbers)


def check_duplicates(board):
    numbers = []
    for x in range(len(board)):
        for y in range(len(board)):
            numbers.append(board[x][y])
    if len(set(numbers)) == len(numbers):
        return True
    else:
        return False

def chopping_board(board):
    numbers = []
    numbers_to_use = []
    number_of_zeros = 0
    for x in range(len(board)):
        for y in range(3):
            numbers.append(board[x][y])
            if board[x][y] == 0:
                number_of_zeros = number_of_zeros + 1
    check_tool = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for z in check_tool:
        if z not in numbers:
            numbers_to_use.append(z)
    return numbers_to_use, numbers, number_of_zeros


def check_sudoku(board):

    row_sum = sum_of_row(board, 0)
    for x in range(len(board)):
        if sum_of_row(board, x) != row_sum:
            return False
        if sum_of_column(board, x) != row_sum:
            return False
    return True

def generate_board(board):
    global found, final_board
    numbers, _, zeros = chopping_board(board)
    for x in range(len(board)):
        for y in range(3):
            if board[x][y] == 0:
                for z in numbers:
                    board[x][y] = z
                    if zeros == 1:
                        if check_sudoku(board) == True:
                            found = True
                            board_copy = copy.deepcopy(board)
                            if board_copy not in final_board:
                                final_board.append(board_copy)
                    else:
                        generate_board(board)
                    board[x][y] = 0

def generate_board_X(board):
    number = chopping_board(board)
    for x in range(len(board)):
        for y in range(3):
            if board[x][y] == 0:
                board[x][y] = 15 - sum(board[x])
    return board




generate_board(board)
print(final_board) if found else print("Not found")