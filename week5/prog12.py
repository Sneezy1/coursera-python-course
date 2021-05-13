def palindrom():
    a = int(input())
    b = int(input())
    for i in range(a, b + 1):
        pal = tuple(str(i))
        if pal[0] == pal[3] and pal[1] == pal[2]:
            print(i)


palindrom()
