#count number of mines around a cell 
from globals import MINE_SYMBOL

#define function to count adjacent mines around a specific row and column 
def count_adjacent_mines(row, col, board):
    size = len(board) 
    count = 0
    #For loop to count number of mines around a specific row, col index and add to mine count if found
    for i in range(row - 1, row + 2): 
        for j in range(col - 1, col + 2):
            #skip the middle cell 
            if (i, j) == (row, col):
                continue
            #check if any neighbors are within the board boundaries 
            if 0 <= i < size and 0 <= j < size:
                #if within boundaries and is a mine symbol, increment the count of mines by 1
                if board[i][j] == MINE_SYMBOL:
                    count += 1
   #return total number of mines adjacent to that cell 
    return count



