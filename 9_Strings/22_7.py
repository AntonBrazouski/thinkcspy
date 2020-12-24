def mirror(s):
    res = ''
    for ch in s:
        res = ch + res
    res = s + res
    return res

print(mirror("Kangaru!"))
