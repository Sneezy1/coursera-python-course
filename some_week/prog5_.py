familytree = dict()


def getparent(child):
    if not len(familytree[child]):
        return 0
    return 1 + getparent(familytree[child])


fin = open('input.txt', 'r', encoding='utf-8')
num = int(fin.readline())
for line in fin:
    now = line.strip().split()
    familytree[now[0]] = now[1]
    familytree[now[1]] = familytree.get(now[1], '')
fin.close()
for child in sorted(familytree):
    print(child, getparent(child))
