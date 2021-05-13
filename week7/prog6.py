fs = open('input6.txt', 'r', encoding='utf-8')
maxnum = int(fs.readline())
arr = list(fs.readlines())
dupa = set(range(1, maxnum + 1))
for i in range(len(arr)):
    arr[i] = arr[i][:-1]
fs.close()
for j in range(0, len(arr) - 2, 2):
    cur = list(arr[j].split())
    if arr[j + 1] == 'YES':
        tmp = set(map(int, cur))
        dupa &= tmp
    elif arr[j + 1] == 'NO':
        tmp = set(map(int, cur))
        dupa -= tmp
    elif arr[j] == 'HELP':
        break
print(*sorted(dupa), end='')
