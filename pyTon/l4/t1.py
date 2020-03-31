import time


def timer(f):
    def inner(*args):
        start = time.time()
        result = f(*args)
        end = time.time() - start
        print('time:', end)
        return result
    return inner


@timer
def test(a, b, c, d):
    for i in range(a*b):
        for j in range(c*d):
            for _ in range(i*j):
                c = a + b


test(10, 20, 30, 40)
