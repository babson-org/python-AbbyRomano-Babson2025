#create cipher that uses dictionary
def decode_message(message, cipher_map):
    decoded_char = []
    for char in message:
        if char in cipher_map:
            decoded_char.append(cipher_map[char])
        else:
            decoded_char.append(char)
    return ''.join(decoded_char)
        

cipher_map = {
    '!': 'a',
    '@': 'b',
    '#': 'c',
    '$': 'd',
    '%': 'e',
    '^': 'f',
    '&': 'g',
    '*': 'h',
    '(': 'i',
    ')': 'j',
    '-': 'k',
    '+': 'l',
    '=': 'm',
    '{': 'n',
    '}': 'o',
    '[': 'p',
    ']': 'q',
    ':': 'r',
    ';': 's',
    '"': 't',
    "'": 'u',
    '<': 'v',
    '>': 'w',
    ',': 'x',
    '.': 'y',
    '?': 'z', 
    } 

message = input('enter the coded message: ')
decoded_message = decode_message(message, cipher_map)
print('the decoded message is:', decoded_message)


