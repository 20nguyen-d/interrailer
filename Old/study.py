class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def _printName(self):
        print(self.name)

    def printMe(self):
        self._printName()

class Animal(Person):
    def __init__(self, species, size, name="Echo", age="1"):
        super(Animal, self).__init__(name, age)
        self.species = species
        self.size = size

    def whoAmI(self):
        print("I am a {} and I am {}".format(self.species, self.size))
        self.printMe()

    def getSpecies(self):
        return self.species

    def getSize(self):
        return self.size

a = Animal('dog', 'medium')
b = Animal('cat', 'big')
c = Animal('tiger', 'small', name="BoEcho")
d = Animal('tiger', 'big')

animals = [a, b, c, d]

diepAnh = Person("Diep Anh", 13)
lamVy = Person("Lam Vy", 8)

class People(object):
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def getHeight(self):
        return self.height
    def getAll(self):
        return 'name is {}, height is {}, weight is {}'.format(self.name, self.height, self.weight)

    def getBMI(self):
        return self.weight / (self.height * self.height)
e = People('a', 5, 4)
f = People('b', 3, 7)
g = People('c', 6, 2)
people = [e, f, g]

mx = 0
p = None
mn = 10
q = None
for x in people:
    if x.getBMI() > mx:
        mx = x.getBMI()
        p = x
    if x.getBMI() < mn:
        mn = x.getBMI()
        q = x



inpVal = "A,Echo,Dog;P,DiepAnh,40,1.50;A,Boo,Cat;P,LamVy,25,1.52;A,Boo,Dog"
inps = inpVal.split(';')
animalList = []
peopleList = []
for x in inps:
    y = x.split(',')
    if y[0] == 'A':
        animalList.append(Animal(y[1], y[2]))
    if y[0] == 'P':
        peopleList.append(People(y[1], int(y[2]), float(y[3])))

maxHeight = 0
tallest = None
for x in animalList:
    print(x.whoAmI())

for x in peopleList:
    print(x.getAll())
    if x.getHeight() > maxHeight:
        maxHeight = x.getHeight()
        tallest = x.getName()

print('there are {} animals, and {} people '.format(len(animalList), len(peopleList)))
print('tallest is {}, at {}'.format(tallest, maxHeight))



class Node(object):
    mx = 0

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printTree(self):
        if self.left is not None:
            self.left.printTree()

        if self.right is not None:
            self.right.printTree()

        if self.val is not None:
            print(self.val)

    def checkForVal(self, value):
        check = False
        if self.left is not None:
            if self.left.checkForVal(value):
                return True

        if self.right is not None:
            if self.right.checkForVal(value):
                return True

        if self.val is not None:
            if int(self.val) == value:
                check = True
        return check

    def toList(self, vals):
        if self.left is not None:
            self.left.toList(vals)

        if self.right is not None:
            self.right.toList(vals)

        if self.val is not None:
            vals.append(self.val)

    def isInOrder(self):
        check = True
        if self.left is not None:
            if self.left.val > self.val:
                check = False
            self.left.isInOrder()

    def postOrder(self):
        if self.left is not None:
            self.left.postOrder()
        print(self.val)
        if self.right is not None:
            self.right.postOrder()

    def postOrderList(self, vals):
        if self.left is not None:
            self.left.postOrderList(vals)
        vals.append(self.val)
        if self.right is not None:
            self.right.postOrderList(vals)

    def maxCount(self,level, nodes):
        if self.left is not None:

            self.left.maxCount(level + 1, nodes)

        if self.right is not None:

            self.right.maxCount(level + 1, nodes)

        if level > Node.mx:
            Node.mx = level

        print(level, self.val, Node.mx )
        return Node.mx




    def getPaths(self):
        if self.left is not None:
            self.left.getPaths()

        if self.right is not None:
            self.right.getPaths()

        if self.val is not None:
            print(self.val)




    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)

    def findDepth(self, level, vals):
        if self.left is not None:
            self.left.findDepth(level + 1, vals)
        vals.append(level)
        if self.right is not None:
            self.right.findDepth(level + 1, vals)

    def findPath(self, previousPath, vals):
        if self.left is not None:
            self.left.findPath(previousPath + [self.val], vals)
        vals.append(previousPath + [self.val])
        if self.right is not None:
            self.right.findPath(previousPath + [self.val], vals)


    def find(self, value):
        check = False
        if self.left is not None:
            check = self.left.find(value)

        check = check or (self.val == value)


        if self.right is not None:
            check = check or self.right.find(value)

        return check




root = Node(8, Node(5, Node(55, Node(4)), Node(7)), Node(11, Node(9, Node(10)), Node(14)))
a = Node(1, Node(2), Node(3))
vals = []
root.findPath([], vals)

values = []
maxV = max([len(x) for x in vals])
for x in vals:
    if len(x) == maxV:
        values.extend([y for y in x])

print(set(values))
for x in range(len(set(values))):
    print('Node: {}    level = {}'.format(values[x], x + 1))

print(vals)


def decreaseCount(letter):
    counts[letter] -= 1
    if counts[letter] == 0:
        del counts[letter]


def addLetter(letter):
    self.st += letter
    decreaseCount(letter)
    print(self.st)


alphabet = [chr(x) for x in range(97, 123)]
counts = {}
for x in s:
    counts[x] = 1 if x not in counts else counts[x] + 1
print(counts)
print(counts.keys())
print(min(counts.keys()))
self.st = ''
letter = min(counts.keys())

addLetter(letter)
print(self.st)

while True:
    maxLetter2 = None
    for x in alphabet:
        if x > letter and x in counts and counts[x] > 0:
            maxLetter2 = x

            break

    if maxLetter2 is None:
        break
    letter = maxLetter2
    print(maxLetter2)
    addLetter(maxLetter2)

letter2 = max(counts.keys())
addLetter(letter2)
print(self.st)

while True:
    minLetter2 = None
    for x in alphabet:
        if x < letter2 and x in counts and counts[x] > 0:
            minLetter2 = x

            break

    if minLetter2 is None:
        break
    letter2 = minLetter2
    print(minLetter2)
    addLetter(minLetter2)


































