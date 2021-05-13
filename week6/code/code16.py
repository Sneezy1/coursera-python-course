mylist = list(map(int, input().split()))
grades = [0] * 11
for now in mylist:
    grades[now] += 1
for grade in range(len(grades)):
    #for i in range(grades[grade]):
        #print(grade, end=' ')
    print((str(grade) + ' ') * grades[grade], end='')
