fin = open('input.txt', 'r', encoding='utf8')
a = int(fin.readline())
b = int(fin.readline())
print(a + b)

lines = fin.readlines()
print([lines[0].strip(), lines[1].strip()])
