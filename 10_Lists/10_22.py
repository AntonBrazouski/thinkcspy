# functions that produce lists
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
       for i in range(2, n):


def primes_upto(n):
    """ Return a list of all prime numbers Less than n. """
    result = []
        if is_prime(i):
            result.append(i)
    return result

print(primes_upto(12))
