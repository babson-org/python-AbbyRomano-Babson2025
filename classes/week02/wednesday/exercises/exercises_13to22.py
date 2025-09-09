
from classes.week00.second_class.utils import clear_screen
'''
#13 - Conditional Logic
Ask the user for a number and print whether it is positive, negative, or zero.
'''
# enter code here

num = float(input('Enter a number: '))
if num > 0:
    print('value is positive')
elif num == 0: 
    print('value is zero')
else:
    print('value is negative')

pause=input('pause')
clear_screen()

'''
#14 - Even/Odd Check
Ask the user for a number and print if it is even or odd.
'''
# enter code here

num = int(input('Enter a number: '))

if num % 2 == 0: 
    print('Number is even')
else:
    print('Number is odd')



pause=input('pause')
clear_screen()

'''
#15 - Boolean Operators
Ask the user for two numbers and check if both are positive, either is positive, or none is positive.
'''
# enter code here

a = float(input('Enter the first number'))
b = float(input('Enter the second number'))

if a > 0 and b > 0:
    print('both numbers are positive')

elif a > 0 or b > 0:
    print('One of the numbers is positive')

else:
    print('None of the numbers are positive')

pause=input('pause')
clear_screen()

'''
#16 - For Loop
Print all numbers from 1 to 20, skipping multiples of 3.
'''
# enter code here

for i in range (1,21):
    if i % 3 == 0:
        continue 
    print(i)

pause=input('pause')
clear_screen()

'''
#17 - While Loop
Ask the user to guess a secret number (hardcoded) until they get it right.
'''
# enter code here

secret = 2

guess = int(input('Guess the number: '))

while guess != secret:
    print('Wrong guess, try again!')
    guess = int(input('guess the number: '))

print('correct, you have guessed the correct number!')

pause=input('pause')
clear_screen()

'''
#18 - Break / Continue
Print numbers 1-10 but stop printing when you reach 7 and skip 3.
'''
# enter code here

for i in range (1,11):
    if i == 3:
        continue
    if i == 7:
        break
    print(i)


pause=input('pause')
clear_screen()

'''
#19 - Function Definition
Write a function square(x) that returns the square of a number and test it.
'''
# enter code here

def square(x):
    return x * x
print(square(2))

pause=input('pause')
clear_screen()

'''
#20 - Function with Mutable Argument
Write a function add_item(lst, item) that appends item to lst and observe the effect on the original list.
'''
# enter code here

list = [2,4,8]

def add_item(lst, item):
    lst.append(item)
    return(list)

print('before:', list)

add_item(list, 10)
print('After:', list )

pause=input('pause')
clear_screen()

'''
#21 - Comments / Documentation
Write a function greet(name) with single-line and multi-line comments explaining each step.
'''
# enter code here

'''
Create greeting
Create name string (to convert txt into a string)
'''

def greet(name):
    name_str = str(name).strip()

#create default incase name is not provided
    if not name_str:
        name_str = 'there'

    message = f'Hello, {name_str}!'
    return message

pause=input('pause')
clear_screen()

'''
#22 - Combining Tools
Ask the user to enter 5 names. Store them in a list, capitalize each name, sort the list, and print it.
'''
# enter code here

names = []

for i in range(5):
    name = input(f'Enter name {i+1}: ')
    names.append(name.capitalize())

names.sort()
print('Sorted Names:', names)



pause=input('pause')
clear_screen()

