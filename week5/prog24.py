def max_el():
    array = list(map(int, input().split()))
    min_ele = 0
    count = 0
    for i in range(len(array)):
        if min_ele == 0:
            min_ele = array[i]
            count = i
        elif array[i] > min_ele:
            min_ele = array[i]
            count = i
    print(min_ele, count)


max_el()
#s = s[::-1] разворот списка
