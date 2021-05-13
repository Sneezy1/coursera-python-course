from math import sqrt


def MinDivisor(n):
    i = 2
    sq = n ** 0.5
    while n % i != 0:
        if i >= sq:
            return n
        i += 1
    return i


print(MinDivisor(int(input())))
