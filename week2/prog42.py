a = int(input())
b, d = 0, 0
c = a
while a != 0:
    if a == c:
        b += 1
        if b > d:
            d = b
    else:
        c = a
        b = 1
    a = int(input())
print(d)
