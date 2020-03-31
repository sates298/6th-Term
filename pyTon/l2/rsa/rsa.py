#!/bin/python
import getopt
import sys
from math import log, gcd
import random
from functools import reduce
import re

file_key_prv = 'key.prv'
file_key_pbl = 'key.pbl'


def encrypt(text):
    with open(file_key_pbl, 'r') as key:
        n = int(key.readline())
        e = int(key.readline())
    b = [int.from_bytes(bytes(text, encoding='utf-8'), 'big')]
    texts = [text]
    while max(b) > n:
        if max([len(s) for s in texts]) == 1:
            raise ValueError('N is too small to encrypt that message')
        texts = reduce(
            lambda x, y: x + y, [[t[:len(t)//2], t[len(t)//2:]]
                                 for t in texts if len(t) > 0])
        texts = [t for t in texts if t != '']
        b = [int.from_bytes(bytes(t, encoding='utf-8'), 'big') for t in texts]

    c = map(lambda x: str(pow(x, e, n)), b)
    out = ' '.join(c)
    return out


def decrypt(code):
    with open(file_key_prv, 'r') as key:
        n = int(key.readline())
        d = int(key.readline())
    num = [int(s) for s in code.split(' ') if s != '']
    decoded = map(lambda x: str(pow(x, d, n).to_bytes(
        (x.bit_length() + 7) // 8, 'big'), 'utf-8'), num)
    result = ''.join(decoded)
    return result


def prime_test(n, k=8):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    d = n-1
    max_pow = 0
    while d % 2 == 0:
        max_pow += 1
        d //= 2
    for _ in range(k):
        a = int(random.uniform(1, n-1))
        res = pow(a, d, n)
        if res != 1:
            for r in [x for x in range(max_pow)]:
                if pow(a, d*(2**r), n) == n-1 % n:
                    break
            else:
                return False
    else:
        return True


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        return None
    else:
        return x % m


def coprime(a):
    common_e = 2**16 + 1
    if a > common_e and modinv(common_e, a) != common_e:
        return common_e
    return 7


def gen_keys(bits):
    random.seed()
    min_p = 2**bits
    max_p = 2**(bits+1)-1
    p, q = 0, 0
    while not prime_test(p):
        p = random.randint(min_p, max_p)
    while p == q or not prime_test(q):
        q = random.randint(min_p, max_p)
    n = p*q
    eul = (p-1)*(q-1)
    e = coprime(eul)
    d = modinv(e, eul)
    if d is not None:
        key_pbl = (n, e)
        key_prv = (n, d)
        with open(file_key_prv, 'w') as f:
            f.write(str(key_prv[0]))
            f.write('\n')
            f.write(str(key_prv[1]))
        with open(file_key_pbl, 'w') as f:
            f.write(str(key_pbl[0]))
            f.write('\n')
            f.write(str(key_pbl[1]))
    else:
        gen_keys(bits)


def main():
    optlist, args = getopt.getopt(
        sys.argv[1:], '', ['encrypt=', 'decrypt=', 'gen-keys='])
    opts = dict(optlist)
    if '--gen-keys' in opts:
        gen_keys(int(opts['--gen-keys']))
    elif '--encrypt' in opts:
        res = encrypt(opts['--encrypt'] + ' ' + ' '.join(args))
        print(res)
    elif '--decrypt' in opts:
        res = decrypt(opts['--decrypt'] + ' ' + ' '.join(args))
        print(res)


if __name__ == "__main__":
    main()
