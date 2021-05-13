ls = ['abcd', 'bc', '1234']
ls.sort(key=len)
print(ls)
points = [(1, 1),
          (10, 1),
          (5, 5)]


def sqrDist(point):
    return point[0] ** 2 + point[1] ** 2


points.sort(key=sqrDist)
print(*points)
