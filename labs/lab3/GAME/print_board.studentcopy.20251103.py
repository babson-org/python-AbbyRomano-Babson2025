def print_board(board):
    """Print the board row by row in a simple grid format."""
    print("\nCurrent Board:")
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()