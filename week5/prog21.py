def reverse_printer():
    array = list(map(int, input().split()))
    for i in range(-1, -len(array) - 1, -1):
        print(array[i], end=' ')


reverse_printer()
