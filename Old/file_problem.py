def read_from_file(filename):
    with open(filename, "r") as fp:
        return fp.read()


def write_to_file(filename, content):
    with open(filename, "a") as fp:
        print(content)
        fp.write("\n" + content)


def solve_from_string(str):
    operations = ['+', '-', '*', '/']
    for pos, x in enumerate(str):
        if x in operations:
            number1 = int(str[:pos])
            number2 = int(str[pos+1:])
            if x == '+':
                return number1 + number2
            elif x == '-':
                return number1 - number2
            elif x == '*':
                return number1 * number2
            elif x == '/':
                return number1 / number2


content = read_from_file("file2.txt").split('\n')
number = int(content[0])
for x in range(1, number+1):
    output = solve_from_string(content[x])
    write_to_file("file2.out", str(output))
