#Determines if winner is on the board 
def calc_score(board: list[int]):
    #define winning combos by listing all possible winning INDEX combinations e.g. 0, 3, 6 is a diagonal win 
    winning_combinations = [
        (0, 1, 2), 
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6), 
        (1, 4, 7), 
        (2, 5, 8), 
        (0, 4, 8),
        (2, 4, 6),
    ]
     
    def line_sum(a, b, c):
        s = board[a] + board[b] + board[c]
        # If x (=10) is in all three cells, sum is 30 and X wins 
        if s == 30:
             return(f'X wins')
        #if 0 (=-10) is in all three cells, sum is -30 and O wins 
        if s == -30: 
             return(f'O wins')
        #if no winner (no sums to 30/-30), return nothing
        return None
    
    #create a loop to check for winning combos
    for a, b, c in winning_combinations: 
        result = line_sum(a, b, c)
        #if the sum of lines a, b, c is 30 or -30, return the result 
        if result is not None: 
            return result 
        
    #if no winner, return 0   
    return 0  

  

"""
Determines if there's a winner on the board.
Returns 30 if X wins, -30 if O wins, 0 otherwise.
         
there are 8 ways to win: 3 rows, 3 columns, 2 diagnols
if the cells in a row, column or diagnol add up to 30 return 30
if they add upto -30 return -30
else return 0
"""

'''
line_sum takes 3 numbers and if the sum is either 30
or -30 returns that sum otherwise do not return
'''         
         
        # TODO: Sum the values at board[a], board[b], board[c] 
        # TODO: Return 30 if X wins, -30 if O wins otherwise do not return

     
    # TODO: For each of the 8 ways to win
    # TODO: Check the cells in each row, column, or diagonal using line_sum
    # TODO: Return 0 if line_sum() didn't return 30 or -30


