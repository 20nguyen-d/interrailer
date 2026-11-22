def find_sub_string():
    a = "animals are cute"
    b = "are2"
    success = False
    my_number = len(b)
    for x in range(len(a) - my_number):
        if a[x] == b[0]:
            z = 0
            found = True
            while z < len(b)-1:
                if a[x+z] != b[z]:
                    found = False
                z = z + 1
            if found == True:
                success = True
    if success == True:
        print("yay")
    else:
        print("no")

def check_for_symmetry():
    a = input("give me a string: ")
    z = 0
    y = len(a) - 1
    success = True
    while y - z > 1:
        if a[y] != a[z]:
            success = False
        z = z + 1
        y = y - 1
    if success == True:
        print("yay")
    else:
        print("nope")

def remove_one():
    a = "abcdef"
    pos = 3
    b = a[0:pos] + a[pos+1: ]
    print(b)

def remove_b():
    a = 'abbcc'
    b = 'bc'
    while b in a:
        c = a.index(b)
        a = a[0:c] + a[c+len(b):]

        print(a)


def string_stuff():
    first_list = input("give me a string ")
    second_list = input("give me a string ")
    third_list = input("give me a string ")
    success = True
    for x in first_list + second_list:
        if x not in third_list:
            success = False
    if len(first_list) + len(second_list) != len(third_list):
        success = False
    if success == True:
        print("yay")
    else:
        print("no")

def string_in_string():
    a = input("give me a string: ")
    b = input("give me a string: ")
    a = a + a
    if b in a and len(b) == len(a):
        print(True)

def name_change():
    your_name = input("give me your full name ")
    success = False
    space = -1
    for n in range(len(your_name) - 1, -1, -1):

        if your_name[n] == ' ':
            success = True
            space = n
    distance = your_name[0:space]

    your_name = your_name[space + 1: ] + ' ' + distance[0].upper() + distance[1:]

    print(your_name)

def most_common_end():
    a = input("give me a list ").split(",")
    space = -1
    values = []
    for x in range(len(a)):
        for y in range(len(a[x]) - 1, -1, -1):
            if a[x][y] == ' ':
                space = y
            value = (a[x][space : ])
        values.append(value)

    m = 0
    max = 0
    t = 0
    for m in range(len(values)):
        p = 0
        for s in values:
            if values[m] == s:
                p = p + 1
        if max < p:
            max = p
            t = values[m]
    print(t)

def sentence_matrix():
    your_string = input("give me a string ")
    n = int(input("give me a number "))
    board = []
    m = len(your_string) % n
    for i in range((len(your_string) // n) + m ):
        board.append([' '] * n)

    col = 0
    row = 0
    for v in your_string:
        board[row][col] = v
        col = col + 1
        if col >= n:
            col = 0
            row = row + 1


    for i in range(((len(your_string) + n - 1) // n) ):
        print(board[i])

def longest_shortest_word():
    your_string = input("give me a string ").split(" ")
    numbers = []
    answer = []
    for x in range(len(your_string)):
        numbers.append(len(your_string[x]))
    max = numbers[0]
    min = numbers[0]
    for y in range(len(numbers)):
        if max < numbers[y]:
            max = numbers[y]
        if min > numbers[y]:
            min = numbers[y]
    for z in your_string:
        if len(z) == min:
            answer.append(z)
        elif len(z) == max:
            answer.append(z)
    print(answer)

def names():
    names = ['Le', 'Nguyen', 'Tran', 'Nguyen']
    dt = {}

    for name in names:
        if name in dt:
            dt[name] = dt[name] + 1
        else:
            dt[name] = 1

    for name in dt:
        print(name, ':', dt[name])

def check_symmetry():
    your_string = input("give me a string ")
    t = len(your_string)
    n = 0
    success = True
    yay = True
    for m in your_string:
        if your_string[t - 1] == your_string[n]:
            t = t - 1
            n = n + 1
        elif your_string[t - 1] != your_string[n]:
            success = False
    if success == True:
        print("Yay!")
    if success == False:
        for y in range(len(your_string)):
            new = your_string[0:y] + your_string[y+1:]
            l = len(new)
            s = 0
            for a in new:
                if new[l - 1] == new[s]:
                    l = l - 1
                    s = s + 1
                elif new[l - 1] != new[s]:
                    yay = False
            if yay == True:
                print("Yayy!")

def sym_minus_one():
    def is_sym_2(s):
        t = len(s)
        n = 0
        success = True
        for m in s:
            if s[t - 1] == s[n]:
                t = t - 1
                n = n + 1
            elif s[t - 1] != s[n]:
                success = False

        return success

    def is_sym(s):
        return s[::-1] == s

    your_string = input("give me a string ")
    yay = True
    success = is_sym(your_string)
    if success == True:
        print("Yay!")

    if success == False:
        for y in range(len(your_string)):
            new = your_string[0:y] + your_string[y+1:]
            yay = is_sym(new)
            if yay == True:
                print("Yayy!")



def taxi_company():
    print("Welcome to the Taxi Company")
    km_distance = int(input("How many kilometres would you like to go?")) #prompt for how many kilometres
    while km_distance <= 0:                                   #while loop to re-prompt if the kn_distance is invalid
        km_distance = int(input("How many kilometres(>0) would you like to go? "))
    passenger_number = int(input("How many passengers will be coming? ")) #prompt for how many passengers
    passenger_fare = 2 * passenger_number #how much the passengers cost(£2 * passenger_number)
    km_fare = 1.50 * km_distance #how much the distance costs(£1.50 * km_distance)
    total_fare = passenger_fare + km_fare #this calculates the overall fare
    print('The overall fare will be: £{}, £{} for passengers, and £{} for distance. '.format(total_fare, passenger_fare, km_fare))
    #this outputs the overall fare,passenger fare, and distance fare













