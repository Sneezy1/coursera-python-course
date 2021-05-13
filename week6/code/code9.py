def printList(lst, mysep=' '):
    for i in range(len(lst) - 1):
        print(lst[i], mysep, sep='', end='')
    print(lst[-1], sep='')


printList([1, 2, 3, 4, 5, 6], mysep='a')
printList([1, 2, 3, 4, 5, 6])


def mysum(*args):
    res = 0
    for i in args:
        res += i
    return res


def mysum2(*args):
    return sum(args)

print(mysum(1, 2, 3, 4))
print(mysum(1))
print(mysum(1, 2, 3))


def mymin(first, *others):
    nowmin = first
    for now in others:
        if now < nowmin:
            nowmin = now
    return nowmin


print(mymin(1))
print(mymin(2, 3, 5, -7, 1, -14))


def printList(myList, sep=' '):
    print(sep.join(map(str, myList)))


printList([1, 2, 3])
printList([3, 2, 1], sep='\n')

