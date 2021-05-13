first = int(input())
second = int(input())
res1 = 0 ** (first // second)
res2 = 0 ** (second // (first + 1))
print(first * (0 ** res1) + second * (0 ** res2))

res3 = first // second
res4 = second // first
new = (res3 * first) + (res4 * second)
print(new // (res3 + res4))

