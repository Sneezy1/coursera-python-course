def null_counter(n):
    null_c = 0
    for i in range(n):
        x = int(input())
        if x == 0:
            null_c += 1
    return null_c


e = int(input())
print(null_counter(e))
