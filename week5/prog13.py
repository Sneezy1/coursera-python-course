def printer():
    list_nums = list(map(int, input().split()))
    for i in range(len(list_nums)):
        if i % 2 == 0:
            print(list_nums[i], end=' ')


printer()
