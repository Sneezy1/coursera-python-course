def myRange(n):
    i = 0
    while i < n:
        yield i ** 2
        i += 1


s = 0
for i in myRange(10):
    print(i)


def genDecDigs(cntDigits, maxDigit):
    if cntDigits > 0:
        for nowDigit in range(maxDigit + 1):
            for tail in genDecDigs(cntDigits - 1, nowDigit):
                yield nowDigit * 10**(cntDigits - 1) + tail
    else:
        yield 0

print(*genDecDigs(2, 3))
