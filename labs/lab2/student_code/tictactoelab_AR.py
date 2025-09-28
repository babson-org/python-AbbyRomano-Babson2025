#AI to select first available cell 
#returns python index 0-8 -> prints 1 for board number 2 
def ai_move(board: list[int]):
    for i in range(len(board)):
        if abs(board[i]) != 10:
            return i 
    pass 
board = [10, 2, 3, 4, -10, 6, 7, 8, 9] 
print(ai_move(board))

#returns the board number 1-9 -> prints 2 for board number 2  
def ai_move_b(board: list[int]):
    for i in range(len(board)):
        if abs(board[i]) != 10: 
            return i + 1
    pass
board = [10, 2,3, 4, -10, 6, 7, 8, 9]
print(ai_move_b(board)) 



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



#TEST 

#Three 10's in row indicies 0,1,2 -> X wins
board1 = [10, 10, 10, 4, 5, 6, 7, 8, 9]
print(calc_score(board1))

#Three -10's in row indicies 0, 3, 6 -> 0 wins 
board2 = [-10, 2, 3, -10, 5, 6, -10, 8, 9]
print(calc_score(board2))