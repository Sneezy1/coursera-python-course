def lost_cards(n):
    allc = 0
    curr = 0
    for i in range(1, n):
        allc += i
        x = int(input())
        curr += x
    allc += n
    last = allc - curr
    print(last)


e = int(input())
lost_cards(e)
