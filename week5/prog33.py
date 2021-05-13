def change_pos():
    arr = list(map(int, input().split()))
    maxEl = max(arr)
    minEl = min(arr)
    indf = arr.index(maxEl)
    indl = arr.index(minEl)
    arr[indf], arr[indl] = arr[indl], arr[indf]
    print(*arr)


change_pos()
