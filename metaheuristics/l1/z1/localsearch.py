from functools import reduce
from math import pow, cos, sqrt
from sys import stdin, stdout
import time
import random

# x = (x1,x2,x3,x4)


def happy_cat(x):
    norm_2 = abs(sum([pow(i, 2) for i in x]))
    first = pow(pow(norm_2 - 4, 2), 0.125)
    second = 0.25*(0.5*norm_2 + sum(x))
    return first + second + 0.5

# x = (x1,x2,x3,x4)


def griewank(x):
    second = sum([pow(i, 2) for i in list(x)])*(1/4000)
    third = reduce(lambda x, y: x*y, [cos(x[i-1]/sqrt(i)) for i in range(1, 5)])
    return 1 + second - third


def neighbourhood(x, diff=0.01):
    result = []
    combs = [(diff*(-1)**i, diff*(-1)**(i//2)) for i in range(4)]
    sets = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3], [1], [2], [3], [0]]
    for s in sets:
        for i in range(2**len(s)):
            curr = x.copy()
            for j in range(len(s)):
                curr[s[j]] += combs[i][j]
            result.append(curr)
    return result


def localsearch(f, t_max, max_jumps):
    start = time.time()
    t_curr = 0
    best_global = [4*random.random()-2 for _ in range(4)]
    best_value = f(best_global)
    curr = best_global
    prev = best_global
    best_counter = 1
    while t_curr < t_max:
        neighbours = neighbourhood(curr)
        for n in neighbours:
            curr_val = f(n)
            if curr_val < best_value:
                best_global = n
                best_value = curr_val
        if prev == best_global:
            if best_counter > max_jumps:
                return best_global + [best_value]
            else:
                curr = [4*random.random()-2 for _ in range(4)]
                best_counter += 1
        else:
            prev = best_global
            curr = best_global
        t_curr = time.time() - start

    return best_global + [best_value]


def main():
    max_jumps = 1_000_000
    in_ = list(map(lambda x: int(x), stdin.read().split()))
    out_ = localsearch(happy_cat, in_[0], max_jumps) if in_[
        1] == 0 else localsearch(griewank, in_[0], max_jumps)
    stdout.write(' '.join(map(lambda x: str(x), out_)) + '\n')


if __name__ == "__main__":
    main()
