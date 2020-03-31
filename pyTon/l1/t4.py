from math import sqrt
import numpy as np

def is_prime(x):
    if x == 2:
        return True
    if x < 2:
        return False
    for d in range(2, int(sqrt(x)) + 1):
        if x % d == 0:
            return False
    return True


def prime_factors(n):
    factors = []
    for p in range(n+1):
        if is_prime(p): 
            while n % p == 0:
                factors.append(p)
                n /= p
    fact = np.array(factors)
    unq, cnt = np.unique(fact, return_counts=True)
    return list(zip(unq, cnt))

print(prime_factors(1))
            