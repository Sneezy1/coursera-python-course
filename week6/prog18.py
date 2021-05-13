fin = open('input.txt', 'r', encoding='utf-8')
dev = []
des = []
odi = []
for line in fin:
    now = list(map(str, line.split()))
    now[2] = int(now[2])
    now[3] = int(now[3])
    if now[2] == 9:
        dev.append(now[3])
    elif now[2] == 10:
        des.append(now[3])
    elif now[2] == 11:
        odi.append(now[3])
fin.close()
dev.sort(key=lambda p: -p)
des.sort(key=lambda p: -p)
odi.sort(key=lambda p: -p)
for i in range(len(dev)):
    if dev[i] > dev[i + 1]:
        print(dev[i + 1], end=' ')
        break
for i in range(len(des)):
    if des[i] > des[i + 1]:
        print(des[i + 1], end=' ')
        break
for i in range(len(odi)):
    if odi[i] > odi[i + 1]:
        print(odi[i + 1])
        break
