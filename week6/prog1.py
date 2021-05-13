def merge(A, B):
    lena = len(A)
    lenb = len(B)
    i = 0
    j = 0
    C = []
    while i < lena and j < lenb:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    C += A[i:lena] + B[j:lenb]
    print(*C)


A = list(map(int, input().split()))
B = list(map(int, input().split()))
merge(A, B)
