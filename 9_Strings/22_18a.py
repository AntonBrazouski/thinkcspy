message = 'ABC'
letters = 'A->B, B->A, C->G'


def sc(message, letters):
    result = ''
    idx = 0
    for ch in message:
        idx = letters.index(ch) + 3
        print(idx)
        result += letters[idx]

    return result


print(sc(message, letters))
