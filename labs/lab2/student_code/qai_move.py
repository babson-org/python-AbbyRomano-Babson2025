#AI to select first available cell 
#returns python index 0-8 -> prints 1 for board number 2 
def ai_move(board: list[int]):
    for i in range(len(board)):
        if abs(board[i]) != 10:
            return i 
    pass 
board = [10, 2, 3, 4, -10, 6, 7, 8, 9] 
print(ai_move(board))

#returns the board number 1-9 -> prints 2 for board number 2  
def ai_move_b(board: list[int]):
    for i in range(len(board)):
        if abs(board[i]) != 10: 
            return i + 1
    pass
board = [10, 2,3, 4, -10, 6, 7, 8, 9]
print(ai_move_b(board)) 



"""
        Simple AI that selects the first available cell.
        Remember board is a list that starts with items 1 - 9
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        after two moves with X choosing 1 and O choosing 5 the board looks like:
        [10, 2, 3, 4, -10, 6, 7, 8, 9]
        
        so in this case your function should return 2
    """
    # TODO: Loop through board
    # TODO: Find the first index where abs(cell) != 10
    # TODO: Return that index as the AI's move