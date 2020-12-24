def srem_one(s, p):
    res = ''
    c = 0
    idx = 0
    for ch in s:
        if (len(p) == 1 and ch == p):
            c += 1

        elif (idx == len(p)-1) and (len(p) != 1):
            idx = 0
            c += 1
        elif ((ch == p[idx]) and (c < 1)):
            idx += 1
        else:
            res += ch

    return res

print(srem_one('catacombas!', 'c')) 
print(srem_one('catacombas!', 'ca'))
print(srem_one('cacacomca!', 'ca'))
