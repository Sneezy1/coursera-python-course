def summ():
    x = int(input())
    while x != 0:
        return x + summ()


print(summ())
