from sys import stdin, stdout, stderr
from math import exp


def mse(M, Mp):
    n = len(M)
    m = len(M[0])
    sum = 0
    for i in range(n):
        for j in range(m):
            sum += (M[i][j] - Mp[i][j])*(M[i][j] - Mp[i][j])
    return sum/(n*m)


def p(delta, c, T):
    try:
        ans = 0 if delta < 0 else exp(c*delta/T)
    except OverflowError:
        ans = float('inf')
    return 1/(1+ans)


def get_neighbour(M, k):
    pass


def find_prim(t_max, M, k):
    values = [0, 32, 64, 128, 160, 192, 223, 225]
    print_matrix(M)


def print_matrix(M):
    for i in M:
        stderr.write(' '.join(map(lambda x: str(x), i)) + '\n')


def main():
    in_ = stdin.readlines()
    t_max, n, m, k = [int(x) for x in in_[0].split()]
    data = [[int(c) for c in line.replace('\n', '').split()] for line in in_[1:]]
    out_ = find_prim(t_max, data, k)
    stdout.write(f' {out_[1]}\n')


if __name__ == '__main__':
    main()
