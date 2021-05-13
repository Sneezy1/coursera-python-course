days = list(map(int, input().split()))
zabast = list()
for i in range(days[1]):
    cur = list(map(int, input().split()))
    zabast.append(cur)
holidays = set()
i = 5
while i < days[0]:
    holidays.add(i + 1)
    holidays.add(i + 2)
    i += 7
zabasts = set()
for i in range(len(zabast)):
    for el in range(zabast[i][0], days[0] + 1, zabast[i][1]):
        zabasts.add(el)
print(len(zabasts.difference(holidays)))
