def printer():
    n = int(input())
    count = 10 ** n - 1
    сount2 = 10 ** (n - 1) - 1
    for i in range(count, сount2, -2):
        print(i, end=' ')


printer()
