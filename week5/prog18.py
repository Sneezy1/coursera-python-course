def printer():
    listN = list(map(int, input().split()))
    counter = 1
    for i in range(1, len(listN)):
        if listN[i] > listN[i - 1]:
            counter *= 1
        else:
            counter *= 0
    if counter == 1:
        print('YES')
    else:
        print('NO')


printer()
