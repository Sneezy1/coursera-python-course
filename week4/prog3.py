from math import sqrt


def distance(x1, y1, x2, y2):
    res = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return res


def perimetr(x1, y1, x2, y2, x3, y3):
    l1 = distance(x1, y1, x2, y2)
    l2 = distance(x1, y1, x3, y3)
    l3 = distance(x2, y2, x3, y3)
    return l1 + l2 + l3


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

print(perimetr(x1, y1, x2, y2, x3, y3))
