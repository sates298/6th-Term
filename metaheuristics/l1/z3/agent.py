from sys import stdin, stdout
from setup import UP, DOWN, RIGHT, LEFT
from setup import WALL, EXIT
from setup import find_exit, find_entry
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


def neighbourhood(path):
    l_path = list(path)
    size = len(path)
    neighbours = []
    for i in range(size):
        for j in range(i+1, size):
            curr = l_path.copy()
            curr[i], curr[j] = curr[j], curr[i]
            neighbours.append(remove_obvious(''.join(curr)))
    return neighbours


def agent_simulation(data, rows_no, columns_no, t_max):
    entry = find_entry(data, rows_no)
    best_path, success, t_left = find_exit(data, entry, t_max)
    best_len = len(best_path)
    if not success:
        return -1, ''
    tabu = [best_path]
    prev = best_path
    t_curr = 0
    start = time.time()
    while t_curr < t_left:
        ns = neighbourhood(best_path)
        for n in ns:
            if n not in tabu:
                appr, steps = exit_path(data, entry, n)
                if appr and steps < best_len:
                    best_path = n
                    best_len = steps
        if prev == best_path:
            return best_len, best_path
        else:
            prev = best_path
        tabu.append(best_path)
        t_curr = time.time() - start
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
