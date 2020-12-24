def srem_one(s, p):
    res = ''
    idx = 0

    for ch in s:
        #print(f"idx= {idx}, ch = {ch}")
        if (len(p) == 1 and ch == p):
            pass

        elif (idx == len(p)-1) and (len(p) != 1):
            idx = 0

        elif ((ch == p[idx])):
            idx += 1
        else:
            res += ch

    return res

print(srem_one('catacombas!', 'c')) # fails
print(srem_one('catacombas!', 'ca')) # fails
print(srem_one('cacacomca!', 'ca')) # FAILS !! - m!
