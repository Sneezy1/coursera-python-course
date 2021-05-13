from math import sqrt
a = float(input())
b = float(input())
c = float(input())
diskr = (b ** 2) - (4 * a * c)
if a == 0 and c == 0 and b == 0:
    print(3)
elif diskr > 0 and a != 0:
    x1 = (-b + sqrt(diskr)) / (2 * a)
    x2 = (-b - sqrt(diskr)) / (2 * a)
    if x1 > x2:
        x1, x2 = x2, x1
    print(2, '{:.5f} {:.5f}'.format(x1, x2))
elif diskr == 0 and a != 0:
    x3 = -b / (2 * a)
    print(1, '{:.5f}'.format(x3))
elif a == 0 and b != 0:
    x3 = -c / b
    print(1, '{:.5f}'.format(x3))
else:
    print(0)
