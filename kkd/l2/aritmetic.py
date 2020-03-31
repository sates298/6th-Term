#!/bin/python
# from math import log2, ceil
# from functools import reduce

# _P = {b'a': 0.7, b'b': 0.1, b'c': 0.2}


def generate_interval(base_interval, sign):
    start = base_interval[0]
    end = base_interval[1]
    length = end - start
    prev = start
    intervals = {}
    for k, v in f.items():
        curr = prev + length*v/size
        intervals[k] = (prev, curr)
        prev = curr
    return intervals[sign]


def text_to_bin(text):
    return ''.join(format(ord(c), 'b') for c in text) + '#'


def decimal_converter(num):
    while num > 1:
        num /= 10
    return num


def float_bin(number, places=10):
    _, dec = str(number).split(".")
    dec = int(dec)
    res = ''
    for _ in range(places):
        whole, dec = str((decimal_converter(dec)) * 2).split(".")
        dec = int(dec)
        res += whole
    return res


def encode(text):
    global f, size
    bin_text = text_to_bin(text)
    l, p = (0, 1)
    counter = 0
    res = ''
    for s in bin_text:
        if s == '#':
            break
        l, p = generate_interval((l, p), s)
        f[s] += 1
        size += 1
        # scaling
        if p <= 0.5:
            p *= 2
            l *= 2
            res += '0' + '1'*counter
            counter = 0
        elif l >= 0.5:
            l -= 0.5
            p -= 0.5
            p *= 2
            l *= 2
            res += '1' + '0'*counter
            counter = 0
        elif 0.25 <= l < 0.5 and 0.5 < p <= 0.75:
            l -= 0.25
            p -= 0.25
            p *= 2
            l *= 2
            counter += 1
        # p += 1

    # z = l + (p-l)/2
    # m = 1 + ceil(log2(1/reduce(lambda x, y: x*y, [f[s]/size for s in bin_text])))

    # return float_bin(z)[:m], len(bin_text)-1
    return res, len(bin_text), (l, p)


def decode(code, P):
    pass


def main():
    global alphabet, size, f
    alphabet = ['0', '1']
    size = len(alphabet)
    f = {a: 1 for a in alphabet}
    text = 'abd'
    # z, n = encode(text)
    print(encode(text))


if __name__ == "__main__":
    main()
