number = int(input())
first = 0
second = 0
while number != 0:
    if number > second:
        second = number
    if second > first:
        first, second = second, first
    number = int(input())
print(second)
