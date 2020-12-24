def sum_of_squares(xs):
    sum = 0
    for item in xs:
        sum = sum + item ** 2

    return sum

print(sum_of_squares([2,3,4]))
print(sum_of_squares([2,2,-2]))
print(sum_of_squares([3,4]))
