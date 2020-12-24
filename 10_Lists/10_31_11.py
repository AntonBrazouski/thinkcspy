# Sum all the elements in a list up to but not including the first even number.

def sum_up(alist):
    sum = 0
    for item in alist:
        if item % 2 != 0:
            break
        sum += item

    return sum

print(sum_up([1,2,3,4,5]))
print(sum_up([2,2,4,4,5,2,7]))
