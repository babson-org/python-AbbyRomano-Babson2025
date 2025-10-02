from calc_score import calc_score
def game_over(board: list[int]):
    """
        After every move (see play_game) we check to see if the game 
        is over.  The game is over if calc_score() returns 30 or -30
        or if ther are no open moves left on the board
        Returns True if the game has a winner or no remaining moves, False otherwise.
    """
    
    # TODO: Check if all cells are filled (abs(cell) == 10)
    has_open_space = False
    for cell in board: 
        if 1<= cell <= 9:
            has_open_space = True 
            break 
    if not has_open_space: 
        print('Its a tie!')
        return True
    
    score = calc_score(board)
    if score == 30:
        print('X Wins!')
        return True 
    if score == -30: 
        print('Y Wins')
        return True
    
   
    return False


    # TODO: Use calc_score to check if someone has won
    # TODO: Return True if game over, otherwise False
    pass

    