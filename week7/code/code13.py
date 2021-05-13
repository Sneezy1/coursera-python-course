fin = open('input11.txt', 'r', encoding='utf-8')
myDict = dict()
for line in fin:
    eng, latins = line.split('-')
    latinsList = latins.split(',')
    eng = eng.strip()
    for latin in latinsList:
        if latin.strip() not in myDict:
            myDict[latin.strip()] = []
        myDict[latin.strip()].append(eng)
for latin in sorted(myDict):
    print(latin, '-', ', '.join(sorted(myDict[latin])))
