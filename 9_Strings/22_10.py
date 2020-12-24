def occu(s, p):
    c = 0
    idx = 0

    for ch in s:
        # print(f"index = {idx}")
        # print(f"ch = {ch}")
        # print(f"c = {c}")
        if idx == len(p)-1:
            c += 1
            idx = 0

        elif ch == p[idx]:
            idx += 1

    return c
#
print(occu('ca', 'cat'))
print(occu('cat', 'cat'))
print(occu('catacat', 'cat'))
print(occu('catacatandcat', 'cat'))
print(occu('catacatandcat', 'cat'))

# print(occu('ca', 'cac'))
# print(occu('cac', 'cac'))
print("")
print(occu('cacac', 'cac')) # fixed with elif (not if)
print(occu('caccac', 'cac'))
print(occu('cacandcac', 'cac'))
