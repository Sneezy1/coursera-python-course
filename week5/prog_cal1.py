n = int(input())
mylist = list(map(int, input().split()))
x = int(input())
number = 1001
difference = 10000
for i in range(len(mylist)):
    if abs(mylist[i] - x) < difference:
        number = mylist[i]
        difference = abs(mylist[i] - x)
print(number)
