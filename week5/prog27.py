def insert_el():
    arr = list(map(int, input().split()))
    rules = list(map(int, input().split()))
    arr.insert(rules[0], rules[1])
    print(*arr)


insert_el()
