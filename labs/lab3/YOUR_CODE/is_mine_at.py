from globals import MINE_SYMBOL, DEFAULT_SYMBOL
from print_board import print_board


def is_mine_at(hidden_board, mine_board, mines):
    found_mines = 0 
    total_mines = len(mines)
    size = len(mine_board)

    print('Begin guessing! Try to find all mines!')
    #print hidden board by calling the function and adding 0 as the second argument as we only want to see the 1st layer of the board aka diamonds 
    print_board(hidden_board, 0)

    #While loop that will continue until found mines = total mines 
    while found_mines < total_mines: 
        try: 
            #Ask user for a row and a column, to present user choice as correct board/python index, -1 from size
            row = int(input(f'enter a row (0-{size-1}): '))
            col = int(input(f'enter a column (0-{size-1}): '))
        #Make sure the user input is valid and within range, if not present an error message 
        except ValueError:
            print("Please enter numbers only!")
        
        #if row/column chosen is not above 0 or within -1 (index) of size chosen by user, present error because invalid input
        if not (0 <= row < size and 0 <= col < size):
            print("Value not on board, try again!")
            continue
        
        #If the row and column chosen are in list of mines, 
        if (row, col) in mines: 
            print('You found a mine!')
            #update the board at that index to show the mine symbol from globals 
            hidden_board[row][col] = (MINE_SYMBOL, MINE_SYMBOL) 
            #add 1 to found mines, so loop from place_random_mines continues until found mines == total mines 
            found_mines += 1
        #if the index chosen is not in mines list, print try again
        else: 
            print('No mine there. Try again!')
            #keep the row and column chosen as the default symbol and continue loop to next index/guess
            hidden_board[row][col] = (DEFAULT_SYMBOL, DEFAULT_SYMBOL)

        #print updated board after each turn
        print("DEBUG hidden_board sample:", hidden_board[0][0])
        print_board(hidden_board, 0)

#once mines found == total mines, prints message and the mine board 
    print('You found all of the mines game over!')
    print('Here was the mine board')
    print_board(mine_board, 0)
    