mySet = {1, 2, 3, 4000000}
for elem in mySet:
    print(elem)


primes = {2, 3, 5, 7, 11, 13}
n = int(input())
if n in primes:
    print('in set')
else:
    print('not in set')


if n not in primes:
    print('not in set')
else:
    print('in set')

primes.add(17)
print(primes)
primes.remove(2)
primes.discard(99)
print(primes)
