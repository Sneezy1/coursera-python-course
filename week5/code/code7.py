a = [1, 2, 3, 4, 2, 2, 3]
b = [3, 6, 7, 8, 9]
print(a.count(2))
a.append(22)
print(a)
a.extend(b)
print(a)
c = [5, 6, 7, 8, 9, 7, 10]
c.remove(7)
print(c)
e = c.copy()
print(e)
f = [22, 33, 44, 55, 66, 77]
f.insert(1, 11)
print(f)
f.pop(3)
print(f)
