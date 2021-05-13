from math import sqrt


def IsPrime(n):
    sq = sqrt(n)
    i = 2
    while i <= sq:
        if n % i == 0:
            return 'NO'
        i += 1
    return 'YES'


print(IsPrime(int(input())))
