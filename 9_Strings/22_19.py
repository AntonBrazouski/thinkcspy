message = 'ABC'
letters = 'A->B, B->A, C->G'
enc_message = 'BAG'

def dc(enc_message, letters):
    search_str = ''
    result = ''
    idx = 0
    for ch in enc_message:
        search_str = '->' + ch
        idx = letters.index(search_str) - 1
        result += letters[idx]

    return result


print(dc(enc_message, letters))
