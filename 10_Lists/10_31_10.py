## # count how many words in a list have length 5

def count_five(alist):
    counter = 0
    for word in alist:
        if len(word) == 5:
            counter += 1

    return counter

print(count_five(['x','abcde','fgklmnopr','']))
