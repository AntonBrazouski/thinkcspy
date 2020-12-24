# list methods
mylist = []

mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(1, 12)
print(mylist)
print(mylist.count(12))

print(mylist.index(3))
print(mylist.count(5))

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist.remove(5)
print(mylist)
mylist.remove(12)
print(mylist)

lastitem = mylist.pop()
print(lastitem)
print(mylist)

lastitem = mylist.pop(0)
print(lastitem)
print(mylist)

### methods return
print("\n" + "Example 2")
mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist = mylist.sort() # probably an error
print(mylist)
