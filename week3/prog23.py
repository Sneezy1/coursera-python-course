str = input()
x = str.find('h')
y = str.rfind('h')
str1 = str[x + 1:y]
new_str = str1.replace('h', 'H')
print(str[:x + 1] + new_str + str[y:])
