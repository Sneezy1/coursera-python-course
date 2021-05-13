points = [(1, 1),
          (5, 1),
          (2, 1),
          (2, 3),
          (1, 2)]


def sqrDist(point):
    return point[0] ** 2 + point[1] ** 2


kekMda = lambda p: p[0] ** 2 + p[1] ** 2

points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
print(*points)
