def diofant():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    counter = 0
    for i in range(1000 + 1):
        if (i - e) != 0:
            if ((a * (i ** 3) + b * (i ** 2) + c * i + d) / (i - e)) == 0:
                counter += 1
    print(counter)


diofant()
