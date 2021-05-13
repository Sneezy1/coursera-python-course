import functools
print(*functools.reduce(lambda x, y: map(lambda a, b: abs(a - b), x, y), map(lambda x: map(int, input().split()), range(int(input())))))
