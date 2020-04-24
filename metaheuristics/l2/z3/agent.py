from sys import stdin, stdout
from setup import UP, DOWN, RIGHT, LEFT
from setup import WALL, EXIT
from setup import find_exit, find_entry
import random
import time
import math


def exit_path(data, entry, path):
    x, y = entry
    steps = 0
    for c in path:
        if c == UP:
            y -= 1
        elif c == DOWN:
            y += 1
        elif c == RIGHT:
            x += 1
        elif c == LEFT:
            x -= 1
        curr = data[y][x]
        steps += 1
        if curr == EXIT:
            return True, steps
        if curr == WALL:
            return False, steps
    return False, math.inf


def remove_obvious(path):
    size = len(path)
    prev = size + 1
    while prev > size:
        path = path.replace(
            LEFT+RIGHT, '').replace(
            RIGHT+LEFT, '').replace(
            UP+DOWN, '').replace(
            DOWN+UP, '')
        prev, size = size, len(path)
    return path


def p(delta, c, T):
    try:
        ans = 0 if delta < 0 else math.exp(c*delta/T)
    except OverflowError:
        ans = float('inf')
    return 1/(1+ans)


def get_neighbour(path):
    size = len(path)
    i, j = random.sample(list(range(size)), k=2)
    curr = list(path)
    curr[i], curr[j] = curr[j], curr[i]
    return remove_obvious(''.join(curr))


def agent_simulation(data, rows_no, columns_no, t_max):
    entry = find_entry(data, rows_no)
    best_path, success, t_left = find_exit(data, entry, t_max)
    best_len = len(best_path)
    if not success:
        return -1, ''
    T = 1_000_000
    last_epsilon = 0.00000000000001
    red_factor = 0.05
    t_start = time.time()
    c = .5 + .5*random.random()
    iter = 0
    max_iter = 5
    while T > last_epsilon:
        x_p = get_neighbour(best_path)
        while not exit_path(data, entry, x_p):
            x_p = get_neighbour(best_path)
        y_p = len(x_p)
        del_f = -(best_len - y_p)
        r = random.random()
        if p(del_f, c, T) > r:
            best_path = x_p
            best_len = y_p
            iter = 0
        else:
            iter += 1
        T = (1 - red_factor)*T if iter < max_iter else T*(1 + iter*red_factor)
        t_curr = time.time() - t_start
        if t_curr >= t_max:
            break
    return best_len, best_path


def main():
    in_ = stdin.readlines()
    data = [[c for c in line.replace('\n', '')] for line in in_[1:]]
    t_max, rows_no, columns_no = [int(x) for x in in_[0].split()]
    size, path = agent_simulation(data, rows_no, columns_no, t_max)
    stdout.write(str(size) + '\n')
    stdout.write(path + '\n')


if __name__ == "__main__":
    main()
