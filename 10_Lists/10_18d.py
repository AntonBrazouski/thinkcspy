words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]

past_tense = []
for idx in range(len(words)):
    word = words[idx]
    if word[-1] == 'e':
        word = word + 'd'
    else:
        word = word + 'ed'
    past_tense. append(word)
