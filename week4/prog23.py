def move(n, x, y):
    if n == 1:
        print(n, x, y)
    else:
        tmp = 6 - x - y
        move(n - 1, x, tmp)
        print(n, x, y)
        move(n - 1, tmp, y)


a = int(input())
move(a, 1, 3)
