from math import sqrt


def lagr(x, depth):
    if depth == 0:
        return 'NO'
    sqrtx = int(sqrt(x))
    if sqrtx * sqrtx == x:
        return str(sqrtx)
    while sqrtx > 0:
        if lagr(x - sqrtx * sqrtx, depth - 1) != 'NO':
            return str(sqrtx) + " " + lagr(x - sqrtx * sqrtx, depth - 1)
        sqrtx -= 1
    return 'NO'


xx = float(input())
print(lagr(xx, 4))
