def printer():
    nums_list = list(map(int, input().split()))
    min_el = 0
    for i in range(len(nums_list)):
        if nums_list[i] % 2 == 1:
            min_el_new = nums_list[i]
            if min_el != 0 and min_el_new < min_el:
                min_el = min_el_new
            if min_el == 0:
                min_el = min_el_new
    print(min_el)


printer()
