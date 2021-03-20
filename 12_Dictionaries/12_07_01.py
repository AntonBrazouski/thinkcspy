astring = input('Please enter a sentence: ThiS is String with Upper and lower case Letters.')

astring = astring.lower()
print(astring)

adict = {}

alist = list(astring)
alist.sort()

for ch in alist:
    if ch not in adict:
        adict[ch] = 1
    else:
        adict[ch] += 1


for k,v in adict.items():
    print(k + '\t' + str(v))
