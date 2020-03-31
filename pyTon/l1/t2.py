from math import sqrt


def is_prime(x):
    if x == 2:
        return True
    if x < 2:
        return False
    for d in range(2, int(sqrt(x)) + 1):
        if x % d == 0:
            return False
    return True


def primes(n):
    return [x for x in range(n+1) if is_prime(x)]


print(primes(100))
