# in:   Alice.txt
# out:  alice_words.txt

file = 'Alice.txt'
with open(file, "r", encoding="utf-8") as alice:
    words = {}
    anarray = []

    for line in alice:
        anarray = line.split()
        for aword in anarray:
            if aword not in words:
                words[aword] = 1
            else:
                words[aword] += 1

limit = 10
for k,v in words.items():
    if limit:
        print(k,v)
        limit -= 1
    else:
        break
