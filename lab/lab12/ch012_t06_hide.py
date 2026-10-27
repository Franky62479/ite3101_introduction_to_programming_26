from random import randint
from typing import List

board = []

for x in range(0, 5):
    board.append(["O"] * 5)


def print_board(board_in: List[List[str]]) -> None:
    for row in board_in:
        print(" ".join(row))

# Add your code below!
def random_row(board):
    board = randint(0, len(board_in)-1)
    return board


def random_col(board_in):
        board = randint(0, len(board_in)-1)
    return board
print_board(board)