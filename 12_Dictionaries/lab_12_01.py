def countA(text):
    count = 0
    for c in text:
        if c == 'a':
            count = count + 1
    return count

print(countA("banana"))
