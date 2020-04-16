import time
import random
from sys import stdout, stdin
from math import sqrt, pi, cos, exp


def norm(x):
    return sqrt(sum(map(lambda e: e*e, x)))


def salomon(x):
    return 1 - cos(2*pi*norm(x)) + .1*norm(x)


def p(delta, c, T):
    return 1/(1+exp(c*delta/T))


def get_neighbour(x, eps):
    size = len(x)
    f, s = random.sample(list(range(size)), k=2)
    f1, s1 = random.choices([-eps, 0, eps], k=2)
    neighbour = x.copy()
    neighbour[f] += f1
    neighbour[s] += s1
    return neighbour


def annealing(f, start_pnt, t_max):
    T = 37
    red_factor = 0.3
    t_start = time.time()
    c = .5 + .5*random.random()
    best_x = start_pnt
    best_y = f(best_x)
    while T > 0:
        x_p = get_neighbour(best_x)
        y_p = f(x_p)
        del_f = -(best_y - y_p)
        r = random.random()
        if p(del_f, c, T) > r:
            best_x = x_p
            best_y = y_p
        T = (1 - red_factor)*T
        t_curr = time.time() - t_start
        if t_curr < t_max:
            break

    return best_x, best_y


def main():
    in_ = list(map(lambda x: int(x), stdin.read().split()))
    out_ = annealing(salomon, in_[1:], in_[0])
    stdout.write(' '.join(map(lambda x: str(x), out_)) + '\n')


if __name__ == '__main__':
    main()
