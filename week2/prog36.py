number = int(input())
max_element = number
i = 0
while number != 0:
    if number > max_element:
        max_element = number
        i = 0
    if number == max_element:
        i += 1
    number = int(input())
print(i)
