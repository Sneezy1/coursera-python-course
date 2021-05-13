arr = map(int, input().split())


def CountSort(list):
    nums = [0] * 101
    for i in list:
        nums[i] += 1
    for e in range(101):
        print((str(e) + ' ') * nums[e], end='')


CountSort(arr)
