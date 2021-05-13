def nearest():
    arr_size = int(input())
    arr = list(map(int, input().split()))
    num = int(input())
    dif = 1001
    targ = 0
    if arr.count(num) != 0:
        print(num)
    else:
        for i in range(2002):
            if arr.count(num - i) != 0:
                print(num - i)
                break
            elif arr.count(num + i) != 0:
                print(num + i)
                break

nearest()
