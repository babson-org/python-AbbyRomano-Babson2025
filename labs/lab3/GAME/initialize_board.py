#Make sure to import the diamond symbol from globals so it prints below 
from globals import DEFAULT_SYMBOL

#define function to create a board that the user will see. Keep mines hidden, only diamonds showing
def initialize_board(size):
    #create a board, displaying default diamond, for size x by size y given by user
    board = [[DEFAULT_SYMBOL for _ in range(size)] for _ in range(size)]
 
 

