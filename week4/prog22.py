

def sev(n, depth):
    if depth == 0:
        return 0
    thir = int(n ** (1/3))
    if thir ** 3 == n:
        return str(thir ** 3)
    while thir > 0:
        if sev(n - thir ** 3, depth - 1) != 0:
            return str(thir ** 3) + ' ' + sev(n - thir ** 3, depth - 1)
        thir -= 1
    return 0


xx = int(input())
print(sev(xx, 7))
