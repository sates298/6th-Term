from inspect import getfullargspec
from math import sqrt


class overload:
    map = {}

    def __init__(self, func):
        args = getfullargspec(func).args
        overload.map[len(args)] = func

    def __call__(self, *args):
        return overload.map[len(args)](*args)


@overload
def norm(x, y):
    return sqrt(x*x + y*y)


@overload
def norm(x, y, z):
    return abs(x) + abs(y) + abs(z)


# %%
if __name__ == '__main__':
    print(f"norm(2,4) = {norm(2,4)}")
    print(f"norm(2,3,4) = {norm(2,3,4)}")
