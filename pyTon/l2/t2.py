#!/bin/python
import getopt
import sys

array = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def encode(fin, fout):
    with open(fin, 'rb') as f:
        file = f.read()

    code = '0' + bin(int.from_bytes(file, 'big'))[2:]
    encoded = ''
    size = len(code)
    if size % 6 == 4:
        code += '00'
        padding = '='
    elif size % 6 == 2:
        code += '0000'
        padding = '=='
    else:
        padding = ''

    while code:
        curr = code[:6]
        code = code[6:]
        idx = int(curr, 2)
        encoded += array[idx]

    with open(fout, 'w') as f:
        f.write(encoded+padding)


def decode(fin, fout):
    with open(fin, 'r') as f:
        file = f.read()

    del_code = 0
    if file[-2:] == '==':
        file = file[:-2]
        del_code = -4
    elif file[-1] == '=':
        file = file[:-1]
        del_code = -2
    code = ''
    for c in file:
        curr = '{0:b}'.format(array.index(c))
        while len(curr) < 6:
            curr = '0' + curr
        code += curr
    code = code if del_code == 0 else code[:del_code]
    n = int(code, 2)
    decoded = n.to_bytes(
        (n.bit_length() + 7) // 8, 'big').decode(encoding='utf-8')
    with open(fout, 'w') as f:
        f.write(decoded)


def main():
    optlist, args = getopt.getopt(sys.argv[1:], '', ['encode', 'decode'])
    fin = args[0]
    fout = args[1]
    o = optlist[0][0]
    if o == '--encode':
        encode(fin, fout)
    else:
        decode(fin, fout)


if __name__ == "__main__":
    main()
