def get_valid_input(prompt, min_value = 1, max_value=None):
    while True:
        try:
            value = (int(input(prompt)))
            if value < min_value: 
                print('Please enter a number greater than 0')
            elif max_value and value > max_value:
                print('please enter a number below 20')
            else:
                return value
        except ValueError: 
            print('Error. Please enter a number. Try again!')
            