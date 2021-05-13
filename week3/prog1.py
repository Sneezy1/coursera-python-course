a = float(input())
b = float(input())
c = float(input())
polu_per = (a + b + c) / 2
s = (polu_per * (polu_per - a) * (polu_per - b) * (polu_per - c)) ** 0.5
print(s)
