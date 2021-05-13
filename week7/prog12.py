A = []
for i in range(4):
    l = input()
    A.append(''.join([s for s in l if s.isdigit()]))
    A[i] = A[i][1:] if len(A[i]) == 11 else '495' + A[i]
    if i != 0:
        print('YES') if A[0] == A[i] else print('NO')
