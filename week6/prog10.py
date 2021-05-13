users = []
fin = open('input.txt', 'r', encoding='utf-8')
for line in fin:
    now = line.split()
    new = now[:2] + now[3:]
    users.append(new)
fin.close()
users.sort(key=lambda elem: elem[0])
fout = open('output.txt', 'w', encoding='utf-8')
for line in users:
    print(*line, file=fout)
fout.close()
