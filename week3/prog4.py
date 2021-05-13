number = float(input())
full = number
number //= 1
print(round(number), round((full - number) * 100))
