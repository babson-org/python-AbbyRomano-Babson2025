import globals

def print_board(board: list, level: int):

    board = [
        [(' ♦', '💣'), (' ♦', '💣'), (' ♦', 1),
         (' ♦', '   '), (' ♦', '   '), (' ♦', '   ')],
        [(' ♦', 2), (' ♦', 2), (' ♦', 1),
         (' ♦', '   '), (' ♦', '   '), (' ♦', '   ')],
        [(' ♦', '   '), (' ♦', '   '), (' ♦', '   '),
         (' ♦', '   '), (' ♦', '   '), (' ♦', '   ')],
    ]

    level = 0

    line_hash = '|-----'

    print('      ', end='')
    for idx in range(globals.COLS):
        print(f'   {idx}  ', end='')                
    print(f'\n      {line_hash * globals.COLS}|')

    for row in range(globals.ROWS):
        print(f'  {row:<3}|', end='')
        for col in range(globals.COLS):
            print(f'| {board[row][col][level]} ', end='')
        print('|')
        print(f'      {line_hash * globals.COLS}|')
    print()
    return board, level


    
