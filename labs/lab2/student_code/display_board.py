from utils import clear_screen

def print_board(board: list[int]) -> None:
    """
    Display the Tic-Tac-Toe board.
    Args:
        board: List of 9 integers (10 for X, -10 for O, 1–9 for open).
    """
    #define cell to use when printing the row and properly converting -10 to an O and 10 to and X, otherwise just return its cell value 
    def cell(value: int) -> str:
        if value == 10: return 'X'
        elif value == -10: return 'O'
        else: return str(value)

    clear_screen()
    print()
#run a for loop 3 times to bprint 3 rows , * row by 3 and + column to create values/indecies for each of the rows, and then use cell to convert it to an X or an O if -10 or 10
    for row in range(3):
        row_values = [cell(board[row * 3 + col]) for col in range(3)]
        #print spaces and lines for the board and then print row values for rows 1 2 and 3 followed by more spaces and lines to complete the filled/playable board
        print('   |   |   ')
        print(f' {row_values[0]} | {row_values[1]} | {row_values[2]} ')
        print('   |   |   ')
        #if row is above row 2, print a horizontal line otherwise if row is 3 or up print nothing
        if row < 2:
            print('-----------')
    print()

'''
from utils import clear_screen
def print_board(board: list[int]):
    """
        Display the Tic-Tac-Toe board with human-friendly layout.
        Remember the board may look like:
        [10, 2, 3, 4, -10, 6, 7, 8, 10] after 3 moves and print_board
        
        X | 2 | 3
        ---------
        4 | O | 6
        ---------
        7 | 8 | X
    """
        
    clear_screen()
'''
    # TODO: For each row, print formatted board row using cell()
    # HINT: For each row create a list of what should be printed
    #       row_values = [ 'X', '2', '3' ] call cell() each time to get each value
    #       add the board layout:
    
    #                  |   |          
    #                X | 2 | 3 
    #                  |   |   
    #               -----------
    #                  |   |   
    #                4 | O | 6 
    #                  |   |   
    #               -----------
    #                  |   |   
    #                7 | 8 | X 
    #                  |   |   
    
