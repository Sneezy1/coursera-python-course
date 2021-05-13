s = input()
print(s[0:1], s[1:].replace('', '*', len(s) - 1), sep='')


s = input()
g = s[1:-1:1]
if len(s) == 1:
    print(s)
else:
    print(s[0] + g.replace('', '*') + s[-1])
