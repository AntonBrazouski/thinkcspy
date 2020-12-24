
def remove(theStr, substr):
    index = theStr.find(substr)
    if index < 0: # substr doesn't exist in theStr
        return theStr
    return_str = theStr[:index] + theStr[index + len(substr):]
    return return_str


print(remove('catacombas!', 'c')) # FAILS !!
print(remove('catacombas!', 'ca'))
print(remove('cacacomca!', 'ca'))
