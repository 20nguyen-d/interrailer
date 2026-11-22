def combi_for():
    lst = [4, 5, 7, 8, 2, 3]
    for x in range(len(lst)):
        for y in range(x + 1, len(lst)):
            for z in range(y + 1, len(lst)):

                print([lst[x], lst[y], lst[z]])

def mult(a):
    if a < 10:
        return a
    else:
        return mult(a - (10 * (a//10)))



def digitSum(num):
    if num < 10:
        return num
    else:
        last = num % 10
        num = (num - last) // 10
        return digitSum(num) + last




b = '10110'

n = 2
count = 0
for x in range(len(b)):

    if b[x] == '1':
        count += n

    n = n * 2



def power2(num):
    if num == 0:
        return 1
    else:
        return power2(num - 1) * 2

def getDec(s):
    prev = 0
    if len(s) > 1:
        prev = getDec(s[:-1]) * 2

    return prev + int(s[-1])

def checkPalindrome(vals):
    if len(vals) < 2:
        return True
    else:
        if vals[0] == vals[-1]:
            return checkPalindrome(vals[1:-1])
        else:
            return False

input = [1, 2, 3, 4]

for x in range(len(input)):
    for y in range(len(input)):
        for z in range(len(input)):
            for a in range(len(input)):
                if x != y and x != z and x != a and y != z and y != a and z != a:
                    pass
                    #print(input[x], input[y], input[z], input[a])


def findPerm(vals):
    def traverseAllPerms(vals, sol):
        if len(vals) == len(sol):
            lst.append([vals[x] for x in sol])
        else:
            for x in range(len(vals)):
                if x not in sol:
                    sol.append(x)
                    traverseAllPerms(vals, sol)
                    sol.pop()
    lst = []
    traverseAllPerms(vals, [])
    return lst



allPerms = findPerm(input)

for x in range(len(input)):
    for y in range(x + 1, len(input)):
        for z in range(y + 1, len(input)):
            if x != y and x != z and y != z:
                pass
                #print(x,y,z)

def findCombi(vals, n):
    def traverseAllPerms(vals, sol, si):
        if n == len(sol):
            lst.append([vals[a] for a in sol])
        else:
            for x in range(si, len(vals)):
                if x not in sol:
                    sol.append(x)
                    traverseAllPerms(vals, sol, x + 1)
                    sol.pop()
    lst = []
    traverseAllPerms(vals, [], 0)
    return lst

vals = [7,7,7,4,4,4,2]
target = 14

def getAllCombi(n, target):
    def traverseAllLengths():
        for x in range(2, n):
            combi = findCombi(vals, x)

            for y in combi:
                if sum(y) == target:
                    out.append(y)
    out = []
    traverseAllLengths()
    return out



# A practical number is one whose divisors can be combined in various ways to form all the integers from 1 to that number. Each divisor may only be used once and they can only be added together, not multiplied or any other operation.
#
# For example, 12 is a practical number because it has factors of 1, 2, 3, 4, 6 and 12. We can combine these to form all the numbers from 1 to 12 as follows:
#
# 1 = 1
# 5 = 2 + 3
# 9 = 6 + 3
# 2 = 2
# 6 = 6
# 10 = 6 + 4
# 3 = 3
# 7 = 6 + 1
# 11 = 6 + 4 + 1
# 4 = 4
# 8 = 6 + 2
# 12 = 12



def getCoins():

    coins = [1, 2, 5]
    target = 10
    l = []
    def get(coins, target, lst):
        nonlocal l
        if target == 0:
            l.append(lst)
            return lst
        else:
            for x in coins:
                if target >= x:
                    get(coins, target - x, lst + [x])

    print(get(coins, target, []))
    print(l)
    new = [len(x) for x in l]
    mn = min(new)
    l = sorted(l)[::-1]
    for x in l:
        if len(x) == mn:
            return x
print(getCoins())




def getCoins():

    coins = [1, 2, 5]
    target = 10
    l = []
    def get(coins, target, lst):
        nonlocal l
        if target == 0:
            l.append(lst)
            return lst
        else:
            for x in coins:
                if target >= x:
                    get(coins, target - x, lst + [x])









