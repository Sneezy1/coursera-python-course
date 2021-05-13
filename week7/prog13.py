numofcountries = int(input())
countries = []
mydict = dict()
for i in range(numofcountries):
    now = input().split()
    countries.append(now)
questions = int(input())
for k in range(numofcountries):
    for el in range(1, len(countries[k])):
        keycountry = countries[k][el]
        mydict[keycountry] = countries[k][0]
for fi in range(questions):
    print(mydict[input()])
