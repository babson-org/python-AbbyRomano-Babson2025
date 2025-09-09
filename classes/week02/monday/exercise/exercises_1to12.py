from classes.week00.second_class.utils import clear_screen
'''
# 1

Write down the steps a program would need to make a cup of tea. Then implement a Python 
function make_tea() that prints each step.
'''
# enter your code here

steps = [
    'fill a kettle with water',
    'place kettle on stove',
    'bring water to a boil', 
    'once water is boiling',
    'pour water into a tea cup',
    'place a tea bag into the hot water',
    'add honey, milk, any desired addition',
    'stir your tea',
    'enjoy!'
]

def make_tea(entries):
    for s in entries:
        print(s)




pause=input('pause')
clear_screen()
'''
#2

Given a list [2, 4, 6, 8, 10], write a program that prints the next three numbers in the list.  
(the ones after 10)
'''
# enter your code here

pattern = [2,4,6,8,10]
for i in range(3):
    next_num = pattern[-1]+ 2
    pattern.append(next_num)
    print(next_num)

pause=input('pause')
clear_screen()
'''
#3

Write a program that asks the user for their first and last name, then prints a greeting:
"Hello, <first name> <last name>!"
'''
# enter your code here

fname = input('please enter your first name')
lname = input('please enter your last name')

print(f'hello, {fname} {lname}!')



pause=input('pause')
clear_screen()
'''
#4

Write a program that prints your Python version and platform using the sys and platform modules.
'''
# enter your code here

import platform
import sys
print('Python Version:', sys.version)
print('Platform:', platform.system(), platform.release())

pause=input('pause')
clear_screen()
'''
#5

Ask the user to input two numbers. Calculate and print their sum, difference, product, 
and division (both / and //).
'''
# enter your code here

x = float(input('Enter first number: '))
y = float(input('Enter second: '))

print('sum:', x + y)
print('difference:', x - y)
print('product:', x * y)
print('division:', x / y)
print('floor division:', x // y)

pause=input('pause')
clear_screen()
'''
#6

Ask the user to input a sentence. Print it in uppercase, lowercase, with the first letter 
capitalized, and split it into words.
'''

# enter your code here

txt = input('Enter a sentence')
print('Uppercase:', txt.upper())
print('Lowercase:', txt.lower())
print('Capitalized:', txt.capitalize())
print('Split into words:', txt.split())


pause=input('pause')
clear_screen()
'''
#7

Calculate the result of the following without parentheses and then with parentheses:
10 + 2 * 5 / 2 - 3 ** 2
'''
# enter your code here

result1 = 10 + 2 * 5 / 2 - 3 ** 2
result2 = (10 + (2*5))/((2-3)**2)

print('Without parentheses:', result1)
print('With parentheses:', result2)

pause=input('pause')
clear_screen()
'''
#8

Create a list of your three favorite foods. Replace the second item with a new one, 
then print the list.
'''
# enter your code here

list = ['Raspberries', 'Strawberries', 'Chocolate']
list[2] = 'Dark Chocolate'
print('Updated favorites list:', list)

pause=input('pause')
clear_screen()
'''
#9

Create a tuple with four numbers. Try to change the first number (observe the error) 
and then print the tuple.
'''
# enter your code here

tup = (2,5,6,7)
try:
    tup[1] = 3
except TypeError:
    print('Tuples are immutable and cannot be modified')
print('tuple remains:', tup)


pause=input('pause')
clear_screen()
'''
#10

Create a dictionary representing a student (name, age). Update the age. Create a list of 
favorite numbers and add a new number.
'''
# enter your code here

from pprint import pprint
student = {'name' : 'Alice', 'age' : '22'}
student['age'] = 24
fav_nums = [2, 7, 21]
student['favorites'] = fav_nums
print('student dictionary')
pprint(student)




pause=input('pause')
clear_screen()
'''
#11

Ask the user to input their favorite quote. Save it to a file quotes.txt 
and read it back to print it.
'''
# enter your code here
quote = input('Enter your favorite quote: ')

with open('quote.txt', 'w') as f:
    f.write(quote)

with open ('quote.txt', 'r') as f:
    saved_quote = f.read()
print('Your quote:', saved_quote)



pause=input('pause')
clear_screen()
'''
#12
Ask the user to input 5 numbers (one at a time), store them in a list, and print the sum and average.
'''
# enter your code here

numbers = []
for i in range(5):
    num = int(input(f'enter number {i+1}: '))
    numbers.append(num)
total = sum(numbers)
average = total / len(numbers)
print('numbers', numbers)
print('total', total)
print('average', average)

pause=input('pause')
clear_screen()