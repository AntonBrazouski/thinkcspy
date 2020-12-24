def srem_one(s, p):
    res = ''
    c = 0
    idx = 0

    for ch in s:
        if ((idx == (len(p)- 1)) and c < 1):
            c += 1
            idx = 0
        elif ch == p[idx]:
            idx += 1
        else:
            res += ch

    return res

print(srem_one('catacombas!', 'ca'))
