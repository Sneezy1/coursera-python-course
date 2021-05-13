def printer():
    list_nums = list(map(int, input().split()))
    for i in list_nums:
        if i % 2 == 0:
            print(i, end=' ')


printer()
