str = input()
pos = 0
last = 0
res = str.find('f', pos)
first = res
while res != -1:
    pos = str.find('f', pos) + 1
    res = str.find('f', pos)
    if res > last:
        last = res
if first != -1 and last == 0:
    print(first)
elif last != 0 and last > first:
    print(first, last)
