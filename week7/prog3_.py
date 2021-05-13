fin = open('input.txt', 'r', encoding='utf-8')
clients = dict()
for line in fin:
    now = line.split()
    if now[0] == 'DEPOSIT':
        clients[now[1]] = clients.get(now[1], 0) + int(now[2])
    elif now[0] == 'WITHDRAW':
        clients[now[1]] = clients.get(now[1], 0) - int(now[2])
    elif now[0] == 'BALANCE':
        if now[1] not in clients:
            print('ERROR')
        else:
            print(clients[now[1]])
    elif now[0] == 'TRANSFER':
        clients[now[1]] = clients.get(now[1], 0) - int(now[3])
        clients[now[2]] = clients.get(now[2], 0) + int(now[3])
    elif now[0] == 'INCOME':
        for cli in clients:
            perc = int(now[1]) / 100 + 1
            if clients[cli] > 0:
                clients[cli] = int(clients[cli] * perc)
fin.close()
