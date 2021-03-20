f = open('alice.txt', 'r', encoding='utf-8')

count = {}

for line in f:
    for word in line.split():

        # remove punctuation
        word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
        word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
        word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
        word = word.replace(']', '').replace(';', '')

        # ignore cause
        word = word.lower()

        # ignore numbers
        if word.isalpha():
            if word in count:
                count[word] = count[word] + 1
            else:
                count[word] = 1

# modified to sort a key list
keys = count.keys()
ar_keys = []

for item in keys:
    ar_keys.append(item)

ar_keys.sort()
keys = ar_keys


# save the word count analysis to a file
out = open('alice_words.txt', 'w', encoding="utf-8")


max = 0
max_word = ''
max_count = 0

for word in keys:
    if len(word) > max:
        max = len(word)
        max_word = word
        max_count = count

print(max_word + " " + str(max))
print('\n')

# print("The word 'alice' appears " + str(count['alice']) + " times in the book.")
