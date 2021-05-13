def magaz():
    legsize = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    k = 0
    for i in range(len(arr)):
        if arr[i] >= legsize:
            legsize = arr[i] + 3
            k += 1
    print(k)


magaz()
