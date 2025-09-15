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