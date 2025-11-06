from globals import MINE_SYMBOL
def is_mine_at(mine_board, row, col):
    if row< 0 or col < 0:
        return False
    if row >= len(mine_board) or col >= len(mine_board[0]):
        return False
    return mine_board[row][col] == MINE_SYMBOL 


    