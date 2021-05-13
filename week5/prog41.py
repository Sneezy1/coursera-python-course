def maxrep():
    arr = list(map(int, input().split()))
    i = 0
    max_c = 0
    for j in range(len(arr)):
        new_c = arr.count(arr[j])
        if new_c > max_c:
            max_c = new_c
            i = j
    print(arr[i])


maxrep()
