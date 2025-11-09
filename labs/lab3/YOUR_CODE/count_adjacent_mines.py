#count number of mines around a cell 
from globals import MINE_SYMBOL

def count_adjacent_mines(row, col, board):
    size = len(board) 
    count = 0
    #For loop to count number of mines around a specific row, col index and add to mine count if found
    for i in range(row - 1, row + 2): 
        for j in range(col - 1, col + 2):
            if (i, j) == (row, col):
                continue
            if 0 <= i < size and 0 <= j < size:
                if board[i][j] == MINE_SYMBOL:
                    count += 1
    return count



