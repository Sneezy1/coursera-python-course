fin = open('input.txt', 'r', encoding='utf-8')
arr = []
for line in fin:
    arr.append(line[:-1:1])
parties = []
fin.close()
i = 1
breaker = 0
while i != len(arr):
    if arr[i] == 'VOTES:':
        breaker = i
        break
    else:
        parties.append(arr[i])
        i += 1
votes = arr[breaker + 1:]
res = []
yesno = []
for i in range(len(parties)):
    yesno.append((votes.count(parties[i]) / len(votes)) * 100)
    if yesno[i] >= 7:
        print(parties[i])
