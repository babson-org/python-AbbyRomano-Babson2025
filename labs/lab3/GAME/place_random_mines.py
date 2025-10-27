import random 
size = int(input('Enter board size: '))

board = [['⬧' for _ in range(size)] for _ in range(size)]
for i in range(size):
    print('⬧ ' * size)

num_mines = int(input('Enter a number: '))
for _ in range(num_mines):
    row = random.randint(0, size - 1)
    col = random.randint(0, size - 1)
    board[row][col] = '💣'

# Print the board again with mines
print('\nBoard with mines:')
for row in board:
    print(*row)