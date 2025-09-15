# ==============================
# Main Program
# ==============================
def main():
    while True:
        print("Lab 1 - Python Basics")
        print("1. Draw Diamond")
        print("2. Text Analysis")
        print("3. Caesar Cipher")
        choice = input("Select part to run (1-3): ")
        
        if choice == "1":
            draw_diamond()
        elif choice == "2":
            text_analysis()
        elif choice == "3":
            caesar_cipher()
        else:
            exit()



"""
Lab 1 - Python Basics
Author: <Your Name>
Instructions: Complete each part below. Save your work and commit + sync in Codespaces.
"""

# ==============================
# Part 1: Draw a Diamond
# ==============================
def draw_diamond():
    """
    Ask the user for an odd number for the diamond height
    and print a symmetric diamond of that height.
    """
    
print("you have some work todo!, draw_diamond")

'''
ask user for odd number: ask for input and turn odd number into an integer
divide height by 2 to find half way point so it knows how many rows to print on top and then on bottom 
print top half of diamond using range (half+ 1) so it will print rows 0,1,2, and then +1 will print row 3 - define how many spaces to print before and after first and second *, if = 0, first row so will use loop to only print 1 star
print bottom half of diamond using range half -1,-1,-1 so loop will count backwards from 2,1,0 and use same method for printing very bottom singular * and then spaces before and after * 
'''
height = int(input("Enter an odd number for the diamond height: "))

half = height // 2

for i in range(half + 1):
    spaces_before = " " * (half - i)
    if i == 0:
        print(spaces_before + "*")
    else:
        middle_spaces = " " * (2 * i - 1)
        print(spaces_before + "*" + middle_spaces + "*")

for i in range(half - 1, -1, -1):
    spaces_before = " " * (half - i)
    if i == 0:
        print(spaces_before + "*")
    else:
        middle_spaces = " " * (2 * i - 1)
        print(spaces_before + "*" + middle_spaces + "*")

#Uncomment to test Part 1
# draw_diamond()


# ==============================
# Part 2: Count Letters, Words, and Sentences
# ==============================
    """
    Ask the user for a block of text.
    Count and display:
        - Number of letters (only count a-zA-Z)
        - Number of words   (use split())
        - Number of sentences (., ?, !) 
    """

    print("you have some work todo!, text_analysis")

'''
ask user for text using input function 
set letter count at 0, use for loop to look if charachter is a-z using is.alpha, if so +1 letter count 
split text block into list using .split function, use len to count # of words on the list 
set sentence_count to 0, look for characters .!?, if present, +1 to sentence count 
add check_words at the end to ensure all text input is a-z, if not error will present and user will reinput text 
'''

def text_analysis():

text = input("Enter some text: ")

letters = 0
for char in text: 
    if char.isalpha():
        letters += 1

words = text.split()
num_words = len(words)

sentence_count = 0
for char in text:
    if char in ".?!":
        sentence_count += 1

check_words = len(text.split())
if check_words != words:
    print('fatal error: something went wrong')
    exit()
    
print(f"Letters: {letters}")
print(f"Words: {num_words}")        
print(f"Sentences: {sentence_count}")   

 



# Uncomment to test Part 2
# text_analysis()


# ==============================
# Part 3: Caesar Cipher – Encrypt and Decrypt
# ==============================
'''
define function 
use ord function to turn both upper and lower case letters into numbers to shift values properly 
define shift so it will only shift the numbers using if else function: if user chooses 'e', if not use -shift to move letters backwards and decrypt
use ord(char) to convert letter into a numeric value, - start shifts start to 0 to add/subtract the shift input by the user
modulus of 26 for wrap around to keep within 0-25
'''

text = input("Enter text: ")
shift = int(input("Enter shift value (integer): "))
choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

def caesar_cipher(text, shift, choice): 
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            actual_shift = shift if choice == 'e' else -shift
            result += chr((ord(char) - start + actual_shift) % 26 + start)
        else:
            result += char
    return result 

if choice not in ['e', 'd']:
    print('Invalid choice! Choose Again.')
else:
    result = caesar_cipher(text,shift,choice)
    print("Result:", result)

# Uncomment to test Part 3
# caesar_cipher()




if __name__ == "__main__":
    main()