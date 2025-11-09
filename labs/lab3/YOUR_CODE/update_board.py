#updates players visible board when revealing cells 
def update_board(player_board, row, col, initialize_board):
    player_board[row][col] = initialize_board[row][col]
    