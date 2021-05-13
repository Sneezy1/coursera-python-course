a = [1, 2, 3]
b = a[:]
a[0] = 3
print(a, b)

def replace(fList):
    fList = fList[::-1]


a = [1, 2, 3]
replace(a)
print(a)


a = [1, 2]
b = a
a = [3, 4]
print(b)
