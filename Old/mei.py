
import math

cog1 = [267, 851, 259, 433, 493, 165, 701, 102]
cog2 = [914, 494, 468, 460, 143, 150, 832, 580, 299, 334, 408]
cog3 = [296, 763, 155, 145,168, 437, 733, 154, 141]


def spinCog(n, cog):

   return cog[n%len(cog)]

def hcf(x, y):
  while y:
      x, y = y, x % y
  return x

nine = ['102334155','165580141','267914296','433494437','701408733'] #9-digit fibonacci numbers

sets = [[102,334,155], [165,580,141], [267,914,296], [433,494,437], [701,408,733]]

def checkPy(a, b, c):
    vals = sorted([a, b, c])
    a = vals[0]
    b = vals[1]
    c = vals[2]
    if hcf(a,b) == 1 and hcf(b,c) == 1 and hcf(a,c) == 1:

        if a**2 + b ** 2 == c ** 2:
            return True
    return False


def check60(a, b, c):
    val1 = (b**2 + c**2 - a**2)/(2*b*c)
    val2 = (a**2 + b**2 - c**2)/(2*a*b)
    val3 = (a**2 + c**2 - b**2)/(2*a*c)

    return val1 == 0.5 or val2 == 0.5 or val3 == 0.5

def checktri(a, b, c): #heron triangle!!

    def old():
        if a + b <= c or a + c <= b or b + c <= a:
            return False
        val = (a + b + c) * (-a + b + c) * (a - b + c) * (a + b - c)
        if val <= 0:
            return False
        k = math.isqrt(val)
        if k * k != val:
            return False
        return k % 4 == 0

    s = (a + b + c) / 2
    q = s * (s - a) * (s - b) * (s - c)
    if q < 0:
        return False

    area = math.sqrt(q)
    return abs(area - round(area)) < 1e-9


def checkFib(a,b,c):
    d = str(a) + str(b) + str(c)
    return d in nine

a = 267
b = 914
c = 296


def goooo(start):
    pcheck = False
    qcheck = False
    rcheck = False
    scheck = False

    for x in range(793):
        a = spinCog(x, cog1)
        b = spinCog(x, cog2)
        c = spinCog(x, cog3)

        if [a, b, c] == start:
           #print('YAEY', x)

            break
    num = x

    total = 0
    #119 to get to first

    for x in range(num, 793*2):
        a = spinCog(x, cog1)
        b = spinCog(x, cog2)
        c = spinCog(x, cog3)

        if checkPy(a,b,c):
            #print('YAY', x)
            pcheck = True
            break

    total += x - num
    p = x-num

    num = x
    for x in range(num, 793*3):
        a = spinCog(x, cog1)
        b = spinCog(x, cog2)
        c = spinCog(x, cog3)

        if check60(a,b,c):
            #print('YAY', x)
            qcheck = True
            break
    total += x - num
    q = x-num
    num = x

    for x in range(num, 793*4):
        a = spinCog(x, cog1)
        b = spinCog(x, cog2)
        c = spinCog(x, cog3)

        if checktri(a,b,c):
            #print('YEY', x)
            rcheck = True
           #print(a, b, c)
            break



    total += x - num
    r = x -num
    num = x

    for x in range(num, 793*5):
        a = spinCog(x, cog1)
        b = spinCog(x, cog2)
        c = spinCog(x, cog3)

        if checkFib(a,b,c):
           #print('YAE', x)
            scheck = True
            break

    total += x - num
    s = x-num


    if pcheck and qcheck and rcheck and scheck:
        print(p,q,r,s)
        return p*q*r*s
    else:
        return -100

lst = []
for y in sets:

        go = goooo(y)
        if go > -100:
            lst.append(go)

print(lst)
print(set(lst))
print(min(lst))
