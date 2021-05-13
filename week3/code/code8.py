str = 'aaaaaa'
while str.find('aa') != -1:
    str = str.replace('aa','a', 1)
print(str)
