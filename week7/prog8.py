fs = open('input.txt', 'r', encoding='utf-8')
users = int(fs.readline())
cur_setus = list()
all_sets = list()
last_answer = set()
for i in range(users):
    cur_am = int(fs.readline())
    for j in range(cur_am):
        str = fs.readline()
        last_answer.add(str[:-1])
        cur_setus.append(str[:-1])
    all_sets.append(cur_setus)
    cur_setus = []
fs.close()
for em in range(len(all_sets)):
    all_sets[em] = set(all_sets[em])
res = all_sets[0]
for il in range(1, len(all_sets)):
    res &= all_sets[il]
print(len(res))
for ugumg in res:
    print(ugumg)
print(len(last_answer))
for els in last_answer:
    print(els)
