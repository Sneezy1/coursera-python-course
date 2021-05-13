a = int(input())
b = int(input())
c = int(input())
d = int(input())
if b != 0 and a == 0:
    print(0)
elif a == 0 and b == 0:
    print('INF')
elif c * -b / a + d != 0 and -b / a % 1 == 0:
    print(-b // a)
else:
    print('NO')
