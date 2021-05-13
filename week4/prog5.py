from math import sqrt


def IsPointInSquare(x, y):
    return sqrt(x ** 2) + sqrt(y ** 2) <= 1


def Printer(x, y):
    if IsPointInSquare(x, y):
        return 'YES'
    return 'NO'


print(Printer(float(input()), float(input())))
