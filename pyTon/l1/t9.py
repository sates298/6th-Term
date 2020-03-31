from math import *


def calc():
    print('Calculator ')
    expr = 'start'
    i = 0
    while True:
        expr = input('[{}]: '.format(i))
        if expr == 'exit': break
        if '^' in expr:
            expr = expr.replace('^','**')
        if 'import' in expr: continue
        try:
            result = eval(expr)
            print(result)
        except ZeroDivisionError:
            print('Division by zero')
        except SyntaxError:
            print('Syntax Error')
        except NameError:
            print('Unknown parameter')
        i += 1

calc()