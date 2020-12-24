# List comprehensions

def is_prime(num):
    if num > 1:
       # check for factors
       for i in range(2,num):
           if (num % i) == 0:
               return False
       else:
           return True

    else:
       return False


def primes_upto(n):
    """ Return a list of all prime numbers less than n using a list comprehension. """

    result = [num for num in range(2, n) if is_prime(num)]
    return result


print(primes_upto(100))
