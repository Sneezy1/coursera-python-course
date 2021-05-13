a = int(input())
b = int(input())
c = int(input())
d = int(input())

def min4(a, b, c, d):
    x1 = min(a, b)
    x2 = min(c, d)
    res = min(x1, x2)
    return res


print(min4(a, b, c, d))

def min4(a, b, c, d):
    return min(min(a, b), min(c, d))
print(min4(input(), input(), input(), input()))
