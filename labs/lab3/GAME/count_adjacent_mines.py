def count_adjacent_mines(row, col, board):
    global size 
    
    count = 0
    for i in range(row - 1, row + 2): 
        for j in range(col - 1, col + 2):
            if (i, j) == (row, col):
                continue
        if 0 <= i < size and 0 <= j < size:
            if board[i][j] == '💣':
                count += 1
        return count



