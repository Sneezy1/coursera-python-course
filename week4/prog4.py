def IsPointInSquare(x, y):
    return x ** 2 <= 1 and y ** 2 <= 1


def Printer(x, y):
    if IsPointInSquare(x, y):
        return 'YES'
    return 'NO'


print(Printer(float(input()), float(input())))
