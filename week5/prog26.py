def remove_el():
    arr = list(map(int, input().split()))
    pos = int(input())
    arr.pop(pos)
    print(*arr)


remove_el()
