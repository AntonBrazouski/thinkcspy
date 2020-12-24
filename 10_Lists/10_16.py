origlist = [45, 32, 88]
origlist.append("cat")
print(origlist)

origlist = [45, 32, 88]
origlist = origlist + ["cat"]
print(origlist)

origlist = [45, 32, 88]
newlist = origlist + ["cat"]
print(newlist)

try:
    newlist + 1
except TypeError:
    print('TE')
