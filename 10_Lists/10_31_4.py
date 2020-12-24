def average(alist):
    result = 0
    length = len(alist)
    sum = 0
    for x in alist:
        sum = sum + x
    result = sum / length

    return result

print(average([1,2,3,4]))
