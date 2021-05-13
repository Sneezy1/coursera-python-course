print((1, 1) < (2, 'abc'))
p = [(172, 'Vasya'),
     (180, 'Petya'),
     (180, 'Misha')]
p.sort()
m = sorted(p, reverse=True)
print(*p)
print(*m)
