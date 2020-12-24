def pldr(s,p):
    return s == s_reverse(p)


def s_reverse(arg):
    #return arg[::-1]
    res = ''
    for ch in arg:
        res = ch + res
    return res

print(pldr('cat', 'tac'))
print(pldr('ca', 'ta'))
