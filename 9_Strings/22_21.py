
def rot13(msg):
    alb = "abcdefghijklmnopqrstuvwxyz"
    enc = ''
    for ch in msg:
        idx = (alb.find(ch) + 13 )% 26
        enc = enc + alb[idx]

    return enc

print(rot13('cat'))
print(rot13('jjz'))
print(rot13(rot13('jjz')))
