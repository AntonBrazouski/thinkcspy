# Count how many words occur in a list up to
# and including the first occurrence of the word “sam”.

def count_words_before_sam(alist):
    word_counter = 0
    for word in alist:
        if word == 'sam':
            word_counter += 1
            break
        word_counter += 1
    return word_counter

print(count_words_before_sam(['joe', 'pitt', 'sam','kate', 'jolie']))
print(count_words_before_sam(['sam', 'pitt', 'sam','kate', 'jolie']))
