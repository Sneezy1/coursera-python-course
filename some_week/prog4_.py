def lowercount(word):
    counter = 0
    for i in word:
        if i.isupper():
            counter += 1
    return counter
words = set()
fin = open('input.txt', 'r', encoding='utf-8')
dictlen = int(fin.readline())
for _ in range(dictlen):
    words.add(fin.readline().strip())
text = fin.read().split()
fin.close()
lowwords = {s.lower() for s in words}
errors = 0
for word in text:
    if word not in words:
        if word.lower() in lowwords:
            errors += 1
        elif word.islower():
            errors += 1
        elif lowercount(word) != 1:
            errors += 1
print(errors)
