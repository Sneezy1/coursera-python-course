def newprinter():
    arr = list(map(int, input().split()))
    arr_keg = []
    e = 0
    arr_dist = []
    for i in range(arr[0]):
        arr_keg.append('I')
    while e < arr[1]:
        arr_dist += list(map(int, input().split()))
        e += 1
    for m in range(0, len(arr_dist) - 1, 2):
        for s in range(arr_dist[m] - 1, arr_dist[m + 1]):
            arr_keg[s] = '.'
    print(*arr_keg, end='', sep='')


newprinter()
