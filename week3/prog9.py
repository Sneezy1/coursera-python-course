from math import sqrt
number = int(input())
counter = 0
sum = 0
res = 0
sq_sum = 0
while number != 0:
    sq_sum += number ** 2
    sum += number
    res = res + (-2 * number)
    counter += 1
    number = int(input())

av_sum = sum / counter
# print(av_sum)
# print(counter)
last_res = sqrt((sq_sum + av_sum * (counter * av_sum + res)) / (counter - 1))
print('{:.11f}'.format(last_res))
