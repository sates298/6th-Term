from math import log2


def elias_delta(N):
    result = ''
    if N > 0:
        x = int(log2(N))
        y = int(log2(x+1))
        result = '0'*y
        result += '{0:b}'.format(x+1)
        result += '{0:b}'.format(N)[1:]
    return result


def elias_delta_dec(code):
    result = []
    while code:
        L = code.index('1')
        code = code[L:]
        N = int(code[:L+1], 2) - 1
        code = code[L+1:]
        result.append(int('1' + code[:N], 2))
        code = code[N:]
    return result


def elias_gamma(N):
    result = ''
    if N > 0:
        x = int(log2(N))
        result = '0'*x
        result += '{0:b}'.format(N)
    return result


def elias_gamma_dec(code):
    result = []
    while code:
        i = code.index('1')
        code = code[i:]
        result.append(int(code[:i+1], 2))
        code = code[i + 1:]
    return result


def elias_omega(N):
    result = ['0']
    while N > 1:
        curr = '{0:b}'.format(N)
        result.append(curr)
        N = len(curr) - 1
    return ''.join(reversed(result))


def elias_omega_dec(code):
    result = []
    N = 1
    while code:
        if code[0] == '0':
            code = code[1:]
            result.append(N)
            N = 1
        else:
            curr = code[:N+1]
            code = code[N+1:]
            N = int(curr, 2)
    return result


def fib_memory(f):
    memory = {}
    memory_v = {}

    def inner(num, target):
        i = 0
        if num not in memory:
            memory[num] = f(num, target)[0]
            memory_v[memory[num]] = num
        if target:
            for val in sorted(memory.values(), reverse=True):
                if i == 0 and val < target:
                    break
                if val <= target:
                    return val, True, memory_v[val]
                i += 1
        return memory[num], False, 0
    return inner


@fib_memory
def fib_num(N, target):
    if N < 1:
        return 0, (False if target and target > 0 else True), 0
    if N == 1:
        return 1, (False if target and target > 1 else True), 0
    f1 = fib_num(N-1, target)
    f2 = fib_num(N-2, target)
    if f1[1]:
        return f1
    if f2[1]:
        return f2
    return f1[0] + f2[0], False, 0


def fibbonacci(N):
    result = []
    while N > 0:
        for i in range(N+2):
            score = fib_num(i, N)
            if score[1]:
                break
        N -= score[0]
        if len(result) == 0:
            result = ['0' for _ in range(score[2]-2)] + ['1', '1']
        else:
            result[score[2] - 2] = '1'

    return ''.join(result)


def fibbonacci_dec(code):
    result = []
    words = map(lambda x: x + '1', code.split('11')[:-1])
    for s in words:
        curr = 0
        for i in range(len(s), 0, -1):
            if s[i-1] == '1':
                curr += fib_num(i+1, None)[0]
        result.append(curr)
    return result
