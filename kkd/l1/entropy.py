from math import log2
import collections as coll
import sys
import time

def read_file_by_bytes(file):
    chars = []
    with open(file, "rb") as f:
        while byte := f.read(1):
            chars.append(byte)
    return chars

def H_Y_X(X_c, Y_c, size):
    sum2 = sum([sum([v2*(log2(v1) - log2(v2)) for y,v2 in Y_c.items() if y[0] == x]) for x,v1 in X_c.items()])
    return sum2/size

def H_X(P, X_c):
    return -sum([P[x]*log2(P[x]) for x in X_c])


def main():
    start = time.time()
    file_name = sys.argv[1]
    X = read_file_by_bytes(file_name)
    Y = list(zip([b'\x00'] + X, X))
    X_c, Y_c = coll.Counter(X), coll.Counter(Y)
    size = len(X)
    P = {x: (v/size) for x,v in X_c.items()}
    X_cond = {k: v for k,v in X_c.items()}
    if b'\x00' in X_cond:
        X_cond[b'\x00'] += 1
    else:
        X_cond[b'\x00'] = 1
    # P_y = {y: (v/size) for y,v in Y_c.items()}


    entr , cond_entr = H_X(P, X_c), H_Y_X(X_c, Y_c, size)
    print('entropy: ', entr)
    print('conditional entropy: ', cond_entr)
    print('difference: ', abs(entr-cond_entr))
    print(time.time() - start)

if __name__ == "__main__":
    main()