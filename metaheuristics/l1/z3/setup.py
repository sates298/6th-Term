import time
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
    le = (data[y][x-1], (x-1, y)) if x > 0 else (WALL, (x, y))
    u = (data[y-1][x], (x, y-1)) if y > 0 else (WALL, (x, y))
    r = (data[y][x+1], (x+1, y)) if x < len(data[0]) else (WALL, (x, y))
    d = (data[y+1][x], (x, y+1)) if y < len(data) else (WALL, (x, y))
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
    tabu = []
    curr = data[y][x]
    direction = ''
    l, u, r, d = get_neighbours(data, (x, y))
    if l[0] == EXIT:
        return LEFT, True, t_left-t_curr
    elif u[0] == EXIT:
        return UP, True, t_left-t_curr
    elif r[0] == EXIT:
        return RIGHT, True, t_left-t_curr
    elif d[0] == EXIT:
        return DOWN, True, t_left-t_curr
    if r[0] is not WALL:
        x, y = r[1]
        curr = r[0]
        direction = RIGHT
        result = RIGHT
    elif d[0] is not WALL:
        x, y = d[1]
        curr = d[0]
        direction = DOWN
        result = DOWN
    elif l[0] is not WALL:
        x, y = l[1]
        curr = l[0]
        direction = LEFT
        result = LEFT
    elif u[0] is not WALL:
        x, y = u[1]
        curr = u[0]
        direction = UP
        result = UP
    else:
        return '', False, 0
    tabu.append((x, y))
    t_curr = time.time() - start
    if t_curr > t_left:
        return result, False, 0

    while curr == EMPTY or curr == ENTRY:
        l, u, r, d = get_neighbours(data, (x, y))
        t_curr = time.time() - start
        if l[0] == EXIT:
            return result + LEFT, True, t_left-t_curr
        elif u[0] == EXIT:
            return result + UP, True, t_left-t_curr
        elif r[0] == EXIT:
            return result + RIGHT, True, t_left-t_curr
        elif d[0] == EXIT:
            return result + DOWN, True, t_left-t_curr
        if direction == RIGHT:
            if r[0] is not WALL and r[1] not in tabu:
                x, y = r[1]
                curr = r[0]
            elif d[0] is not WALL and d[1] not in tabu:
                x, y = d[1]
                curr = d[0]
                direction = DOWN
            elif u[0] is not WALL and u[1] not in tabu:
                x, y = u[1]
                curr = u[0]
                direction = UP
            else:
                return result, False, 0
        elif direction == LEFT:
            if l[0] is not WALL and l[1] not in tabu:
                x, y = l[1]
                curr = l[0]
            elif u[0] is not WALL and u[1] not in tabu:
                x, y = u[1]
                curr = u[0]
                direction = UP
            elif d[0] is not WALL and d[1] not in tabu:
                x, y = d[1]
                curr = d[0]
                direction = DOWN
            else:
                return result, False, 0
        elif direction == UP:
            if u[0] is not WALL and u[1] not in tabu:
                x, y = u[1]
                curr = u[0]
            elif r[0] is not WALL and r[1] not in tabu:
                x, y = r[1]
                curr = r[0]
                direction = RIGHT
            elif l[0] is not WALL and l[1] not in tabu:
                x, y = l[1]
                curr = l[0]
                direction = LEFT
            else:
                return result, False, 0
        elif direction == DOWN:
            if d[0] is not WALL and d[1] not in tabu:
                x, y = d[1]
                curr = d[0]
            elif l[0] is not WALL and l[1] not in tabu:
                x, y = l[1]
                curr = l[0]
                direction = LEFT
            elif r[0] is not WALL and r[1] not in tabu:
                x, y = r[1]
                curr = r[0]
                direction = RIGHT
            else:
                return result, False, 0
        tabu.append((x, y))
        result += direction
        if t_curr > t_left:
            return result, False, 0
