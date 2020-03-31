from sys import stdin, stdout
import time
import random


def path_length(data, path):
    length = 0
    for from_, to in zip(path, path[1:] + [0]):
        length += data[from_][to]
    return length


def neighbourhood(path, n):
    cities = path[1:]
    first = path[0]
    neighbours = []
    for i in range(n-1):
        for j in range(i+1, n-1):
            curr = cities.copy()
            curr[i], curr[j] = curr[j], curr[i]
            neighbours.append([first] + curr)
    return neighbours


def tabu_search(t_max, cities_no, data, tabu_size=100):
    start = time.time()
    t_curr = 0
    best_path = [0] + random.sample(range(1, cities_no), cities_no-1)
    prev = best_path
    tabu = [best_path]
    best_length = path_length(data, best_path)
    while t_curr < t_max:
        neighbours = neighbourhood(best_path, cities_no)
        for n in neighbours:
            if n not in tabu:
                curr_len = path_length(data, n)
                if curr_len <= best_length:
                    best_path = n
                    best_length = curr_len
        if prev == best_path:
            return best_length, best_path + [0]
        else:
            prev = best_path
        tabu.append(best_path)
        if len(tabu) > tabu_size:
            tabu = tabu[1:]
        t_curr = time.time() - start
    return best_length, best_path + [0]


def main():
    # tabu_size = 100
    in_ = [[int(x) for x in s.split()] for s in stdin.readlines()]
    out_ = tabu_search(*in_[0], in_[1:])

    stdout.write(str(out_[0]) + '\n')
    stdout.write(' '.join(map(lambda x: str(x+1), out_[1])) + '\n')


if __name__ == "__main__":
    main()
