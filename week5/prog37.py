def printer():
    arr = list(map(int, input().split()))
    arr2 = []
    for i in arr:
        if arr.count(i) == 1:
            arr2.append(i)
    print(*arr2)


printer()
