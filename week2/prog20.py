number = int(input())
i = 1
square = 0
while square < number:
    square = i ** 2
    if square <= number:
        print(square, end=' ')
        i = i + 1
