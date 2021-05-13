a = tuple(map(int, input().split()))
k = []
for i in range(len(a)):
    if i % 2 == 1:
        k += [a[i]]
        k += [a[i - 1]]
if len(a) % 2 == 1:
    k += [a[-1]]
print(*k)
