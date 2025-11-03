import globals

def print_board(board, level):
    #set level to 0 to refer to hidden board 
    level = 0 

    line_hash = '|-----' * globals.COLS + '|'

    print('      ', end='')
    for col in range(globals.COLS):
        print(f'   {col}  ', end='')
    print()

    print('      ', line_hash)

    for row in range(globals.ROWS):
        print(f' {row} ', end='')

        for col in range(globals.COLS):
            cell = board[row][col]

            if isinstance(cell, tuple):
                symbol = cell[level]
            else:
                symbol = cell if cell is not None else ' '
            print(f'|{symbol}', end=' ')
        print('|')
        print('     ' + line_hash)
    
