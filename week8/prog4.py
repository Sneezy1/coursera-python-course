import sys
print(not all(filter(lambda x: x == 0, list(map(int, sys.stdin.read().split())))))
