# myList = [76, 92.3, "hello", True, 4, 76]
myList = []
myList.append(76)
myList.append(92.3)
myList.append("hello")
myList = myList + [True]
myList = myList + [4]
myList = myList + [76]

print(myList)

# TASK 3
myList.append("apple")
myList.append(76)
myList.insert( 3,"cat")
myList.insert(0, 99)
print(myList)
print(f"myList.index('hello') = {myList.index('hello')}")
print(f"myList.count(76) = {myList.count(76) } ")
myList.remove(76)
myList.pop(myList.index(True))

print(myList)
