def archive():
    data = []
    arr_param = list(map(int, input().split()))
    maxs = arr_param[0]
    for i in range(arr_param[1]):
        data.append(int(input()))
    data.sort()
    res = 0
    count = 0
    for i in range(len(data)):
        if res + data[i] < maxs:
            res += data[i]
            count += 1
    print(count)


archive()
