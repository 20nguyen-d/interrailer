def calc(a, b, opr):
    if opr == '+':
        return a + b
    elif opr == '-':
        return a - b
    elif opr == '*':
        return a * b
    elif opr == '/':
        return a / b

def calculate(expr):
    operators = "+-*/"
    check_opr = False
    for operator in operators:
        if operator in expr:
            check_opr = True
            opr_index = expr.index(operator)
            a = float(expr[: opr_index])
            b = float(expr[opr_index + 1:])
            answer = calc(a, b, operator)
    if check_opr == False:
        return False
    return answer

assert calculate("51+13") == 64
assert calculate("2-1") == 1
assert calculate("4*2") == 8
assert calculate("10/5") == 2
calculate("10%5")

def fact(n):
    if n < 1:
        return 1
    else:

       return n * fact(n - 1)


def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def powers(a, n):
    if n < 1:
        return 1
    else:
        return a * powers(a, (n-1))


def fraction_sequence(n):
    if n < 1:
        return 0
    else:
      return 1/n + fraction_sequence(n-1)


def power_sequence(n):
    if n < 1:
        return 0
    else:
      return 2 ** n + power_sequence(n-1)


print(power_sequence(123))
print(calculate('5+6'))
print(calc(5, 6, '+'))