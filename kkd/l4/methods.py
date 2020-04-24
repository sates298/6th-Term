def s1(NW: int, N: int, W: int) -> int:
    return W


def s2(NW: int, N: int, W: int) -> int:
    return N


def s3(NW: int, N: int, W: int) -> int:
    return NW


def s4(NW: int, N: int, W: int) -> int:
    return N + W - NW


def s5(NW: int, N: int, W: int) -> int:
    return N + (W - NW)//2


def s6(NW: int, N: int, W: int) -> int:
    return W + (N - NW)//2


def s7(NW: int, N: int, W: int) -> int:
    return (N + W)//2


def ns(NW: int, N: int, W: int) -> int:
    if NW >= max(W, N):
        return max(W, N)
    if NW <= min(W, N):
        return min(W, N)
    return W + N - NW


methods_map = {
    '1': s1,
    '2': s2,
    '3': s3,
    '4': s4,
    '5': s5,
    '6': s6,
    '7': s7,
    'new': ns
}
