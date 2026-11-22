import math

def getLength(x1, y1, x2, y2):
    a = abs(x1 - x2)
    b = abs(y1 - y2)

    return math.sqrt(a**2 + b**2)


def checkTri(x1, y1, x2, y2, x3, y3):
    lst = [getLength(x1, y1, x2, y2),getLength(x3, y3, x2, y2),getLength(x1, y1, x3, y3)]
    lst = sorted(lst)

    return lst[0] ** 2 + lst[1] ** 2 == lst[2] ** 2

def getArea(x1, y1, x2, y2, x3, y3):
    lst = [getLength(x1, y1, x2, y2), getLength(x3, y3, x2, y2), getLength(x1, y1, x3, y3)]
    lst = sorted(lst)

    return (lst[0] * lst[1]) / 2

def q(x1, y1, x2, y2, x3, y3):
    a = (x2 - x1)*(x3 - x1) + (y2-y1)*(y3-y1)
    b = (x1 - x2)*(x3 - x2) + (y1-y2)*(y3-y2)
    c = (x1 - x3)*(x2 - x3) + (y1-y3)*(y2-y3)

    if a == 0 or b == 0 or c == 0:
        return True

    return False

for y in range(-1000000, 1000000):
    x = y/100000


    if (q(1,3, -2, 4, x, -5)):
        print([x, -5])
        print(getArea(1,3, -2, 4, x, -5))

    if (q(1,3, -2, 4, 3, x)):
        print([3, x])
        print(getArea(1,3, -2, 4, 3, x))

    if (q(x,3, -2, 4, 3, -5)):
        print([x, 3])
        print(getArea(x,3, -2, 4, 3, -5))

    if (q(1,x, -2, 4, 3, -5)):
        print([1, x])
        print(getArea(1,x, -2, 4, 3, -5))

    if (q(1,3, x, 4, 3, -5)):
        print([x, 4])
        print(getArea(1,3, x, 4, 3, -5))

    if (q(1,3, -2, x, 3, -5)):
        print([-2, x])
        print(getArea(1,3, -2, x, 3, -5))

