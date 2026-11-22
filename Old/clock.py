def getVals(h, m, s):
    hVal = (30.0 * h) + (0.5 * m) + ((1/120) * s)
    mVal = (6.0 * m) + ((0.1) * s)
    sVal = (6.0 * s)

    return hVal, mVal, sVal

def getDistances(h, m, s):
    a=  abs(h - m)
    b = abs(h - s)
    c = abs(m - s)
    return min(a, 360 - a), min(b, 360 - b), min(c, 360 - c)

hours = [x for x in range(24)]
minutes = [x for x in range(60)]
seconds = [x for x in range(60)]

def checkSequence(x, y, z):
    if x == y or y == z or x == z:
        return False

    if y - x == z - y:
        return True

    return False

distances = []


for x in hours:
    for y in minutes:
        for z in seconds:
            if checkSequence(x, y, z):

                vals = getVals(x%12, y, z)
                distance = getDistances(vals[0], vals[1], vals[2])
                distances.append(sum(distance))

print(min(distances))
