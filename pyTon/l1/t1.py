def _pascal(f):
    triangle = {}

    def inner(row, num):
        if row not in triangle:
            triangle[row] = {}
        if num not in triangle[row]:
            triangle[row][num] = f(row, num)
        return triangle[row][num]
    return inner


@_pascal
def _pascal_value(row, place):
    if place == 1:
        return 1
    return (_pascal_value(row, place-1)*(row - place+1)) // (place-1)


def _print_pascal(tr, n):
    splits = []
    max_ = max([len(str(x)) for x in tr[-1]])
    for i in range(n):
        str_ = ' '*(n-i)*max_
        for j in range(i+1):
            str_ += ' %{}d'.format(2*max_ - 1) % tr[i][j]
        splits.append(str_)
    for k in splits:
        print(k)


def pascal_triangle(n):
    triangle = []
    for row_n in range(1, n+1):
        row = []
        for place in range(1, row_n+1):
            row.append(_pascal_value(row_n, place))
        triangle.append(row)

    _print_pascal(triangle, n)


pascal_triangle(6)
