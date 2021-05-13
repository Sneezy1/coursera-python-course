from math import sqrt


def squares(i):
    n = int(input())
    sq = sqrt(n) // 1
    if n != 0:
        if sq * sq == n:
            return str(squares(i + 1)) + ' ' + str(n)
        return squares(i)
    if i == 0:
        return 0
    return ''


print(squares(0))
