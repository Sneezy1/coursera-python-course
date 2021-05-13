def printer():
    listofnums = list(map(int, input().split()))
    maxEl = 0
    maxpos = 0
    for i in range(len(listofnums)):
        if listofnums[i] >= maxEl:
            maxEl = listofnums[i]
            maxpos = i
    print(maxEl, maxpos)


printer()
