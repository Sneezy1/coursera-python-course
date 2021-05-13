number = int(input())
counter = number
i = 0
while number != 0:
    if number % 2 == 0:
        i += 1
    number = int(input())
print(i)
