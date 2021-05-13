def sork_drob(a, b):
    if a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    elif a > b:
        return a
    else:
        return b
    return sork_drob(a, b)


p, q = int(input()), int(input())
d = sork_drob(p, q)
print(p // d, q // d)
