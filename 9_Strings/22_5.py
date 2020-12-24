def number_of_digits(anint):

    result = 0

    if type(anint) == type(3):
        has_digits = True
    else:
        has_digits = False


    n = 0
    count = 0

    while has_digits:
        if anint == 0:
            return 1
        if (anint / 10**n >= 1) or (anint / 10**n <= -1):
            count += 1
            n += 1
        else:
            has_digits = False

    return count

print(number_of_digits(0))
