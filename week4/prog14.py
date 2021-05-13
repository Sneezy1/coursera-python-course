def power(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        a = power(a * a, n / 2)
        return a
    if n % 2 == 1:
        a = a * power(a, n - 1)
        return a


x = float(input())
y = float(input())
print(power(x, y))
