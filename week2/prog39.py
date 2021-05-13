a = int(input())
b = int(input())
while a > b:
    while a % 2 == 0 and a // 2 >= b:
        a /= 2
        print(':2')
    if a > b:
        a -= 1
        print('-1')
