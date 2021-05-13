def same_sign():
    array = list(map(int, input().split()))
    for i in range(1, len(array)):
        if array[i - 1] > 0 and array[i] > 0:
            print(array[i - 1], array[i])
            break
        elif array[i - 1] < 0 and array[i] < 0:
            print(array[i - 1], array[i])
            break


same_sign()
