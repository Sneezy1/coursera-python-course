def power(a, n):
    if n == 0:
        return 1
    if n != 0:
        power(a, n - 1)
        return a ** n


e = float(input())
k = float(input())
print(power(e, k))


def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)

a = float(input())
n = int(input())
print(power(a, n))
