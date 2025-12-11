#symbol cipher decoding
def decode_message(txt):
    cipher = {
        '!':'a', '@':'b', '#':'c', '$':'d',
        '%':'e', '^':'f', '&':'g', '*':'h'
    }

    decoded = ' '
    for ch in txt:
        if ch in cipher:
            decoded += cipher[ch]
        else:
            decoded += ch
    return decoded

message = input('Enter the encoded message: ')
print('Decoded message:', decode_message(message))


