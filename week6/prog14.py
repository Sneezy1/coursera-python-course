numofppl = int(input())
arr = []
for i in range(numofppl):
    new = input().split()
    arr.append((new[0], int(new[1])))

arr.sort(key=lambda p: -p[1])
for j in range(numofppl):
    print(arr[j][0])
