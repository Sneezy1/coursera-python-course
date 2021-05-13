number = int(input())
new = number
counter = 0
while number != 0:
    number = int(input())
    if number > new:
        counter += 1
    new = number
print(counter)
