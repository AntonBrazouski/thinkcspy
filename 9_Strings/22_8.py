def srem(s,r):
    res = ''

    for ch in s:
        if ch != r[0]:
            res = res + ch

    return res

print(srem('catacombas!', 'c'))        
