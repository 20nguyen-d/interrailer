def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n -2)



def gcd(a, b):
    if a == 1 or a == b:
        return a
    if b == 1:
        return b
    else:
        if a > b:
            return gcd(a - b, b)
        else:
            return gcd(a, b - a)



def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n



def digitsum(s):
    if s == '':
        return 0
    else:
        return int(s[0]) + digitsum(s[1:])




print(digitsum('132243'))


l

