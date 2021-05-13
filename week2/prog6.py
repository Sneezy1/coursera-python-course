first = int(input())
second = int(input())
if (second % (second - first + 1)) == 0:
    print('YES')
else:
    print('NO')
