str = input()
i = str.find(' ')
print(str[i + 1:] + ' ' + str[:i])
