str = input()
pos = 0
res = str.find('h', pos)
first = res
second = 0
while res != -1:
    pos = str.find('h', pos) + 1
    res = str.find('h', pos)
    if res != -1:
        second = res
print(str[:first] + str[second + 1:])
