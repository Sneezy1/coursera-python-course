def max2(a, b):
    if a > b:
        return a
    return b


def max3(a, b, c):
    return max(max2(a, b), c)
print(max2(2, 5))
print(max2(7, 3))
print(max2(2, 2))
print(max3(1, 2, 3))
