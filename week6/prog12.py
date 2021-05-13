numofkeys = int(input())
numofpresses = list(map(int, input().split()))
allpress = int(input())
presschain = list(map(int, input().split()))
presscount = [0] * numofkeys
for press in presschain:
    presscount[press - 1] += 1
response = [''] * numofkeys
for i in range(numofkeys):
    if presscount[i] <= numofpresses[i]:
        print('NO')
    else:
        print('YES')
