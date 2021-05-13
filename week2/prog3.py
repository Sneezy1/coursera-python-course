x = int(input())
y = int(input())
z = int(input())
if x >= y >= z or x >= z >= y:
    print(x)
elif y >= z >= x or y >= x >= z:
    print(y)
elif z >= x >= y or z >= y >= x:
    print(z)
else:
    print(x)
