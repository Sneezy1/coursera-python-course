number = int(input())
imax = 1
imin = 1
a1 = number
counter = 1
while number != 0:
    if number == a1:
        imin = 1
        imax = 1
    if number > a1:
        imin = 1
        imax += 1
        a1 = number
        number = int(input())
        if counter < imax:
            counter = imax
    elif number < a1:
        imax = 1
        imin += 1
        a1 = number
        number = int(input())
        if counter < imin:
            counter = imin
    else:
        number = int(input())
print(counter)
