perc = float(input())
rub = float(input())
cop = float(input())
full = rub * 100 + cop
perc_full = full * (perc / 100) + full
print(int(perc_full // 100), int(perc_full % 100))
