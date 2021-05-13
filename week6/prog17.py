fin = open('input.txt', 'r', encoding='utf-8')
schools = [0] * 100
for line in fin:
    new = list(line.split())
    arr = new[2:]
    res = list(map(int, arr))
    schools[res[0]] += 1
fin.close()
for i in range(100):
    if schools[i] == max(schools):
        print(i, end=' ')
