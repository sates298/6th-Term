from math import log2
from collections import Counter
import sys
import getopt
import methods


def read_file_by_bytes(file):
    chars = []
    with open(file, "rb") as f:
        while byte:= f.read(1):
            chars.append(byte)
    return chars


def read_file_by_chars(file):
    text = ''
    with open(file, "r") as f:
        text = f.read()
    return text


def write_to_file_chars(file, code):
    with open(file, 'w') as f:
        f.write(code)


def write_to_file_bytes(file, code):
    with open(file, 'wb') as f:
        f.write(code)


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
    out.append(dictionary[c])
    return out


def lzw_decode(codes, dictionary):
    counter = len(dictionary) + 1
    pk = codes.pop(0)
    out = dictionary[pk]
    for k in codes:
        pc = dictionary[pk]
        if k in dictionary:
            string = dictionary[k]
            dictionary[counter] = pc + string[:1]
            out += string
        else:
            b_string = pc + pc[:1]
            dictionary[counter] = b_string
            out += b_string
        pk = k
        counter += 1
    return out


def compress(text, coding_method):
    dictionary = {i.to_bytes(1, 'big'): i+1 for i in range(2**8)}
    code = ''.join([coding_method(i) for i in lzw_encode(text, dictionary)])
    t_len = len(text)*8
    c_len = len(code)
    cr = t_len/c_len
    t_entropy = entropy(Counter(text).values(), t_len/8)
    c_entropy = entropy(Counter(code).values(), c_len)
    return code, (t_len, c_len, cr), (t_entropy, c_entropy)


def decompress(code, decoding_method):
    codes = decoding_method(code)
    dictionary = {i+1: i.to_bytes(1, 'big') for i in range(2**8)}
    return lzw_decode(codes, dictionary)


def stats(compression, entropy):
    print(f'Original text/file length: {compression[0]} bits')
    print(f'Compressed code length: {compression[1]} bits')
    print(f'Compression rate: {compression[2]}')
    print('----------------------------------------------------------')
    print(f'Original text/file entropy (by bytes): {entropy[0]}')
    print(f'Compressed code entropy (by bits): {entropy[1]}')
    print('==========================================================')


def main():
    coding_method = methods.elias_omega
    decoding_method = methods.elias_omega_dec
    opts, _ = getopt.gnu_getopt(sys.argv[1:], 'edi:o:',
                                ['gamma', 'delta', 'fibb', 'omega'])
    encoding = True
    for opt, arg in opts:
        if opt == '-i':
            file_in = arg
        elif opt == '-o':
            file_out = arg
        elif opt == '-e':
            for opt1, _ in opts:
                if opt1 == '--gamma':
                    coding_method = methods.elias_gamma
                elif opt1 == '--delta':
                    coding_method = methods.elias_delta
                elif opt1 == '--fibb':
                    coding_method = methods.fibbonacci
                elif opt1 == '--omega':
                    coding_method = methods.elias_omega
        elif opt == '-d':
            encoding = False
            for opt1, _ in opts:
                if opt1 == '--gamma':
                    decoding_method = methods.elias_gamma_dec
                elif opt1 == '--delta':
                    decoding_method = methods.elias_delta_dec
                elif opt1 == '--fibb':
                    decoding_method = methods.fibbonacci_dec
                elif opt1 == '--omega':
                    decoding_method = methods.elias_omega_dec

    if encoding:
        text = read_file_by_bytes(file_in)
        code, compression, entropy = compress(text, coding_method)
        write_to_file_chars(file_out, code)
        stats(compression, entropy)
    else:
        code = read_file_by_chars(file_in)
        decoded = decompress(code, decoding_method)
        write_to_file_bytes(file_out, decoded)


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
    print('delta:      ', delta, ', decoded: ', d_delta)
    print('gamma:      ', gamma, ', decoded: ', d_gamma)
    print('omega:      ', omega, ', decoded: ', d_omega)
    print('fibbonacci: ', fib, ', decoded: ', d_fib)


if __name__ == '__main__':
    main()
    # test()
