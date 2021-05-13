percent = float(input())
rub = float(input())
cop = float(input())
years = float(input())
full_sum = rub * 100 + cop
result = full_sum
while years > 0:
    result = (result * (percent / 100) + result) // 1
    years -= 1
print(int(result // 100), int(result % 100))
