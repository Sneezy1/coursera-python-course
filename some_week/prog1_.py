fin = open('input.txt', 'r', encoding='utf-8')
dictofparties = {}
votesall = 0
for line in fin:
    now = line.split()
    name = ' '.join(now[:-1])
    dictofparties[name] = dictofparties.get(name, 0) + int(now[-1])
    votesall += int(now[-1])
fin.close()
seats = 450
fich = votesall / seats
ost = {}
for key, val in dictofparties.items():
    ost[key] = val % fich
    dictofparties[key] = int(val / fich)
    seats -= dictofparties[key]
ost = dict(sorted(ost.items(), key=lambda item: -item[1]))
for key, val in ost.items():
    if seats:
        dictofparties[key] += 1
        seats -= 1
for key in dictofparties:
    print(key, dictofparties[key])
