#Ensure user has input a valid number for board size
def get_valid_input(prompt, min_value = 1, max_value = None):
    while True:
        try:
            #When asking for input, ensure its an integer between 0 and a max value if given (e.g. the board indexes)
            value = int(input(prompt))
            if value < min_value: 
                print('Please enter a number greater than 0')
            elif max_value and value > max_value:
                print('please enter a number below 20')
            else:
                return value
        except ValueError: 
            print('Error. Please enter a number. Try again!')
            