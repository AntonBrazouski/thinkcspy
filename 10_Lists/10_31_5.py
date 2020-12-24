def my_max(alist):
    if alist == None:

        return None

    else:
        tmax = alist[0]
        for item in alist:
            if item > tmax:
                tmax = item

        return tmax

print(my_max([1,2,3,4]))
print(my_max([10,-20,33,14]))
