def ppl_line():
    arr = list(map(int, input().split()))
    height = int(input())
    i = 0
    while i <= len(arr) - 1 and height <= arr[i]:
        i += 1
    print(i + 1)


ppl_line()
