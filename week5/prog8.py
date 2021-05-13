def double_multiply():
    for i in range(10, 100):
        first = i // 10
        second = i % 10
        if (2 * first * second) == i:
            print(i)


double_multiply()
