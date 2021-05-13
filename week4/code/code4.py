def sort2(a, b):
    if a < b:
        return a, b
    return b, a


minimum, maximum = sort2(5, 4)
print(minimum, maximum)


def isEven(n):
    return n % 2 == 0


n = int(input())
if isEven(n):
    print('EVEN')
else:
    print('ODD')
