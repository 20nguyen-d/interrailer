def missing_operation(expr):
    first_number = None
    second_number = None
    answer = None
    operation = []
    for x in range(len(expr)):
        equals_pos = expr.index('=')
        if expr[x] == '?':
            first_number = int(expr[:x])
            second_number = int(expr[x+1:equals_pos])
            answer = int(expr[equals_pos+1:])
    if first_number + second_number == answer:
        operation.append('+')
    if first_number - second_number == answer:
        operation.append('-')
    if first_number // second_number == answer:
        operation.append('//')
    if first_number * second_number == answer:
        operation.append('*')
    return operation

def missing_number(expr):
    operation = None
    number = None
    equals = expr.index('=')
    values = []
    ex = ['+', '-', '//', '*']
    if expr[0] == '?':
        operation = expr[1]
        number = int(expr[2: equals])
        answer = int(expr[equals + 1:])
    else:
        for x in range(len(expr)):
            if expr[x] in ex:
                operation = expr[x]
                number = int(expr[: x])
        answer = int(expr[equals + 1:])
    if operation == '+':
        values.append(answer - number)
    if operation == '-':
        values.append(answer + number)
    if operation == '//':
        values.append(answer * number)
    if operation == '*':
        values.append(answer // number)

    return values
def calc(a, b, opr):
    if opr == '+':
        return a + b
    elif opr == '-':
        return a - b
    elif opr == '*':
        return a * b
    elif opr == '/':
        return a / b

def which_one(expr):
    opr = ['+', '-', '//', '*']
    equals = expr.index('=')
    if expr[equals:] != int:
        print('')
equation = input('Equation = ')
if which_one(equation) is True:
    print(missing_number(equation))
else:
    print(missing_operation(equation))
