from calc_score import calc_score
def game_over(board: list[int]):
    """
        After every move (see play_game) we check to see if the game 
        is over.  The game is over if calc_score() returns 30 or -30
        or if ther are no open moves left on the board
        Returns True if the game has a winner or no remaining moves, False otherwise.
    """
    
    # TODO: Check if any rows/diagonals if board = 30 by setting calc_score function equal to score and then telling it what to print when it receives 30 or -30 from calc_score
    score = calc_score(board)
    if score == 30:
        print('X wins!')
        return True
    if score == -30:
        print ('O wins!')
        return True
    
    #Loop through each cell on the board to see if there are any open spaces left, if true loop breaks, if not true, will print its a tie
    has_open_space = False 
    for cell in board: 
        if 1 <= cell <= 9: 
            has_open_space = True
            break
    if not has_open_space:
        print('Its a tie!')
        return True 
    
    #do nothing if there are still open spaces and nothing equals 30 or -30 from calc_score 
    return False 



    # TODO: Use calc_score to check if someone has won
    # TODO: Return True if game over, otherwise False
    pass

    