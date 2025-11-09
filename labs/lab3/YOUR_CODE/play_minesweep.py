import globals 
from globals import EMPTY_SYMBOL
from initialize_board import initialize_board
from place_random_mines import place_random_mines
from is_mine_at import is_mine_at

#define play minesweep function to run game
def play_minesweep():
    print('Welcome to Minesweep. Please enter a board size to begin.')
    
    #ask the user for a board size between 0 and 20 because we set 20 to max value in get_valid_input
    size = int(input('Enter board size (0-20): '))
    globals.ROWS = size
    globals.COLS = size

    #define mine_board and hidden_board
    #mine board will hide mines, its what we append in place_random_mines to place hidden mines for guessing
    mine_board = [[(EMPTY_SYMBOL, EMPTY_SYMBOL) for _ in range(size)] for _ in range(size)]
    #hidden board is what the user will see, and what will be appended in is_mine_at if the user guesses correctly 
    hidden_board = initialize_board(size)

    #call to place random mines on the mine_board, then record the mine positions 
    mines = place_random_mines(mine_board)
    globals.MINES = len(mines)

    #call is_mine_at to begin the guessing game with the hidden board, mine board, and list of mine positions
    is_mine_at(hidden_board, mine_board, mines)
    
#call back function to run the game 
play_minesweep()