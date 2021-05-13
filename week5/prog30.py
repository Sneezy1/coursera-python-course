def diff():
    arr = list(map(int, input().split()))
    arr2 = []
    i = 0
    for j in arr:
        if arr2.count(j) == 0:
            arr2.append(j)
    print(len(arr2))


diff()
