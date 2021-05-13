def change_pos():
    arr = list(map(int, input().split()))
    i = 0
    if len(arr) % 2 == 1:
        while i < len(arr) - 1:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i += 2
        print(*arr)
    elif len(arr) % 2 == 0:
        while i < len(arr):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i += 2
        print(*arr)


change_pos()
