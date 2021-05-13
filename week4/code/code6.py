def f():
    print(a)
    if False:
        a = 1

a = 0
f()
print(a)
