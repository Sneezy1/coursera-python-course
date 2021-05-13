fin = open('input.txt', 'r', encoding='utf-8')
arr = fin.read().split()
fin.close()
textdict = dict()
counter = [0] * len(arr)
for j in range(len(arr)):
    if arr[j] in textdict:
        textdict[arr[j]] += 1
        counter[j] = textdict[arr[j]]
    else:
        textdict[arr[j]] = 0
        counter[j] = 0
print(*counter)
