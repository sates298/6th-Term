import numpy as np
from math import pi
from cmath import exp
from functools import reduce


# %%


class FastBigNum:
    def __init__(self, num):
        print(num)
        self.number = [int(x) for x in reversed(num)]
        self.length = len(num)

    def __mul__(self, other):
        global dft, idft
        if self.length != other.length:
            raise ValueError("Not the same length of numbers")
        double_n = 2*self.length
        X = dft(self.number, double_n)
        Y = dft(other.number, double_n)
        Z = [X[i]*Y[i] for i in range(double_n)]
        result = idft(Z, double_n)
        value = reduce(lambda x, y: x + y[1]*10**y[0],
                       enumerate(result), 0)
        return FastBigNum(str(value))

    def __str__(self):
        val = reduce(lambda x, y: x + y[1]*10**y[0],
                     enumerate(self.number), 0)
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

# %% second implementation


def fft(x, n):
    diff = n - len(x)
    x.extend([0 for _ in range(diff)])
    return fft_rec(x)


def ifft(x, n):
    diff = n - len(x)
    x.extend([0 for _ in range(diff)])
    return ifft_rec(x)


def fft_rec(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft_rec(x[0::2])
    odd = fft_rec(x[1::2])
    T = [exp(-2j*pi*k/N)*odd[k] for k in range(N//2)]
    return [even[k] + T[k] for k in range(N//2)] + \
           [even[k] - T[k] for k in range(N//2)]


def ifft_rec(x):
    res = fft_rec([i.conjugate() for i in x])
    return [i.conjugate().real/len(x) for i in res]


# %% base tests
dft = base_dft
idft = base_idft

# %% own tests
dft = fft
idft = ifft

# %% numpy tests
dft = np.fft.fft
idft = np.fft.ifft


# %%

a = [1, 2, 3, 4, 5]
print(fft([1, 2, 3, 4], 5))
print(base_dft([1, 2, 3, 4], 5))


# %% counting tests
A = '1312312231232131231231231231231231212331233231349123123123123123'
B = '1212312311223123121312312321321231231112323123231123123123123123'
print(len(A))
a = FastBigNum(A)
b = FastBigNum(B)
print((a*b)*(a*b))
print(int(A)*int(B)*int(A)*int(B))
