number = int(input())
i = 1
res = 0
while i <= number:
    res += (1 / (i ** 2))
    i += 1
print(res)
