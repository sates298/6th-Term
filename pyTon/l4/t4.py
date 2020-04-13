from inspect import getfullargspec
from math import sqrt


class overload:
    map = {}

    def __init__(self, func):
        args = getfullargspec(func).args
        self._name = func.__name__
        if func.__name__ not in overload.map:
            overload.map[self._name] = {}
        overload.map[self._name][len(args)] = func

    def __call__(self, *args):
        return overload.map[self._name][len(args)](*args)


@overload
def norm(x, y):
    return sqrt(x*x + y*y)


@overload
def norm(x, y, z):
    return abs(x) + abs(y) + abs(z)


@overload
def norm2(x, y):
    return x + y


@overload
def norm2(x, y, z):
    return x - y - z


# %%
if __name__ == '__main__':
    print(f"norm(2,4) = {norm(2,4)}")
    print(f"norm(2,3,4) = {norm(2,3,4)}")
    print(f"norm2(2,3) = {norm2(2,3)}")
    print(f"norm2(2,3,4) = {norm2(2,3,4)}")
