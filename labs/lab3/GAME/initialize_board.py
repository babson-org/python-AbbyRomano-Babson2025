from globals import DEFAULT_SYMBOL

def initialize_board(size):
    board = [[DEFAULT_SYMBOL for _ in range(size)] for _ in range(size)]
    print('Player Board: ')
    return board 


