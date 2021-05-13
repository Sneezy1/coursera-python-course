def maxmult():
    arr = list(map(int, input().split()))
    maxv = max(arr)
    arr.remove(maxv)
    maxz = max(arr)
    minx = min(arr)
    arr.remove(minx)
    miny = min(arr)
    if maxv * maxz > minx * miny:
        print(maxz, maxv)
    else:
        print(minx, miny)


maxmult()
