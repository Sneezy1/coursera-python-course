def Intersection(A, B):
    lena = len(A)
    lenb = len(B)
    i = 0
    j = 0
    C = []
    while i < lena and j < lenb:
        if A[i] < B[j]:
            i += 1
        elif B[j] < A[i]:
            j += 1
        elif A[i] == B[j]:
            C.append(A[i])
            i += 1
            j += 1
    print(*C)


A = list(map(int, input().split()))
B = list(map(int, input().split()))
Intersection(A, B)
