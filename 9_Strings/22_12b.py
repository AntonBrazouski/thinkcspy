
def remove(theStr, substr):
    return_str = theStr
    index = theStr.find(substr)

    if index < 0:
        return_str = theStr
    else:
        while return_str.find(substr) >= 0: ## ????
            index = return_str.find(substr)
            return_str = return_str[:index] + return_str[index + len(substr):]

    return return_str


print(remove('catacombas!', 'c'))
print(remove('catacambas!', 'ca'))
print(remove('cacacomca!', 'ca'))
print(remove('cacaccomcac!', 'cac'))
print(remove('cacaccomcac!', 'cact'))
