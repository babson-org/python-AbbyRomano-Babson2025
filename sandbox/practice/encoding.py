#make an encoder from lists of letters and symbols 

def build_encoder():
    letters = ['a','b','c','d','e','f','g','h']
    symbols = ['!','@','#','$','%','^','&','*']

    encoder = {}

    for i in range(len(letters)):
        encoder[letters[i]] = symbols[i]
    return encoder

print(build_encoder())

def encode_message(message, encoder):
    encoded_chars = []
    for char in message:
        if char in encoder:
            encoded_chars.append(encoder[char])
        else:
            encoded_chars.append(char)
    return ''.join(encoded_chars)

encoder = build_encoder()
message = input('Enter a message to encode: ')
encoded_message = encode_message(message, encoder)
print('Encoded message:', encoded_message)

