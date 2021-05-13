def mult3():
    arr = list(map(int, input().split()))
    arrnew = arr.copy()
    max1 = max(arr)
    arr.remove(max1)

    max2 = max(arr)
    arr.remove(max2)

    max3 = max(arr)

    min1 = min(arrnew)
    arrnew.remove(min1)

    min2 = min(arrnew)

    first = max1 * max2 * max3
    sec = max1 * min2 * min1

    if first > sec:
        print(max3, max2, max1)
    else:
        print(max1, min2, min1)


mult3()
