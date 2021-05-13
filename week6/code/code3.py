p = [(-172, 'Vasya'),
     (-180, 'Petya'),
     (-172, 'Fedya')]
p.sort()
for i in range(len(p)):
    p[i] = (-p[i][0], p[i][1])
print(*p)
