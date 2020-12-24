def is_even(num):
    return num % 2 == 0

def sum_even(alist):
    sum_even = 0
    for item in alist:
        if is_even(item):
            sum_even = sum_even + item

    return sum_even

print(sum_even([1,2,3,4,5]))
print(sum_even([1,0,3,-4,50]))
