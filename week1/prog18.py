number = int(input())
min1 = str(number // 60 % 60 // 10)
min2 = str(number // 60 % 60 % 10)
sec1 = str(number % 60 // 10)
sec2 = str(number % 10 % 10)
print(number//3600 % 24, min1 + min2, sec1 + sec2, sep=':')
