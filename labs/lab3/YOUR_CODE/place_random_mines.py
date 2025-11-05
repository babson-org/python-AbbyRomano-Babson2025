import random
from globals import MINE_SYMBOL

def place_random_mines(board):
    size = len(board)
    num_mines = int(input("Enter how many mines to place: "))

#create an empty list to hold mine indexes 
    mines = []
#While loop: while list is shorter than number of mines defined by user,
    while len(mines) < num_mines:
        #loop through rows and columns to chooose a random cell 
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        #if random cell chosen is not in mines list, add it to the list and place a mine symbol on the hidden board 
        if (row, col) not in mines:
            mines.append((row, col)) 
            board[row][col] = MINE_SYMBOL
#confrim correct number of mines have been placed for user, and begin playing
    print(f"{num_mines} mines have been placed. Begin playing!")
    return mines

