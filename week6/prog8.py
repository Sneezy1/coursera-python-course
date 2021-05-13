curline = []
fin = open('input.txt', 'r', encoding='utf-8')
dev = []
des = []
odi = []

for line in fin:
    now = line.split()
    curline.append(now)

fin.close()
for i in curline:
    if int(i[2]) == 9:
        dev.append(int(i[3]))
    elif int(i[2]) == 10:
        des.append(int(i[3]))
    elif int(i[2]) == 11:
        odi.append(int(i[3]))

print(sum(dev) / len(dev), sum(des) / len(des), sum(odi) / len(odi))
