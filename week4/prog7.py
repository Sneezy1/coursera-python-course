def IsPointInArea(x, y):
    lines1 = y >= -x and (y >= 2 * x + 2)
    lines2 = (y <= -x) and (y <= 2 * x + 2)
    circle1 = (x + 1) ** 2 + (y - 1) ** 2 <= 4
    circle2 = ((x + 1) ** 2 + (y - 1) ** 2) >= 4

    return (lines1 and circle1) or (lines2 and circle2)


def WantToKnow():
    x = float(input())
    y = float(input())
    if IsPointInArea(x, y):
        return 'YES'
    return 'NO'


print(WantToKnow())
