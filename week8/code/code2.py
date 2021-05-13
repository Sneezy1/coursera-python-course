import functools
import itertools
prints = functools.partial(print, end=' ')
prints(1)
prints(2)
print(functools.reduce(lambda x, y: x + y, [1, 2, 3]))
print(*itertools.accumulate([1, 4, 3, 5], max))