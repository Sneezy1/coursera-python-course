def greater_than_neighbors():
    array = list(map(int, input().split()))
    count = 0
    for i in range(1, len(array) - 1):
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            count += 1
    print(count)


greater_than_neighbors()
