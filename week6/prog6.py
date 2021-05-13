

def old_sorter(c):
    return c[0]


def grob():
    vi = []
    va = []
    res = []
    nv = int(input())
    for i in range(nv):
        res.append(0)
    villdist = list(map(int, input().split()))
    numofvault = int(input())
    vaultdist = list(map(int, input().split()))
    for i in range(nv):
        vi.append((villdist[i], i + 1))
    for j in range(numofvault):
        va.append((vaultdist[j], j + 1))
    vi.sort(key=old_sorter)
    va.sort(key=old_sorter)
    k, m = 0, 0
    while k < nv and m < numofvault - 1:
        if abs(vi[k][0] - va[m][0]) <= abs(vi[k][0] - va[m + 1][0]):
            res[vi[k][1] - 1] = va[m][1]
            k += 1
        else:
            m += 1
        if m == numofvault - 1:
            while k < nv:
                res[vi[k][1] - 1] = va[m][1]
                k += 1
    if numofvault == 1:
        for e in range(nv):
            res[e] = va[0][1]
    print(*res)


grob()
