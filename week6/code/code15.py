li = list(map(int, input().split()))
newlist = []
for i in range(len(li)):
    newlist.append((li[i], i))
newlist.sort()
for now in newlist:
    print(now[1])
