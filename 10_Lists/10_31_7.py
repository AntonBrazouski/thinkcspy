def is_odd(num):
    return num % 2 != 0

def count_odds(alist):
    count = 0
    for item in alist:
        if is_odd(item):
            count += 1

    return count

print(count_odds([1,2,3,4]))
print(count_odds([5,7,9,11,-2]))
