message = 'ABC'
letters = 'A->B, B->A, C->G'


def sc(message, letters):
    search_str = ''
    result = ''
    idx = 0
    for ch in message:
        search_str = ch + '->'
        idx = letters.index(search_str) + 3
        print(idx)
        result += letters[idx]

    return result


print(sc(message, letters))
