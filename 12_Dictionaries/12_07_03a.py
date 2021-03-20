# in:   Alice.txt
# out:  alice_words.txt

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
file = 'Alice.txt'
bigarray = []
file_2 = 'alice_words.txt'

with open(file, "r", encoding="utf-8") as alice:
    words = {}
    anarray = []

    for line in alice:
        anarray = line.split()
        for item in anarray:
            if item[0] in ALPHABET:
                if item not in bigarray:
                    bigarray.append(item)

bigarray.sort()
print(bigarray)
