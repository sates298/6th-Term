import time
import random
from sys import stdout, stdin
from math import sqrt, pi, cos, exp


def norm(x):
    return sqrt(sum(map(lambda e: e*e, x)))


def salomon(x):
    return 1 - cos(2*pi*norm(x)) + .1*norm(x)


def p(delta, c, T):
    try:
        ans = 0 if delta < 0 else exp(c*delta/T)
    except OverflowError:
        ans = float('inf')
    return 1/(1+ans)


def get_neighbour(x, eps, rep):
    size = len(x)
    changes = random.choices([-eps, 0, eps], k=size)

    return tuple(x[i] + changes[i]*rep for i in range(size))


def annealing(f, start_pnt, t_max):
    T = 1_000_000
    last_epsilon = 0.00000000000001
    epsilon = 0.005
    red_factor = 0.05
    t_start = time.time()
    c = .5 + .5*random.random()
    best_x = start_pnt
    best_y = f(best_x)
    iter = 0
    while T > last_epsilon:
        x_p = get_neighbour(best_x, epsilon, iter)
        y_p = f(x_p)
        del_f = -(best_y - y_p)
        r = random.random()
        if p(del_f, c, T) > r:
            best_x = x_p
            best_y = y_p
            if del_f < 10**(-6):
                iter += 1
            else:
                iter = 0
        else:
            iter += 1
        T = (1 - red_factor)*T
        t_curr = time.time() - t_start
        if t_curr >= t_max:
            break

    return best_x, best_y


def main():
    in_ = list(map(lambda x: int(x), stdin.read().split()))
    out_ = annealing(salomon, in_[1:], in_[0])
    stdout.write(' '.join(map(lambda x: str(x), out_[0])) + f' {out_[1]}\n')


if __name__ == '__main__':
    main()
