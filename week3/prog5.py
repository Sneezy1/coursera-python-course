number = float(input())
drob = number - (number // 1)
if drob >= 0.5:
    print(int(number // 1 + 1))
else:
    print(int(number // 1))
