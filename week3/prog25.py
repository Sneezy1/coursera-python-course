str = input()
i = 0
max = len(str)
str_new = str
while i < max:
    cur = str[i]
    if i % 3 == 0:
        str_new = str_new.replace(cur, '', 1)
    i += 1
print(str_new)
