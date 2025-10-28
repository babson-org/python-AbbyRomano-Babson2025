from globals import EMPTY_SYMBOL
from initialize_board import initialize_board
from place_random_mines import place_random_mines
from print_board import print_board
from is_mine_at import is_mine_at

def play_minesweeper():
    print('Welcome to Minesweeper. Please enter a board size to begin.')

    size = int(input('Enter board size: '))
    mine_board = [[EMPTY_SYMBOL for _ in range(size)] for _ in range(size)]
    hidden_board = initialize_board(size)

    mines = place_random_mines(mine_board)

    is_mine_at(hidden_board, mine_board, mines)

if __name__ == '__main__':
    play_minesweeper()