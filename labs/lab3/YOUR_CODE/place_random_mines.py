import random
from globals import MINE_SYMBOL

def place_random_mines(board):
    size = len(board)
    while True:
        try: 
            num_mines = int(input(f'Enter number of mines (1-{size * size - 1}): '))
            if num_mines < 1 or num_mines >= size * size:
                print(f'Please enter a number between 1 and {size * size - 1}.')
                continue
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a valid number.')

    mines = []

    while len(mines) < num_mines: 
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)

        if (row, col) not in mines: 
            mines.append((row,col))
            board[row][col] = (MINE_SYMBOL, MINE_SYMBOL)
        print(f'{num_mines} mines have been placed. Begin playing!')
        return mines 
    
