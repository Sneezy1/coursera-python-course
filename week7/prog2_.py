fin = open('input.txt', 'r', encoding='utf-8')
mydict = dict()
for line in fin:
    now = line.split()
    if now[0] in mydict:
        mydict[now[0]][now[1]] = mydict[now[0]].get(now[1], 0) + int(now[2])
    else:
        mydict[now[0]] = {}
        mydict[now[0]][now[1]] = int(now[2])
for entry in sorted(mydict):
    print(entry, ':', sep='')
    for entry2 in sorted(mydict[entry]):
        print(entry2, mydict[entry][entry2])
