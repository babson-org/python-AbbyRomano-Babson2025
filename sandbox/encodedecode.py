#encode and decode in one

encode_map = { 
    'a': '!', 'b': '@', 'c': '#', 'd':'$', 'e':'%',
    'f': '^', 'g': '&', 'h': '*', 'i': '(', 'j': ')',
    'k': '-', 'l': '=', 'm': '+', 'n': '{', 'o': '}', 
    'p': '::', 'q': ';;', 'r': '"', 's': "'", 't': '<',
    'u': '>', 'v': '?', 'w': '/', 'x': '[', 'y': ']', 
    'z': '|', ' ': '~'
}

def build_decode_map(mapping):
    decode_map = {}
    for key in mapping:
        value = mapping[key]
        decode_map[value] = key
    return decode_map

def encode(text):
    result = ''
    for ch in text.lower():
        if ch in encode_map:
            result += encode_map[ch]
        else:
            result += ch
    return result

def decode(text):
    decode_map = build_decode_map(encode_map)
    result = ''
    for ch in text:
        if ch in decode_map:
            result += decode_map[ch]
        else:
            result += ch
    return result

message = input('Enter a message: ')
encoded_message = encode(message)
print('Encoded message:', encoded_message)
decoded_message = decode(encoded_message)   
print('Decoded message:', decoded_message)


        


