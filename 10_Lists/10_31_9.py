def sum_negatives(alist):
    sum = 0
    for item in alist:
        if item < 0:
            sum = sum + item

    return sum

print(sum_negatives([1,2,-3,4,-1]))
print(sum_negatives([1,-2,-3,4,-1]))
