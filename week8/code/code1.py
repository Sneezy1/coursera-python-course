import itertools
print(*itertools.combinations([1, 2, 3], 2))
print(*itertools.permutations([1, 2, 3]))
print(*itertools.permutations([1, 2, 3], 2))
print(*itertools.combinations_with_replacement([1, 2, 3], 2))