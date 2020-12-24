# implement the following list methods: count, in, reverse, index, insert

# wrong, it's not len, count takes 2 par - list and obj
def count(alist):
    counter = 0
    for intem in alist:
        counter += 1
    return counter

def in_list(element, alist):
    for item in alist:
        if item == element:
            return True
    return False

def reverse(alist):
    newlist = []
    for x in range((len(alist) -1), -1, -1):
        newlist.append(alist[x])
    return newlist

# wrong, index function should return list index
def index(num, alist):
    return alist[num]

def insert(element, alist, pos=0):
    newlist = []
    for x in range(len(alist)):
        if x == pos:
            newlist = alist[:pos]
            newlist.append(element)
            newlist = newlist + alist[pos:]
    return newlist

test_list = [2,-4, 16,-25]
print(count(test_list))
print(in_list(2, test_list))
print(reverse(test_list))
print(index(2, test_list))
print(insert(200, test_list,3 ))
