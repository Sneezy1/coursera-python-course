number = int(input())
c = 1
counter = 0
while c <= number:
    a = c
    b = a % 10
    while a // 10 != 0:
        b = b * 10 + (a // 10 % 10)
        a = a // 10
    if b == c:
        counter += 1
    c += 1
print(counter)
