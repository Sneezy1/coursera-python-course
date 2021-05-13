str = 'abcd abc abd'
print(str.find('abc'))
print(str.find('abd'))
print(str.find('abe'))
pos = 0
while(str.find('abc', pos)) != -1:
    print(str.find('abc', pos))
    pos = str.find('abc', pos) + 1
