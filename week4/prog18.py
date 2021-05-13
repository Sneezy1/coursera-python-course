def evkl(a, b):
    mod = a % b
    if mod != 0:
        a = b
        b = mod
        evkl(a, b)
    else:
        print(b)


a = int(input())
b = int(input())
evkl(a, b)
