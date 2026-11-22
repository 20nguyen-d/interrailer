import math
def distance(a,b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

def heron(a,b,c):
    s = (a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))


a = [[2, 50], [-2, 14]]
b = [[3/4, 21], [-3/4, 15]]
c = [[2/3, 56/3], [-2/3, -8/3]]