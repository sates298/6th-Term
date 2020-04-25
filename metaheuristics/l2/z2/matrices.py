from sys import stdin, stdout, stderr
from math import exp
from copy import deepcopy
import random
import time
from blocks import Matrix


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


def get_neighbour(matrix, values):
    neighbour = deepcopy(matrix)
    while not neighbour.changed:
        r = random.random()
        if r > 0.66:
            neighbour.change_one_color(values)
        elif r > 0.33:
            neighbour.swap_2_blocks()
        else:
            neighbour.stretch_one()
    return neighbour


def find_prim(t_max, M, n, m, k):
    values = [0, 32, 64, 128, 160, 192, 223, 225]
    T = 1_000_000
    last_epsilon = 0.00000000000001
    red_factor = 0.05
    t_start = time.time()
    c = .5 + .5*random.random()
    best_x = Matrix(m, n, k).generate_start(values)
    best_y = mse(M, best_x.to_matrix())
    max_iter = 10
    iter = 0
    while T > last_epsilon:
        x_p = get_neighbour(best_x, values)
        y_p = mse(M, x_p.to_matrix())
        del_f = -(best_y - y_p)
        r = random.random()
        if p(del_f, c, T) > r:
            best_x = x_p
            best_y = y_p
            iter = 0
        else:
            iter += 1
        T = (1 - red_factor)*T if iter < max_iter else T*(1 + iter*red_factor)
        t_curr = time.time() - t_start
        if t_curr >= t_max:
            break

    return best_x, best_y


def print_matrix(M):
    for i in M.to_matrix():
        stderr.write(' '.join(map(lambda x: str(x), i)) + '\n')


def main():
    in_ = stdin.readlines()
    t_max, n, m, k = [int(x) for x in in_[0].split()]
    data = [[int(c) for c in line.replace('\n', '').split()]
            for line in in_[1:]]
    out_ = find_prim(t_max, data, n, m, k)
    stdout.write(f' {out_[1]}\n')
    print_matrix(out_[0])


if __name__ == '__main__':
    main()
