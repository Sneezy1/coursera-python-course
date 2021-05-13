def queen():
    x = []
    y = []
    count = 0
    for i in range(8):
        arr = list(map(int, input().split()))
        x.append(arr[0])
        y.append(arr[1])
    for j in range(8):
        for k in range(8):
            if j != k:
                if x[j] == x[k] or y[j] == y[k] or \
                            abs(x[k] - x[j]) == abs(y[k] - y[j]):
                    count += 1
    if count >= 1:
        print('YES')
    else:
        print('NO')


queen()
