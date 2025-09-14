text = input("Enter text: ")
shift = int(input("Enter shift value (integer): "))
choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

'''
define function 
use ord function to turn both upper and lower case letters into numbers to shift values properly 
define shift so it will only shift the numbers using if else function: if user chooses 'e', if not use -shift to move letters backwards and decrypt
use ord(char) to convert letter into a numeric value, - start shifts start to 0 to add/subtract the shift input by the user
modulus of 26 for wrap around to keep within 0-25
'''

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