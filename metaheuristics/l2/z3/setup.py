import time
import random
EMPTY = '0'
WALL = '1'
EXIT = '8'
ENTRY = '5'

UP = 'U'
DOWN = 'D'
RIGHT = 'R'
LEFT = 'L'


def get_neighbours(data, point):
    x, y = point
    le = (data[y][x-1], (x-1, y), LEFT) if x > 0 else (WALL, (x, y))
    u = (data[y-1][x], (x, y-1), UP) if y > 0 else (WALL, (x, y))
    r = (data[y][x+1], (x+1, y), RIGHT) if x < len(data[0]) else (WALL, (x, y))
    d = (data[y+1][x], (x, y+1), DOWN) if y < len(data) else (WALL, (x, y))
    return (le, u, r, d)


def find_entry(data, rows_no):
    for y in range(rows_no):
        if ENTRY in data[y]:
            return (data[y].index(ENTRY), y)
    return (0, 0)


def find_exit(data, entry, t_left):
    x, y = entry
    start = time.time()
    t_curr = 0
    curr = data[y][x]
    result = ''

    while curr == EMPTY or curr == ENTRY:
        l, u, r, d = get_neighbours(data, (x, y))
        if l[0] == EXIT:
            return result + LEFT, True, t_left-t_curr
        elif u[0] == EXIT:
            return result + UP, True, t_left-t_curr
        elif r[0] == EXIT:
            return result + RIGHT, True, t_left-t_curr
        elif d[0] == EXIT:
            return result + DOWN, True, t_left-t_curr

        to_rand = []
        if r[0] is not WALL:
            to_rand.append(r)
        if d[0] is not WALL:
            to_rand.append(d)
        if u[0] is not WALL:
            to_rand.append(u)
        if l[0] is not WALL:
            to_rand.append(l)
        if not to_rand:
            return result, False, 0

        curr_tuple = random.choice(to_rand)
        x, y = curr_tuple[1]
        curr = curr_tuple[0]
        result += curr_tuple[2]
        t_curr = time.time() - start
        if t_curr > t_left:
            return result, False, 0
    return result, False, 0
