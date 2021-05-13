def printer():
    listOfNums = list(map(int, input().split()))
    counter = 0
    for i in listOfNums:
        if i > 0:
            counter += 1
    print(counter)


printer()
