message = 'ABC'
letters = 'A->B, B->A, C->G'


def sc(message, letters):
    result = ''
    idx = 0
    for ch in message:
        if letters[letters.index(ch) + 1] == '-':
            idx = letters.index(ch) + 3
            print(idx)
        else:
            pass
        result += letters[idx]

    return result


print(sc(message, letters))
