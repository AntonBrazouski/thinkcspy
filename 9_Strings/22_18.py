## HINT - use str to array conversion with split, and join


alphabet = "abcdefghijklmnopqrstuvwxyz"
mapping = "cdefghijklmnopqrstuvwxyzab"
message = 'hello'

def substitution_cipher(message, mapping):
    result = []
    for idx in range(len(message)):
        result[idx] = mapping[idx]

def get_letter_code(char):
    return ord(char)

def get_char_index(char):
    return message.index(char)

def switch_letter(message, index):
    result= []
    message[index] = mapping[index]

    return result

def make_code_message(message, mapping):
    result = []
    for i in range(len(message)):
        switch_letter(message,i)

    return message

make_code_message(message, mapping)

print(ord('a'))
