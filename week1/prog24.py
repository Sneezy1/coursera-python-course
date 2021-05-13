a = int(input())
b = int(input())
res = a % b
print('YES' * (0 ** res), 'NO' * 0 ** (0 ** res), sep='')

s = a % b
x = ((s - 1) // (s + 1)) + 1
c = str('NO' * x) + str('YES' * (1 - x))
print(c)
