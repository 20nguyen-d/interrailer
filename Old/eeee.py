cog1 = [267, 851, 259, 433, 493, 165, 701, 102]
cog2 = [914, 494, 468, 460, 143, 150, 832, 580, 299, 334, 408]
cog3 = [296, 763, 155, 145, 168, 437, 733, 154, 141]
import math

def spinCog(n, cog):

   return cog[n%len(cog)]


def hcf(x, y):
  while y:
      x, y = y, x % y
  return x


def checkPy(a, b, c):
    a, b, c = sorted([a, b, c])

    if a*a + b*b != c*c:
        return False

    return math.gcd(a, math.gcd(b, c)) == 1


for x in cog1:
    for y in cog2:
        for z in cog3:
            if checkPy(x, y, z) and x!= y and y!= z and z != x:
                print([x,y,z])



def check60(a, b, c):
    return a**2 + b**2 - c**2 == a*b or a**2 + c**2 - b**2 == a*c or b**2 + c**2 - a**2 == b*c


def checkSquare(n):
    r = int(math.isqrt(n))
    return r * r == n

def checktri(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False

    s2 = a + b + c
    q = s2 * (s2 - 2*a) * (s2 - 2*b) * (s2 - 2*c)

    return q > 0 and checkSquare(q)



nine = ['102334155','165580141','267914296','433494437','701408733'] #9-digit fibonacci numbers
def checkFib(a,b,c):
    d = str(a) + str(b) + str(c)
    return d in nine



def getCogs(x, y, z):
    v1 = cog1.index(x)
    v2 = cog2.index(y)
    v3 = cog3.index(z)
    c1 = [cog1[v1]] + cog1[v1+1:] + cog1[:v1]
    c2 = [cog2[v2]] + cog2[v2+1:] + cog2[:v2]
    c3 = [cog3[v3]] + cog3[v3+1:] + cog3[:v3]

    return c1, c2, c3




def getDist(c1, c2, c3, x, y, z):
    a = 0
    b = 0
    c =0
    for q in range(10000):
        a = spinCog(q, c1)
        b = spinCog(q, c2)
        c = spinCog(q, c3)

        if [a,b,c] == [x,y,z]:
            return q
    return 0

def distance(a,b):
    cogs = getCogs(a[0], a[1], a[2])
    return getDist(cogs[0], cogs[1], cogs[2], b[0], b[1], b[2])


sixty = [[259, 299, 155], [165, 832, 763]]
py = [[493, 468, 155], [433, 408, 145]]
tri = [[433, 408, 145],[851, 460, 437], [493, 468, 155], [165, 143, 154], [102, 150, 168]]
fib = [[102,334,155], [165,580,141], [267,914,296], [433,494,437], [701,408,733]]


prods = []
vals = []
pqrs = []

for q in fib:
    for w in py:
        for e in sixty:
            for r in tri:
                for t in fib:
                    pqrs.append([q,w,e,r,t])
                    d1 = distance(q, w)
                    d2 = distance(w, e)
                    d3 = distance(e, r)
                    d4 = distance(r, t)

                    prods.append([d1*d2*d3*d4, [d1, d2, d3, d4], [q,w,e,r,t]])
                    vals.append([d1, d2,d3,d4])



print(sorted(prods))
print(884520*16)


def testing():
    dists = []
    for x in range(len(fib)):
        for y in range(len(py)):
            cogs = getCogs(fib[x][0], fib[x][1], fib[x][2])
            dist = getDist(cogs[0], cogs[1], cogs[2], py[y][0], py[y][1], py[y][2])
            dists.append(dist)

    print(dists)
        #[477, 39, 596, 177, 14]

    dists = []
    for x in range(len(py)):
        for y in range(len(sixty)):
            cogs = getCogs(py[x][0], py[x][1], py[x][2])
            dist = getDist(cogs[0], cogs[1], cogs[2], sixty[y][0], sixty[y][1], sixty[y][2])
            dists.append(dist)

    print(dists)#[270, 521]

    dists = []
    for x in range(len(sixty)):
        for y in range(len(tri)):
            cogs = getCogs(sixty[x][0], sixty[x][1], sixty[x][2])
            dist = getDist(cogs[0], cogs[1], cogs[2], tri[y][0], tri[y][1], tri[y][2])
            dists.append(dist)

    print(dists) #[39, 522, 491, 173, 580, 271, 240, 714]

    dists = []
    for x in range(len(tri)):
        for y in range(len(fib)):
            cogs = getCogs(tri[x][0], tri[x][1], tri[x][2])
            dist = getDist(cogs[0], cogs[1], cogs[2], fib[y][0], fib[y][1], fib[y][2])
            dists.append(dist)

    print(dists)  # [6, 444, 679, 306, 469, 315, 753, 196, 615, 778, 346, 784, 227, 646, 17, 664, 310, 545, 172, 335]


