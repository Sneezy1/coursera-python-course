a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())


r1 = (a // d) * (b // e) * (c // f)
r2 = (a // d) * (b // f) * (c // e)
r3 = (a // e) * (b // d) * (c // f)
r4 = (a // e) * (b // f) * (c // d)
r5 = (a // f) * (b // d) * (c // e)
r6 = (a // f) * (b // e) * (c // d)

maxR = r1
if maxR < r2:
    maxR = r2
if maxR < r3:
    maxR = r3
if maxR < r4:
    maxR = r4
if maxR < r5:
    maxR = r5
if maxR < r6:
    maxR = r6
print(maxR)
