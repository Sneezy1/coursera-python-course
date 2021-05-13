import itertools
print('\n'.join(map(''.join, itertools.permutations(map(str, (list(range(1, int(input()) + 1))))))))
