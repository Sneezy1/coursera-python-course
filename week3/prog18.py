str = input()
pos = 0
res = str.find('f', pos)
first = res

pos = str.find('f', pos) + 1
res = str.find('f', pos)
second = res

if second == -1 and first != -1:
    print(-1)
elif first == -1:
    print(-2)
elif second != 0 and second != -1:
    print(second)
