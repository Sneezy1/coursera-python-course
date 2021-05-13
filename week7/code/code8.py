s = input()
letters = dict()
for c in s:
    if c not in letters:
        letters[c] = 0
    letters[c] += 1
for c in sorted(letters):
    print(c, letters[c])



s = input()
letters = dict()
for c in s:
        letters[c] = letters.get(c, 0) + 1
for c in sorted(letters):
    print(c, letters[c])
