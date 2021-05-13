setik = set()
arr = list(map(int, input().split()))
for el in arr:
    if el in setik:
        print('YES')
    else:
        setik.add(el)
        print('NO')
