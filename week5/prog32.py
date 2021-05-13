def shift_els():
    arr = list(map(int, input().split()))
    x = []
    size = len(arr)
    x.append(arr[size - 1])
    for i in range(size - 1):
        x.append(arr[i])
    print(*x)


shift_els()
