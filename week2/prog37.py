number = int(input())
fibo = 0
first = 0
sec = 1
i = 0
while i != number:
    fibo = first + sec
    sec = first
    first = fibo
    i += 1
print(fibo)
