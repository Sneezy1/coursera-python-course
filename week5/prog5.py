def flags(n):
        print('+___ ' * n, sep=' ')
        for i in range(1, n + 1):
            print('|{0} /'.format(i), end=' ')
        print()
        print('|__\\ ' * n, sep=' ')
        print('|    ' * n, sep=' ')


x = int(input())
flags(x)
