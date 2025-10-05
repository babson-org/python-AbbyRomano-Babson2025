    
def player_move(board: list[int], score: dict[str, int]):
    """
        Prompts the player to choose a valid move.
        Remember score is a dictionary from play_game()
        It has two keys 'player' and 'ai' associated values
        are 10 and -10 depending on who goes first.
    """
    
    prompt = "Select an empty cell (1-9): "
    #use a while loop to validate that each move is either open or within the index
    while True:
        try:
            # TODO: Convert input to integer, & create index so its easier to validate if move is not taken
            idx = int(input(prompt)) - 1
            # TODO: Validate move is in range and not taken
            if idx < 0 or idx > 8: 
                print('invalid input, try again!')
                continue 
            if board[idx] in [10, -10]:
                print('cell taken try again!')
                continue
            # TODO: Assign score['player'] to the selected cell on the board
            board[idx] = score['player']
            break

        except ValueError:
            print("Invalid input. Try again (1-9): ")
    pass 
 
    # HINT: remember the board moves are 1 - 9 but the board indices are
    # 0 - 8

