fs = open('input.txt', 'r', encoding='utf-8')
amount = list(map(int, fs.readline().split()))
arr = list(map(int, fs.readlines()))
fs.close()
set1 = set()
set2 = set()
for i in range(amount[0]):
    set1.add(arr[i])
for j in range(amount[0], amount[0] + amount[1]):
    set2.add(arr[j])
setf1 = set1 & set2
dif1 = sorted(set1.difference(set2))
dif2 = sorted(set2.difference(set1))
sorted(set1)
sorted(set2)
print(len(setf1))
print(*sorted(setf1))
print(len(dif1))
print(*dif1)
print(len(dif2))
print(*dif2)


inFile = open('input.txt', 'r', encoding='utf8')
nm = list(map(int, inFile.readline().split()))
Anya = {int(inFile.readline().strip()) for i in range(nm[0])}
Boris = {int(inFile.readline().strip()) for i in range(nm[1])}
print(len(Anya & Boris))
print(*sorted(Anya & Boris))
print(len(Anya - Boris))
print(*sorted(Anya - Boris))
print(len(Boris - Anya))
print(*sorted(Boris - Anya))
