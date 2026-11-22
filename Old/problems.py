import random
def capital_indexes(string):
    indexes = []
    for x in range(len(string)):
        if ord(string[x]) >= 65 and ord(string[x]) <= 90:
            indexes.append(x)
    return indexes
def mid(string):
    if len(string) % 2 == 0:
        return ''
    else:
        number = (len(string) - 1)//2
        return string[number]
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
def online_count(dictionary):
    count = 0
    for x in dictionary.keys():
        if dictionary[x] == "online":
            count = count + 1
    return count
def random_number():
    return random.randint(1, 100)
def only_ints(a, b):
    if a != bool and b != bool:
        if isinstance(a, int) and isinstance(b, int):
            return True
    else:
        return

def double_letters(string):
    for x in range(len(string)):
        if x != len(string)-1:
            if string[x] == string[x+1]:
                return True
    return False
def add_dots(string):
    new_string = []
    ready_string = ''
    for x in range(len(string)):
        new_string.append(string[x])
        if x < len(string)-1:
            new_string.append('.')
    ready_string = ready_string.join(new_string)
    return ready_string
def remove_dots(string):
    new_string = []
    ready_string = ''
    for x in string:
        if x != '.':
            new_string.append(x)
    ready_string = ready_string.join(new_string)
    return ready_string
def count(string):
    tally = 0
    for x in string:
        if x == '-':
            tally = tally + 1
    return tally + 1
def is_anagram(a, b):
    a = sorted(a)
    b = sorted(b)
    if a == b:
        return True
    else:
        return False
def flatten(list_of_lists):
    new_list = []
    for x in list_of_lists:
        for y in x:
            new_list.append(y)
    return new_list
def largest_difference(numbers):
    min = 101
    max = -101
    for x in numbers:
        if x < min:
            min = x
        if x > max:
            max = x
    return max - min
def div_3(number):
    if number % 3 == 0:
        return True
    else:
        return False
def get_row_col(square):
    row = ord(square[0]) - ord('A')
    col = ord(square[1]) - ord('1')

    return col, row
def palindrome(string):
    return string == string[::-1]
def up_down(number):
    return number - 1, number + 1
def consecutive_zeros(sequence):
    count = 0
    list = []
    for x in sequence:
        if x == '0':
            count = count + 1
        if x == '1':
            list.append(count)
            count = 0
    list.append(count)
    max = 0
    for y in list:
        if y > max:
            max = y
    return max
def all_equal(list):
    content = None
    if len(list) > 0:
        content = list[0]
    check = True
    for x in list:
        if x != content:
            check = False
    return check
def triple_and(a, b, c):
    return a and b and c
def convert(list):
    return [str(x) for x in list]
def zap(a, b):
    return_list = []
    for x in range(len(a)):
        y = (a[x], b[x])
        return_list.append(y)
    return return_list
def validate(code):
    if 'def' not in code:
        return "missing def"
    elif ':' not in code:
        return "missing :"
    elif '(' not in code:
        return "missing paren"
    elif ')' not in code:
        return "missing paren:"
    bracket1 = code.index('(')
    bracket2 = code.index(')')
    if bracket1 + 1 == bracket2 and code[bracket1 - 1] != '"' and code[bracket2 + 1] != '"':
        return "missing param"
    elif '    ' not in code:
        return "missing indent"
    elif 'validate' not in code:
        return "wrong name"
    elif 'return' not in code:
        return "missing return"
    return True

def list_xor(n, list1, list2):
    if n in list1 and n in list2 or n not in list1 and n not in list2:
        return False
    else:
        return True
def param_count(*args):
    return len(args)
def format_number(number):
    number = str(number)
    l = len(number)-1
    my_list = number[::-1]
    new_list = []
    count = 0
    for y in my_list:
        count = count + 1
        new_list.append(y)
        if count == 3:
            new_list.append(',')
            count = 0
    new_list = new_list[::-1]
    return "".join(new_list)


print(format_number(1234512345))


















