dist = int(input())
number = int(input())
res = 1
while dist < number:
    dist = dist * 1.1
    res += 1
print(res)
