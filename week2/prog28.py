x1 = int(input())
x2 = int(input())
x3 = int(input())
y1 = int(input())
y2 = int(input())
y3 = int(input())

if x1 > x2:
    x1, x2 = x2, x1
if x2 > x3:
    x2, x3 = x3, x2
if x1 > x2:
    x1, x2 = x2, x1
if y1 > y2:
    y1, y2 = y2, y1
if y2 > y3:
    y2, y3 = y3, y2
if y1 > y2:
    y1, y2 = y2, y1

if x1 == y1 and x2 == y2 and x3 == y3:
    print('Boxes are equal')
elif x1 <= y1 and x2 <= y2 and x3 <= y3:
    print('The first box is smaller than the second one')
elif y1 <= x1 and y2 <= x2 and y3 <= x3:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
