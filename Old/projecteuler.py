def testParenthesis(s):
    def v1(s):
        while '()' in s:
            ind = s.index('()')
            s = s[:ind] + s[ind+2:]
        return s == ''

    count = 0
    for x in s:
        if x == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            break
    return count == 0

def testParenthesis2(s):
    c1 = 0
    c2 = 0
    for x in s:
        if c1 < 0 or c2 < 0:
            break
        if x == '(':
            c1 += 1
        elif x == ')':
            c1 -= 1
        elif x == '[':
            c2 += 1
        else:
            c2 -= 1
        if c1 == 0 and c2 > 0:
            break
    return c1 == 0 and c2 == 0

def testParenthesis3(s):
    c1 = 0
    c2 = 0
    for x in s:
        if c1 < 0 or c2 < 0:
            break
        if x == '(':
            c1 += 1
        elif x == ')':
            c1 -= 1
        elif x == '[':
            c2 += 1
        else:
            c2 -= 1
        if c1 == 0 and c2 > 0:
            break
    return c1 == 0 and c2 == 0

##print(testParenthesis("(())()"))
#print(testParenthesis("(()))(()"))
print(testParenthesis2("(([))(])"))
print(testParenthesis2("([)]")) #false6
print(testParenthesis2("(([]))(([()]))"))
print(testParenthesis2("(())[]"))

a = ''
b = ''