set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
set3 = set1 & set2
print(*sorted(set3))
