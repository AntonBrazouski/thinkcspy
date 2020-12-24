def find2(astring, achar, start):
    """
    Find and return the index of achar in astring
    Return -1 if achar does not occur in astring
    """
    ix = start
    found = False
    while ix < len(astring) and not found:
        if astring[ix] == achar:
            found = True
        else:
            ix = ix + 1
    if found:
        return ix
    else:
        return -1


def find3(asting, achar, start=0):
    """
    find and return the index of achar in astring
    return -1 if achar does not occur in astring
    """
    ix = start
    found = False
    while ix < len(asting) and not found:
        if asting[ix] == achar:
            found = True
        else:
            ix = ix + 1
    if found:
        return ix
    else:
        return -1


def find4(astring, achar, start=0, end=None):
    """
    Find and return the index of achar in astring
    Return -1 if achar does not occur in astring
    """
    ix = start
    if end == None:
        end = len(astring)

    found = False
    while ix < end and not found:
        if astring[ix] == achar:
            found = True
        else:
            ix = ix + 1
    if found:
        return ix
    else:
        return -1


print(find2('banana', 'a', 2))
print(find2('banana', 'n', 3))

print('FIND3')
print(find3('banana', 'a', 2))
print(find3('banana', 'a')) # 1
print(find3('bnna', 'a')) # 3
print(find3('bnna', 'a', 2)) #

print('\n'+'FIND4')
ss = "Python strings have some inetesting methods"
print(find4(ss,'s'))
print(find4(ss,'s',8,12))
print(find4(ss,'s',8,25))
