import numpy as np
from math import pi
from cmath import exp
from functools import reduce


# %%


class FastBigNum:
    def __init__(self, num):
        self.number = [int(x) for x in num]

    def __mul__(self, other):
        global dft, idft
        double_n = 2*len(self.number)
        X = dft(self.number, double_n)
        Y = dft(other.number, double_n)
        Z = [X[i]*Y[i] for i in range(double_n)]
        result = idft(Z, double_n)
        return FastBigNum(result)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        val = reduce(lambda x, y: x + y[1]*10**y[0],
                     enumerate(reversed(self.number)), 0)
        return str(val)


# %% first implementation
def base_omega(k, n):
    return exp(-2j*k*pi/n)


def base_dft(x, n):
    return [sum(x[i]*base_omega(i*k, n) if i < len(x) else 0 for i in range(n))
            for k in range(n)]


def base_idft(x, n):
    return [int(round(sum(x[i]*base_omega(-i*k, n) if i < len(x) else 0
                          for i in range(n)).real)/n) for k in range(n)]


# %% tests
dft = base_dft
idft = base_idft

A = '1312312231232131231231231231231231212331233231349'
B = '1212312311223123121312312321321231231112323123231'
a = FastBigNum(A)
b = FastBigNum(B)
print(a*b*a*b)
print(int(A)*int(B)*int(A)*int(B))


# %% second implementation
def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    T = [exp(-2j*pi*k/N)*odd[k] for k in range(N//2)]
    return [even[k] + T[k] for k in range(N//2)] + \
           [even[k] - T[k] for k in range(N//2)]

# %% tests

# %%
# third implementation


# %% tests
dft = np.fft.fft
idft = np.fft.ifft

A = '1312312231232131231231231231231231212331233231349'
B = '1212312311223123121312312321321231231112323123231'
a = FastBigNum(A)
b = FastBigNum(B)
print(a*b)
print(int(A)*int(B))
