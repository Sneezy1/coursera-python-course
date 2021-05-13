from math import sqrt
a = float(input())
b = float(input())
c = float(input())
diskr = (b ** 2) - (4 * a * c)
if diskr > 0:
    x1 = (-b + sqrt(diskr)) / (2 * a)
    x2 = (-b - sqrt(diskr)) / (2 * a)
    if x1 > x2:
        x1, x2 = x2, x1
    print('{:.5f} {:.5f}'.format(x1, x2))
elif diskr == 0:
    x3 = -b / (2 * a)
    print('{:.5f}'.format(x3))
