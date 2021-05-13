a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
det = a * d - c * b

det1 = e * d - f * b
det2 = a * f - c * e
x1 = det1 / det
x2 = det2 / det
print(x1, x2)
