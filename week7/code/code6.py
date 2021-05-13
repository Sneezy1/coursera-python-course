capitals = {'Russia': 'Moscow', 'France': 'Paris'}
print(capitals['Russia'])
print(capitals['France'])
capitals['USA'] = 'Washington'
print(capitals['USA'])
del capitals['France']
print(*capitals)
print('France' in capitals)
