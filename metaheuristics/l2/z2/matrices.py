from sys import stdin, stdout, stderr
from math import exp
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


def get_neighbour(M, k, values):
    pass


# def find_random_neighbor(sol: Solution, k):
#     new_sol = deepcopy(sol)
#     if random.random() < 0.5:
#         block = random.choice(sol)
#
#         w = block.width
#         h = block.height
#         start_col = block.start_col
#         start_row = block.start_row
#         val = block.value
#
#         if w < k and h < k:
#             return sol
#
#         block1 = None
#         block2 = None
#
#         if random.random() < 0.5:
#             try:
#                 split = random.choice(range(start_row + k, h - k + 1))
#             except IndexError:
#                 return sol
#             start_row_1 = start_row
#             height1 = h - split
#             height2 = split
#             start_row_2 = start_row + split
#
#             block1 = Block(start_row_1, start_col, w, height1, randcolor())
#             block2 = Block(start_row_2, start_col, w, height2, randcolor())
#
#         else:
#             try:
#                 split = random.choice(range(start_col + k, w - k + 1))
#             except IndexError:
#                 return sol
#             start_col_1 = start_col
#             width1 = w - split
#
#             start_col_2 = start_col + split
#             width2 = split
#
#             val = random.choice(ALLOWED)
#             block1 = Block(start_row, start_col_1, width1, h, randcolor())
#             block2 = Block(start_row, start_col_2, width2, h, randcolor())
#
#         new_sol.remove(block)
#         new_sol.extend([block1, block2])
#         return new_sol
#     else:
#         block = random.choice(new_sol)
#         new_block = Block(start_row=block.start_row, start_col=block.start_col,
#                           width=block.width, height=block.height,
#                           value=randcolor())
#         new_sol.remove(block)
#         new_sol.append(new_block)
#         return new_sol


def find_prim(t_max, M, k):
    values = [0, 32, 64, 128, 160, 192, 223, 225]
    T = 1_000_000
    last_epsilon = 0.00000000000001
    red_factor = 0.05
    t_start = time.time()
    c = .5 + .5*random.random()
    # best_x = generate_start(values)
    # best_y = mse(M, best_x)
    max_iter = 10
    iter = 0
    while T > last_epsilon:
        x_p = get_neighbour(best_x, k, values)
        y_p = mse(M, x_p)
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
    for i in M:
        stderr.write(' '.join(map(lambda x: str(x), i)) + '\n')


def main():
    values = [0, 32, 64, 128, 160, 192, 223, 225]
    in_ = stdin.readlines()
    t_max, n, m, k = [int(x) for x in in_[0].split()]
    data = [[int(c) for c in line.replace('\n', '').split()]
            for line in in_[1:]]
    matrix = Matrix(m, n, k)
    print_matrix(matrix.generate_start(values).to_matrix())
    # out_ = find_prim(t_max, data, k)
    stdout.write(f' {out_[1]}\n')
    print_matrix(out_[0])


if __name__ == '__main__':
    main()
