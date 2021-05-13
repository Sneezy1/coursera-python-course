myset = {1, 3.14, (2, 3), 'abc', frozenset((2, 3, 4, 5))}
print(*myset)
print(frozenset(myset))
setset = {1, 5, 3, 4, 7, 8, 9}
print(*setset) #sorted
print(sorted(list(setset)))
mysettt = set('abdcawdawd')
print(len(mysettt))


setFromList = set([1, 2, 3])
print(setFromList)
setFromTuple = set((4, 5, 6))
print(setFromTuple)
setFromStr = set("lol")
print(setFromStr)
setFromRange = set(range(2, 22, 3))
print(setFromRange)
setFromMap = set(map(abs, (1, 2, 3, -2, -4)))
print(setFromMap)
setFromSet = set({1, 2, 3})
print(setFromSet)


mySet = {'abba', 'a', 'long string'}
print(', '.join(mySet))
print(', '.join(sorted(mySet)))


firstSet = {1, 2, 1, 3}
secondSet = {3, 2, 1}
print(firstSet == secondSet)
