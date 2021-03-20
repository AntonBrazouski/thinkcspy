TRANSLATIONS = {
    'sir': 'matey',
     'hotel': 'fleabag inn',
     'student': 'swabbie',
     'boy': 'matey',
     'madam': 'proud beauty',
     'professor': 'foul blaggart',
     'restaurant': 'galley',
     'your': 'yer',
     'excuse': 'arr',
     'students': 'swabbies',
     'are': 'be',
     'lawyer': 'foul blaggart',
     'the': "th'",
     'restroom': 'head',
     'my': 'me',
     'hello': 'avast',
     'is': 'be',
     'man': 'matey'
      }

# print(TRANSLATIONS)

def translator(astring):
    translated = []
    result = ' '
    for word in astring.split(' '):
        if word in TRANSLATIONS:
            word = TRANSLATIONS[word]
        translated.append(word)

    return result.join(translated)

print(translator('hello there students'))
