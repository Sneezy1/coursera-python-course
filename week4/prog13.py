def sum(a, b):
    if b != 0:
        a = sum(a, b - 1) + 1
    return a


x, k = int(input()), int(input())
print(sum(x, k))
