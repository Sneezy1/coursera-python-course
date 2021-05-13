def printer():
    listN = list(map(int, input().split()))
    for i in range(1, len(listN)):
        if listN[i] > listN[i - 1]:
            print(listN[i], end=' ')


printer()
