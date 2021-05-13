numb = int(input())
x1 = numb % 3
x2 = numb % 5
if x1 == 0 or x2 == 0:
    print('YES')
elif numb >= 8:
    print('YES')
else:
    print('NO')
