import numpy as np
from math import pi, log2
from cmath import exp
from functools import reduce
import time
import random


# %%


class FastBigNum:
    def __init__(self, num):
        self.length = len(num)
        self.number = [int(x) for x in reversed(num)]
        while not log2(self.length).is_integer():
            self.number.append(0)
            self.length += 1

    def __mul__(self, other):
        global dft, idft
        if self.length != other.length:
            raise ValueError("Not the same length of numbers")
        double_n = 2*self.length
        X = dft(self.number, double_n)
        Y = dft(other.number, double_n)
        Z = [X[i]*Y[i] for i in range(double_n)]
        result = idft(Z, double_n)
        value = reduce(lambda x, y: x + int(y[1])*10**y[0],
                       enumerate(result), 0)
        return FastBigNum(str(value))

    def __str__(self):
        val = reduce(lambda x, y: x + int(y[1])*10**y[0],
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
    if not log2(n).is_integer():
        raise ValueError("Length should be power of 2")
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
    conj = map(lambda e: e.conjugate(), x)
    res = fft_rec(list(conj))
    size = len(res)
    return [int(round(i.conjugate().real/size)) for i in res]


# %% numpy implementation

def numpy_fft(x, n):
    return np.fft.fft(x, n)


def numpy_ifft(x, n):
    return np.round(np.real(np.fft.ifft(x, n))).astype(int)


# %% base tests
dft = base_dft
idft = base_idft

# %% own tests
dft = fft
idft = ifft

# %% numpy tests
dft = numpy_fft
idft = numpy_ifft


# %% counting tests
def simple_test(size):
    curr_A = ''.join([random.choice("0123456789") for i in range(size)])
    curr_B = ''.join([random.choice("0123456789") for i in range(size)])
    a = FastBigNum(curr_A)
    b = FastBigNum(curr_B)
    print(a*b)
    # print(int(A)*int(B))


# start1 = time.time()
# simple_test(1_000_000)
# print(time.time() - start1)


# %% tests to file
file_name = 'fastbignum_benchmark.csv'


def avg(x):
    return sum(x)/len(x)


def write_table(table):
    with open(file_name, 'w') as f:
        f.write('size of nums, slow version, fast version, numpy version\n')
        for s, x, y, z in table:
            f.write(f'{s}, {x}, {y}, {z}\n')


def generate_element(size):
    global dft, idft
    curr_A = ''.join([random.choice("0123456789") for i in range(size)])
    curr_B = ''.join([random.choice("0123456789") for i in range(size)])
    a = FastBigNum(curr_A)
    b = FastBigNum(curr_B)
    # dft = base_dft
    # idft = base_idft
    # start = time.time()
    # a*b
    # base = time.time() - start
    base = 'N/A'
    dft = fft
    idft = ifft
    start = time.time()
    a*b
    fast = time.time() - start
    dft = numpy_fft
    idft = numpy_ifft
    start = time.time()
    a*b
    nump = time.time() - start

    return (size, base, fast, nump)


def final_test():
    samples_no = 5
    sizes = [100_000, 500_000, 1_000_000]
    with open(file_name, 'w') as f:
        f.write('size of nums, slow version, fast version, numpy version\n')
        for s in sizes:
            for _ in range(samples_no):
                _, x, y, z = generate_element(s)
                f.write(f'{s}, {x}, {y}, {z}\n')


final_test()
# generate_element(1000)
