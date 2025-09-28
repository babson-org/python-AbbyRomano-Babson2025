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
        if s == 30:
             return(f'X wins')
        if s == -30: 
             return(f'O wins')
        return None
    
    for a, b, c in winning_combinations: 
        result = line_sum(a, b, c)
        if result is not None: 
            return result 
        
    return 0  



#TEST 

board1 = [10, 10, 10, 4, 5, 6, 7, 8, 9]
print(calc_score(board1))

board2 = [-10, 2, 3, -10, 5, 6, -10, 8, 9]
print(calc_score(board2))