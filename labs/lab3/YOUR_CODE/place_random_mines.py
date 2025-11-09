import random
from globals import MINE_SYMBOL

def place_random_mines(board):
    size = len(board)
    #loop for user to input a number of mines 
    while True:
        try: 
            #f string to ask user for number of mines, ensure at least 1 mine is placed, and one less than total cells on board
            num_mines = int(input(f'Enter number of mines (1-{size * size -1}): '))
            #if number of mines is less than one or greater than or equal to size of board, ask user for different input
            if num_mines < 1 or num_mines >= size * size:
                print(f'Please enter a number between 1 and {size * size - 1}.')
                continue
            break
        #for non-numeric input 
        except ValueError:
            print('Invalid input. Please enter a valid number.')

    #define a list to store mine location (tuples), in row/col format
    mines = []
    #loop that continues until number of mines placed equals user input number of mines
    while len(mines) < num_mines: 
        #user random to assign mines to a row and column within the board size 
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        #if the randomly chosen row, col is not in mines list already, append the list to add tuple and board to have a mine symbol hidden
        if (row, col) not in mines: 
            mines.append((row,col))
            board[row][col] = (MINE_SYMBOL, MINE_SYMBOL)

    print(f'{num_mines} mines have been placed. Begin playing!')
    return mines