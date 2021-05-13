fin = open('input.txt', 'r', encoding='utf-8')
vsrt = dict()
for line in fin:
    arr = line.split()
    for el in range(len(arr)):
        vsrt[arr[el]] = vsrt.get(arr[el], 0) + 1
fin.close()
lisss = sorted(vsrt.items())
lisss.sort(key=lambda x: x[1], reverse=True)
for el in range(len(lisss)):
    print(lisss[el][0])
