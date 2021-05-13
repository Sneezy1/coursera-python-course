def changepos():
    arr = list(map(int, input().split()))
    k = len(arr) - 1
    while k > -1:
        if arr[k] == 0:
            arr.append(arr.pop(k))
        k -= 1
    print(*arr)


changepos()
