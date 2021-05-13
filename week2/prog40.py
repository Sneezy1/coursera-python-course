number = int(input())
while number > 0:
    a = number % 10
    print(a, end='')
    number //= 10
