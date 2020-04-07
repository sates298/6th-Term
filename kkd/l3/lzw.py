from math import log2
from collections import Counter
import sys
import methods


def read_file_by_bytes(file):
    chars = []
    with open(file, "rb") as f:
        while byte := f.read(1):
            chars.append(byte)
    return chars


def entropy(frequency, size):
    return -sum([(v/size)*(log2(v)-log2(size))
                for v in frequency if v > 0])


def lzw_encode(text, dictionary):
    counter = len(dictionary) + 1
    c = text[0]
    out = []
    for s in text[1:]:
        if c+s in dictionary:
            c += s
        else:
            out.append(dictionary[c])
            dictionary[c+s] = counter
            counter += 1
            c = s
    return out


def lzw_decode(code, dictionary, coding_method):
    pass


def compress(text, coding_method):
    dictionary = {i.to_bytes(1, 'big'): i+1 for i in range(2**8)}
    code = ''.join([coding_method(i) for i in lzw_encode(text, dictionary)])
    t_len = len(text)*8
    c_len = len(code)
    cr = t_len/c_len
    t_entropy = entropy(Counter(text).values(), t_len/8)
    c_entropy = entropy(Counter(code).values(), c_len)
    return code, (t_len, c_len, cr), (t_entropy, c_entropy)


def main():
    coding_method = methods.elias_omega
    file = sys.argv[1]
    text = read_file_by_bytes(file)
    print(compress(text, coding_method)[1:])


def test():
    array = [12, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 2, 3, 3]
    delta = ''.join(map(methods.elias_delta, array))
    gamma = ''.join(map(methods.elias_gamma, array))
    omega = ''.join(map(methods.elias_omega, array))
    fib = ''.join(map(methods.fibbonacci, array))
    d_delta = methods.elias_delta_dec(delta)
    d_gamma = methods.elias_gamma_dec(gamma)
    d_omega = methods.elias_omega_dec(omega)
    d_fib = methods.fibbonacci_dec(fib)
    print('delta: ', delta, ', decoded: ', d_delta)
    print('gamma: ', gamma, ', decoded: ', d_gamma)
    print('omega: ', omega, ', decoded: ', d_omega)
    print('fibbonacci: ', fib, ', decoded: ', d_fib)


if __name__ == '__main__':
    # main()
    test()
