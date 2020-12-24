def s_reverse(arg):
    #return arg[::-1]
    res = ''
    for ch in arg:
        res = ch + res
    return res

print(s_reverse('Kangaru!'))
