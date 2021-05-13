n = int(input())
x = float(input())
coef = 0.0
res = 0.0
while n >= 0:
    coef = float(input())
    res *= x
    res += coef
    n -= 1
print(res)
