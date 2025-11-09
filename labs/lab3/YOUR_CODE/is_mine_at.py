from globals import MINE_SYMBOL, DEFAULT_SYMBOL
from print_board import print_board

def is_mine_at(hidden_board, mine_board, mines):

    found_mines = 0 
    total_mines = len(mines)
    size = len(mine_board)

    print('Begin guessing! Try to find all the mines!')
    
    print_board(hidden_board, 0)
    while found_mines < total_mines:
        try:
            row = int(input(f'Enter a row(0-{size-1}): '))
            col = int(input(f'Enter a column(0-{size-1}): '))
        except ValueError:
            print('Please enter numbers only!')
            continue 
        
        if not (0 <= row < size and 0 <= col < size):
            print('Value not on board, try again!')
            continue 

        if (row, col) in mines: 
            print('You found a mine!')
            hidden_board[row][col] = (MINE_SYMBOL, MINE_SYMBOL)
            found_mines += 1
        else: 
            print('No mine there. Guess again!')
            hidden_board[row][col] = (DEFAULT_SYMBOL, DEFAULT_SYMBOL)
        
        print_board(hidden_board, 0)
        print(f'Mines Found: {found_mines}/{total_mines}')

    print('Congratulations! You found all the mines, game over!')
    print('Here was the mine board: ')
    print_board(mine_board, 0)

    