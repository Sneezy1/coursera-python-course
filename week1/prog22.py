number = int(input())
first = number // 1000
second = number // 100 % 10
third = number // 10 % 10
fourth = number % 10
print(1 + ((first - fourth) ** 2 + (second - third) ** 2))
