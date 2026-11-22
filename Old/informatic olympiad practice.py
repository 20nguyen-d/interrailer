import copy
import random

def encrypt(word):
    alphabet = '!abcdefghijklmnopqrstuvwxyz'
    def run(s):

        for x in range(1, len(s)):
            left = alphabet.index(s[x - 1])
            right = alphabet.index(s[x])
            print(left, right)
            num = left + right
            if num > 26:
                num -= 26
            s[x] = alphabet[num]
        return s

    return ''.join(run([x for x in word]))

def decrypt(code):
    alphabet = '!abcdefghijklmnopqrstuvwxyz'
    code = code[::-1]
    code = [x for x in code]
    for x in range(len(code) - 1):

        num1 = alphabet.index(code[x])

        num2 = alphabet.index(code[x + 1])
        print(code[x], num1, code[x +1], num2)
        if num1 > num2:
            num3 = num1 - num2
        else:
            num3 = 26 + (num1 - num2)


        code[x] = alphabet[num3]

    return ''.join(code[::-1])


def palindromes(n):
    n = [int(x) for x in str(n)]
    if len(n) == 1:
        if n[0] < 8:
            return n[0] + 1
        else:
            return 11
    if len(n) % 2 == 1:
        midpoint = len(n)//2
        left = n[:midpoint]
        mid = str(n[midpoint])
        right = n[midpoint+1:]
        left = ''.join([str(x) for x in left])
        right = ''.join([str(x) for x in right])

        if int(left[::-1]) > int(right):
            return left + mid + left[::-1]
        else:
            if int(mid) < 9:
                return left + (str(int(mid) + 1)) + left[::-1]

            else:

                if n.count(9) == len(n):
                    return('1' + ('0'*(len(n) - 1)) + '1')

                else:
                    left = str(int(left) + 1)
                    return left + '0' + left[::-1]
    else:
        left = n[:len(n)//2]
        right = n[len(n)//2:]
        left = ''.join([str(x) for x in left])
        right = ''.join([str(x) for x in right])
        if int(left[::-1]) > int(right):

            return left + left[::-1]


        if left.count('9') == len(left):

            return '1' + ('0'*(len(n) - 1)) + '1'

        else:
            left = str(int(left) + 1)
            return left + left[::-1]

def clock(one, two):

    def convert(mins):
        num = mins//60
        num2 = mins - (num * 60)
        return num%24, num2


    def get_time(fast, hours):
        val = hours * (60 + fast)

        return convert(val)


    count = 1
    while get_time(one, count) != get_time(two, count):
        count += 1

    time = get_time(one, count)
    hours = time[0]
    minutes = time[1]
    if len(str(hours)) < 2:
        hours = '0' + str(hours)
    if len(str(minutes)) < 2:
        minutes = '0' + str(minutes)


    return str(hours) + ':' + str(minutes)

def debt_repayment(interest, repayment):

    months = 1
    newdebt = 100.0
    repayval = 0
    out = 0
    while newdebt > 0:
        newdebt = newdebt * (1 + (interest/100.0))
        repayval = max(50,(repayment/100.0) * newdebt)
        repayval = min(repayval, newdebt)
        newdebt -= repayval
        out += repayval
        months  += 1
        if months > 10:
            break

    return out


def trailexplorer(num, instructions, moves):
    def nextpos(d, position, i):
        pos = copy.copy(position)
        if d == 'n':
            if i == 'f':
                pos[1] += 1
            elif i == 'r':
                pos[0] += 1
            else:
                pos[0] -= 1
        elif d == 'e':
            if i == 'f':
                pos[0] += 1
            elif i == 'r':
                pos[1] -= 1
            else:
                pos[1] += 1
        elif d == 's':
            if i == 'f':
                pos[1] -= 1
            elif i == 'r':
                pos[0] -= 1
            else:
                pos[0] += 1
        else:
            if i == 'f':
                pos[0] -= 1
            elif i == 'r':
                pos[1] += 1
            else:
                pos[1] -= 1

        return pos

    trail = [[0,0]]
    compass = 'nesw'
    direction = 0

    instructions = instructions * moves
    count = 0

    while count < moves:
        emergency = 0
        current = instructions[count]
        new = nextpos(compass[direction%4], trail[-1], current)

        if current == 'r':
            direction += 1
        elif current == 'l':
            direction -= 1

        if new not in trail:
            trail.append(copy.copy(new))
        else:
            check = False
            for x in range(3):
                direction += 1
                new = nextpos(compass[direction%4], trail[-1], 'f')
                if new not in trail:
                    trail.append(copy.copy(new))
                    check = True
                    break
            if not check:
                return trail



        while len(trail) > num:
            trail.pop(0)



        count += 1


    return trail



def q1():
    testcases = int(input())
    lst = []
    for x in range(testcases):
        lst.append(input().split(' '))

    new = []
    for x in lst:
        a = []
        for y in x:
            a.append(int(y))

        new.append(a)

    def go(days, val):
        total = sum(days)

        newnum = val // total
        newval = newnum * total

        count = 1
        if newval >= val:
            return len(days) * newnum
        else:
            n = newval
            for x in days:
                n += x
                if n >= val:
                    break
                count += 1

            return len(days) * newnum + count

    for x in new:
        print(go(x[1:], x[0]))



def anagram_numbers(num):
    def check(a, b):
        a = [int(x) for x in str(a)]
        b = [int(x) for x in str(b)]
        return sorted(a) == sorted(b)

    out = ''
    c = False
    for x in range(2, 10):
        new = num * x
        if check(new, num):
            c = True
            out += str(x)
            out += ' '

    if not c:
        return 'NO'
    else:
        return out

def fibonacci_letters(one, two, n):
    def get_next(a, b):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        val1 = alphabet.index(a)
        val2 = alphabet.index(b)
        val3 = val1 + val2 + 1

        return alphabet[val3%26]

    out = [one, two]
    while len(out) < n:
        out.append(get_next(out[-2], out[-1]))

    return out[-1]



def decoder_ring(n, code):
    def newring(num):
        alphabet = [chr(ord('a') + x) for x in range(26)]
        new = ''
        lst = [1 for x in range(26)]
        i = -1
        while len(new) < 26:
            for c in range(num):
                i = (i + 1) % 26
                while lst[i] == 0:
                    i = (i + 1) % 26
            new += alphabet[i]
            lst[i] = 0
        return new
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    def one():
        new = newring(n)
        out = ''
        for x in code:
            val = alphabet.index(x)
            val *= 2
            val = val % 26
            out += new[val]

    new = newring(n)
    out = ''
    for x in code:
        val = alphabet.index(x)
        out += new[val]

    return out




def roman(word, n):
    def go(w):
        new = []
        start = 0
        w += '!'
        for x in range(len(w)):
            if w[x] != w[start]:
                new.append(w[start:x])
                start = x
        return new



def digitwords(word):
    def check(num, w):
        num2 = copy.copy(num)
        w2 = copy.copy(w)

        for x in w2:
            print(x, num2)
            if x == num2[0]:
                num2 = num2[1:]
        d = {}


    print(check('one', 'bounce'))

print(digitwords('dsfs'))


def triangles(colours):
    def get(a, b):
        cols = ['r', 'g', 'b']
        if a == b:
            return a
        cols.remove(a)
        cols.remove(b)

        return cols[0]

    def go(s):
        out = ''
        for x in range(len(s) - 1):
            out += get(s[x], s[x+1])

        return out

    new = go(colours)
    while len(new) > 1:
        new = go(new)




testcases = int(input())
lsts = []
ks = []
nums = []
for x in range(testcases):
    q = input().split(' ')
    nums.append(int(q[0]))
    ks.append(int(q[1]))
    w = input().split(' ')
    lsts.append([int(a) for a in w])


def get(lst, k, n):

    lst = sorted(lst)
    lst2 = sorted(set(lst))
    d = {}
    good = 0
    for x in lst:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    for x in lst2:
        val = k - x
        if val in lst2 and val > x:

            n1 = d[x]
            n2 = d[val]
            good += min(n1, n2)
        elif val == x:
            n = d[x]
            good += n//2

    return good


for x in range(len(lsts)):
    print(get(lsts[x], ks[x], nums[x]))

def go(cards, n, m):
    d = {}
    lst = []
    for x in range(0, n*m):
        for y in range(len(cards)):
            for z in cards[y]:
                if z == x:
                    d[x] = y
                    lst.append(y)

    if m > 1 and n > 1:
        new = list(divide(lst, n))
        if check(new):
            return ' '.join([str(x+1) for x in new[0]])
        else:
            return -1
    else:
        return ' '.join([str(x+1) for x in lst])



