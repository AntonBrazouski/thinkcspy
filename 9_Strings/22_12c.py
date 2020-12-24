def remove(s, p):
    idx = 0
    res =''
    buf = ''
    if len(p) == 1: # one char substr
        for ch in s:
            if ch != p:
                res = res + ch

    for ch in s: # more than one char substr
        #print(f"index - {idx}")
        if len(p)-1 == idx:
             idx = 0 # index reset
             buf = '' # buffer rest
        elif ch == p[idx]: #  match!
            idx += 1 # raise index value
            buf = buf + ch # store char to buffer
        else:
            if idx > 0: # no further match
                res = res + buf + ch # fulush buffer + str
                idx = 0 # reset index
            else:
                res = res + ch # raise string output
            #print(res)
        if ch == s[-1] and idx >0: # last char and has buffer
            res = res + ch # flush buffer

    return res

print(remove('strings', 'st'))
print(remove('asagasasa!','asa')) 
print(remove('asagasasa!','a'))
print(remove('strings', 's'))
