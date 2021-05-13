a = list('abcde')
a[0] = 'f'
print(a)
s = ''.join(a)
print(s)


#wordList = input().split()
#print(wordList)

intList = list(map(int, input().split()))
print(' '.join((map(str, intList))))
print(*intList)
