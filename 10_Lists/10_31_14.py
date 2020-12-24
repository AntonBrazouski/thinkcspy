# Write a function replace(s, old, new) that replaces
# all occurences of old with new in a string s

def replace(s, old, new):
    pos = 0
    s2 = ""
    s3 = s

    while (s3.index(old) != -1): # value error
        idx = s.index(old)
        s2 = s2 +s[pos:idx]
        pos = idx + len(old)
        s3 = s2[idx +1:]
    return s2

print(replace('chopper', 'p', 'o'))
