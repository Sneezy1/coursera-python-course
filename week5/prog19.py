def printer():
    listN = list(map(int, input().split()))
    maxall = 1001
    for i in listN:
        if i > 0 and i < maxall:
                maxall = i
    print(maxall)
printer()
