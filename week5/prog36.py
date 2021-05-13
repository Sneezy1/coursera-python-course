def samepairs():
    arr = list(map(int, input().split()))
    count = 0
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            print(i, j + i)
            if arr[i] == arr[j + i]:
                count += 1
    print(count)


samepairs()
