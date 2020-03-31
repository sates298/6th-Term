def faczero(n):
    if n not in range(0,10001):
        return 1
    zero = 0
    result = 1
    for i in range(1,n+1):
        k = i
        while k % 5 == 0:
            zero += 1
            k /= 5
        result *= i

    return result, zero

print(faczero(24))