l1, r1, l2 = int(input()), int(input()), int(input())
r2, l3, r3 = int(input()), int(input()), int(input())
nom1 = 1
nom2 = 2
nom3 = 3
if l2 < l1:
    (l1, l2) = (l2, l1)
    (r1, r2) = (r2, r1)
    (nom1, nom2) = (nom2, nom1)
if l3 < l2:
    (l2, l3) = (l3, l2)
    (r2, r3) = (r3, r2)
    (nom2, nom3) = (nom3, nom2)
if l2 < l1:
    (l1, l2) = (l2, l1)
    (r1, r2) = (r2, r1)
    (nom1, nom2) = (nom2, nom1)
d1 = r1 - l1
d2 = r2 - l2
d3 = r3 - l3
c1 = l2 - r1
c2 = l3 - r2
if (l2 <= r1 and l3 <= r2) or r1 >= l3:
    print(0)
elif d1 < c2 and d3 < c1:
    print(-1)
elif (nom1 < nom3 and d1 >= c2 > 0) or (nom1 < nom3 and c2 <= 0 and c1 > 0):
    print(nom1)
elif d3 >= c1 > 0:
    print(nom3)
elif (nom3 < nom1 and d3 >= c1 > 0) or (nom3 < nom1 and c1 <= 0 and c2 > 0):
    print(nom3)
elif (d1 >= c2 > 0) or (c2 <= 0 and d1 >= c1 > 0):
    print(nom1)
