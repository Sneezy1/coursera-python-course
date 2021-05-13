def reverse():
    number = int(input())
    if number == 0:
        print(0)
    if number != 0:
        reverse()
        print(number)


reverse()
