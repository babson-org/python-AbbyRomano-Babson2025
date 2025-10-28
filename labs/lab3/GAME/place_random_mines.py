import random
from globals import MINE_SYMBOL

def place_random_mines(board):
    size = len(board)
    num_mines = int(input("Enter how many mines to place: "))

    mines = []
    while len(mines) < num_mines:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if (row, col) not in mines:
            mines.append((row, col)) 
            board[row][col] = MINE_SYMBOL

    print(f"{num_mines} mines have been placed. Begin playing!")
    return mines

