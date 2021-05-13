from math import sqrt


def distance(x1, y1, x2, y2):
    res = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return res


print(distance(float(input()), float(input()), float(input()), float(input())))
