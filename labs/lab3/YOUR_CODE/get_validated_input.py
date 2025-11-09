#Ensure user has input a valid number for board size
def get_valid_input(prompt, min_value = 1, max_value = 20):
    while True:
        try:
            #When asking for input, ensure its an integer between 0 and a max value if given (e.g. the board indexes)
            value = int(input(prompt))
            #if number is too small (below 1 or defined min value)
            if value < min_value: 
                print('Please enter a number greater than 0')
            #if number is too big (above 20, or set max value)
            elif max_value and value > max_value: 
                print('Please enter a number below 20')
            #if its valid, return it
            else:
                return value
        #if its a letter or non-number for some reason, make sure user inputs number next time
        except ValueError: 
            print('Error. Please enter a number. Try again!')
            