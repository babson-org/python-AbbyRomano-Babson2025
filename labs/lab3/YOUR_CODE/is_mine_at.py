from globals import MINE_SYMBOL, DEFAULT_SYMBOL
from print_board import print_board

def is_mine_at(hidden_board, mine_board, mines):
    #track number of found mines versus total mines placed
    found_mines = 0 
    total_mines = len(mines)
    size = len(mine_board)

    print('Begin guessing! Try to find all the mines!')
    #show the current board, at level 0 to reveal the players current board with diamonds & hidden mines
    print_board(hidden_board, 0)

    #loop for guessing, will not end until total_mines = found_mines
    while found_mines < total_mines:
        #player chooses a cell, make sure it is {size-1} to ensure value is within row/col index
        try:
            row = int(input(f'Enter a row(0-{size-1}): '))
            col = int(input(f'Enter a column(0-{size-1}): '))
        except ValueError:
            print('Please enter numbers only!')
            continue 
        #if the cell is not within the board boundaries, ask for a new value within
        if not (0 <= row < size and 0 <= col < size):
            print('Value not on board, try again!')
            continue 
        #check if the guessed cell is in the mines list, 
        if (row, col) in mines: 
            #if so print you found a mine 
            print('You found a mine!')
            #append hidden board to show a mine symbol 
            hidden_board[row][col] = (MINE_SYMBOL, MINE_SYMBOL)
            #add to count of found_mines so loop knows when to end
            found_mines += 1
        #if not a mine in list, let user know, do not change any value and tell user guess again
        else: 
            print('No mine there. Guess again!')
            hidden_board[row][col] = (DEFAULT_SYMBOL, DEFAULT_SYMBOL)
        #at end of guess, show updated board (will show mines if have been found, otherwise no change)
        print_board(hidden_board, 0)
        #display number of mines found out of number of total mines so user knows how many more to find 
        print(f'Mines Found: {found_mines}/{total_mines}')
        
    #if all mines have been found and total mines = found_mines (so while loop ends), reveal mine board and congratulate winner
    print('Congratulations! You found all the mines, game over!')
    print('Here was the mine board: ')
    print_board(mine_board, 0)

    