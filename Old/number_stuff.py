import random
def pig() :
    n = int(input("Give me a number"))
    for c in range(n):
        if c % 6 == 0 :
            print("{}boo".format(c))
        elif c % 3 == 0 :
            print("{}bee".format(c))

def prime():
    n = int(input("Give me a number "))
    c = 0
    p = True
    for c in range(2, n // 2 + 1):
        if n % c == 0:
            p = False

    print(p)

def square_root():
    n = int(input("Give me a number "))
    a = 0
    while a * a < n:
        if a * a != n:
            a = a + 1
    if a * a != n:
        a = print("{} does not have a non-decimal square root ".format(n))
    print(a)

def all_primes():
    n = int(input("Give me a number "))
    p = 0
    for p in range(2, n):
        t = True
        for c in range(2, p // 2 + 1):
            if p % c == 0:
                t = False
        if t:
            print(p)

def four_factor():
    n = int(input("Give me a number "))
    for j in range(2, n + 1):
        t = 0
        for g in range(2, j // 2 + 1):
            if j % g == 0:
                t = t + 1
        if t == 2:
            print(j)

def guess_number():
    import random
    player = int(input("Try to guess my number between 1 and 100! "))
    computer = random.randint(1, 100)
    t = 0
    while player != computer:
        if int(player) > int(computer):
            print("Too big")
            player = int(input("Try to guess my number between 1 and 100! "))
        elif int(player) < int(computer):
            print("Too small")
            player = int(input("Try to guess my number between 1 and 100! "))
        if int(player) != int(computer):
            t = t + 1

    print("You guessed my number in {} guesses!".format(t + 2))

def fibonacci():
    n = int(input("Give me a number larger than 2 "))
    k = 1
    s = 1
    p = [1, 1]
    while n <= 2:
        n = int(input("Give me a number larger than 2 "))

    for m in range(n - 2):
        e = k + s
        k = s
        s = e
        p.append(s)
    print(s )
    print(p)

def super_primes():
    n = int(input("Give me a number "))
    m = 0

    for t in range(2, 1000000000000000):
        p = True
        for e in range(2, t // 2 + 1):
            if t % e == 0:
                p = False
        if p:
            print(t)
            m = m + 1

            if m == n:
                break

def three_digit():
    n = int(input("Give me your 3-digit number "))
    t = n // 100
    m = n - (t * 100)
    e = m // 10
    s = m - (e * 10)
    if t == s and t < e:
        print("Great! {} wins!".format(n))
    else:
        print("{} loses!".format(n))

def chicken_dog():
    k = int(input("How many chickens and dogs do you have altogether? "))
    s = int(input("What is the sum of their legs? "))
    l = k
    while 4 * (k - l) + 2 * l != s:
        l = l - 1
    c = l
    d = k - c

    print("You have {} chickens and {} dogs!".format(c , d ))

def solve_equation():
    a = int(input("Give me a number "))
    b = int(input("Give me another number "))
    c = int(input("Give me another number "))
    t = 0
    for x in range (0, 100):
        for y in range(0, 100):
            if (x * a) + (y * b) == c:
                t = t + 1
                print("x = {}, y = {}".format(x, y))
    if t == 0:
        print("NO POSSIBILITIES!")

def average():
    vals = [4, 3, 7, 1, 5, 1]
    max = vals[0]
    min = vals[0]
    for c in range(len(vals)):
        if max < vals[c]:
            max = vals[c]
        if min > vals[c]:
            min = vals[c]
    print(max, min)
    n = len(vals)
    sum = 0
    for e in range(len(vals)):
        sum = sum + vals[e]
    print(sum)



def index():
    values = input("Give me a list of numbers: ").split(",")
    values = [int(x) for x in values]
    min = 0
    for t in range(len(values)):
        if values[min] > values[t]:
            min = t
    print(min, values[min])

def duplication_one():
    values = input("Give me a list of numbers: ").split(",")
    values = [int(x) for x in values]
    t = 0
    for n in range(len(values)):
        for p in range(n + 1, len(values)):
            if values[n] == values[p]:
                t = 1
                print("duplication found")
    if t == 0:
        print("no duplication")

    values = input("Give me a list of numbers: ").split(",")
    values = [int(x) for x in values]

def duplication_two():
    values = input("Give me a list of numbers: ").split(",")
    values = [int(x) for x in values]
    indexes = []
    e = values[0]
    indexes.append(0)
    t = 1
    s = 1
    while s < len(values):
        if e == values[s]:
            t = t + 1
            indexes.append(s)
        s = s + 1
    print(t)
    print(indexes)
    if t == 1:
        print("NOOOOOO")

def duplicate_and_check():
    values = input("Give me a list of numbers: ").split(",")
    values = [int(x) for x in values]
    processed = []
    for a in range(len(values)):
        e = values[a]
        if e not in processed:
            processed.append(e)
            indexes = []
            t = 0
            s = 0
            while s < len(values):
                if e == values[s]:
                    t = t + 1
                    indexes.append(s)
                s = s + 1

            if t == 1:
                print("{} is not duplicated".format(values[a]))
            else:
                print("{} is duplicated {} times at position {}".format(e, t, indexes))

def random_one():
    import random
    processed = []
    k = int(input("Give me a number "))
    for s in range(k):
        success = False
        while not success:
            t = random.randint(1, 100000000000000)
            if t not in processed:
                processed.append(t)
                success = True
    print(processed)

def small_big():
    import random
    processed = []
    m = int(input("Give me a number "))
    s = 0
    for e in range(m):
        success = False
        while not success:
            t = random.randint(1, 1000 - m + e)
            if t > s:
                s = t
                processed.append(t)
                success = True
    print(processed)

def decreaser():
    import random
    processed = []
    m = int(input("Give me a number "))
    s = 1000000000000000
    for e in range(m):
        success = False
        while not success:
            t = random.randint(1 + (m - e) , 1000)
            if t < s:
                s = t
                processed.append(t)
                success = True
    print(processed)

def biggeryesno():
    i = input("give me a list ").split(",")
    i = [int(x) for x in i]
    processed = []
    p = 0
    success = True
    for s in range(len(i)):
        for n in range(s + 1, len(i)):
            if i[s] >= i[n]:
                success = False
    if success == False:
        print("no")
    elif success == True:
        print("yes")

def rangecompare():
    i = input("give me a list ").split(",")
    i = [int(x) for x in i]
    p = int((sum(i)) / len(i))
    n = list(range(p - 5, p + 6))
    a = []
    success = True
    for t in i:
        if t not in n:
            success = False
            a.append(t)
    if success == True:
        print("YES!")
    elif success == False:
        print("{} no".format(a))

def list_extra_print():
    i = input("give me a list ").split(",")
    i = [int(x) for x in i]
    max = i[0]
    min = i[0]
    n = []
    for c in range(len(i)):
        if max < i[c]:
            max = i[c]
        if min > i[c]:
            min = i[c]
    for p in range(min, max):
        if p not in i:
            n.append(p)
    print(n)

def impossible():
    i = input("give me a list ").split(",")
    i = [int(x) for x in i]
    processed = []
    p = 0
    success = True
    for s in range(len(i)):
        for n in range(s + 1, len(i)):
            if i[s] <= i[n]:
                success = False
    if success == True:
        print("yes")
    elif success == False:
        min = i[0]
        processed = []
        p = 0
        for t in range(len(i)):
            min = t
            for n in range(t, len(i)):
                while p <= (len(i)):
                    if min > i[t]:
                        min = i[t]
                        processed.append(min)
                        p = p + 1
                        min = i[p]
    print(processed)

def move_positions():
    i = input("give me a list ").split(",")
    i = [int(x) for x in i]
    p = len(i)-1
    b = 0
    n = []
    n.append(i[p])
    for s in range(len(i) - 1):
        n.append(i[b])
        b = b + 1
    print(n)

def decrease_list():
    i = input("give me a list ").split(",")
    i = [int(x) for x in i]
    s = 1000000000
    n = True
    for p in i:
        if p >= s:
            n = False
        s = p
    if n == False:
        print("Ñ000000000000000000!!!!!!!")
    elif n == True:
        print("ŸAAAAAAAAAAAAAAAAAAAAAAŸ!!!!!!!!!")

def sort_list():
    a = [14, 11, 13, 12]
    c = 0
    min = 0
    for b in range(c, len(a)):
        if a[b] < a[min]:
            min = b
    a[0], a[min] = a[min], a[0]

    c = 1
    min = c
    for b in range(c, len(a)):
        if a[b] < a[min]:
            min = b
    a[c], a[min] = a[min], a[c]
    print(a)

def check_symmetry():
    i = input("give me a list ").split(",")
    i = [int(x) for x in i]
    t = len(i)
    n = 0
    success = True
    for m in i:
        if i[t - 1] == i[n]:
            t = t - 1
            n = n + 1
        elif i[t - 1] != i[n]:
            success = False
    if success == True:
        print("Yay!")
    if success == False:
        print("NO!")

def check_symmetry_2():
    i = input("give me a list ").split(",")
    i = [int(x) for x in i]
    success = True
    for p in range(len(i)//2):
        if i[p] != i[len(i) - (p + 1)]:
            success = False
    if success == True:
        print("Yay!")
    if success == False:
        print("NO!")

def one_missing():
    i = input("give me a list ").split(",")
    i = [int(x) for x in i]
    min = i[0]
    max = i[0]
    b = []
    a = []
    success = True
    for t in range(len(i)):
        if max < i[t]:
            max = i[t]
        if min > i[t]:
            min = i[t]
    for n in range(min, max):
        if n not in i:
            b.append(n)
    if len(b) != 1:
        success = False
    if len(i) != max - min:
        success = False
    if success == True:
        print("YAY!")
    else:
        print("NO!")

def most_repeated():
    i = input("give me a list ").split(",")
    i = [int(x) for x in i]
    for e in i:
        if e not in list(range(1, 21)):
            print("N")
    m = 0
    max = 0
    t = 0
    for m in range(len(i)):
        p = 0
        for s in i:
            if i[m] == s:
                p = p + 1
        if max < p:
            max = p
            t = i[m]
    print(t)

def no_repeat():
    i = input("give me a list ").split(",")
    i = [int(x) for x in i]
    s = input("give me another list ").split(",")
    s = [int(x) for x in s]
    t = []
    n = []
    for e in i:
        if e in s:
            if e not in t:
                t.append(e)
    print(t)

    for m in i:
        if m not in n:
            n.append(m)
    for k in s:
        if k not in n:
            n.append(k)
    print(n)

def digit_sum():
    n = int(input("give me a number "))
    a = 1
    b = 0
    while n > a:
        a = a * 10
    a = a // 10
    while a > 1:
        t = n // a
        m = n - (t * a)
        a = a // 10
        n = m
        b = b + t
    b = b + n
    print(b)

def even_spaces():
    i = input("give me a list ").split(",")
    i = [int(x) for x in i]
    p = True
    m = 0
    c = 0
    r = 1
    h = True
    for q in range(len(i)-1):
        if i[q] < i[q+1]:
            p = False
        elif i[q+1] < i[q]:
            p = True
        if p == False :
            m = i[q + 1] - i[q]
            while r < len(i):
                if i[c] + m != i[r]:
                    h = False
                r = r + 1
                c = c + 1
        elif p == True:
            m = i[q] - i[q + 1]
            while r < len(i):
                if i[c] - m != i[r]:
                    h = False
                r = r + 1
                c = c + 1
    if h == False:
        print("NO!")
    elif h == True:
        print("YAY!")

def no_append_stuff():
    question = int(input("give me a number - -1 to stop"))
    max = 0
    min = question + 1
    total = 0
    my_number = 0
    while question != -1:
        total = total + question
        my_number = my_number + 1
        question = int(input("give me a number - -1 to stop"))
        if question > max:
            max = question
        if question < min and question != -1:
            min = question
        average = total // my_number
    print(max, min, total, average)

def no_append_even_space():
    question = int(input("give me a number - -1 to stop"))
    my_number = question
    victory = True
    has_difference = False
    difference = 0
    while question != -1:
        question = int(input("give me a number - -1 to stop"))
        if question != -1:
            if has_difference:
                if my_number + difference != question:
                    victory = False
            else:
                has_difference = True
                difference = question - my_number
            my_number = question

    if victory == False:
        print("no")
    if victory == True:
        print("yes")

def how_many_times_number_appear():
    list = input("give me a list ").split(",")
    list = [int(x) for x in list]
    number = int(input("give me a number"))
    total = []
    indexes = []
    total_two = []
    for x in range(len(list)):
        if number == list[x]:
            total.append(number)
            indexes.append(x)
    print(len(total), indexes)
    if len(total) == 0:
        for y in list:
            my_number = abs(y - number)
            total_two.append(my_number)
        for z in range(len(total_two)):
            min = total_two[0]
            if z < min:
                min = z
        print(min)

def backward_list():
    list = input("give me a list ").split(",")
    list = [int(x) for x in list]


def common_factor():
    number_one = int(input("give me a number"))
    number_two = int(input("give me another number"))
    append_two = []
    append_one = []
    append_both = []
    if number_one > number_two:
        max = number_one
    else:
        max = number_two
    for x in range((max // 2) +1):
        my_range = x
    for y in range(1, (number_two//2)+ 1):
        if number_two % y == 0:
            append_two.append(y)
    for z in range(1, (number_one//2)+ 1):
        if number_one % z == 0:
            append_one.append(z)
    for a in append_two:
        if a in append_one:
            append_both.append(a)
    print("The factors of {} are {}".format(number_one, append_one))
    print("The factors of {} are {}".format(number_two, append_two))
    print("{} are common factors of {} and {}".format(append_both, number_one, number_two))

def numbers_with_your_factors():
    your_number = int(input("give me a number"))
    first_factors = []
    your_factors = []
    success = False
    for t in range(1, (your_number // 2) + 1):
        if your_number % t == 0:
            first_factors.append(t)
            my_number = len(first_factors)
    for n in range(2, 10000):
        number = 1
        your_factors = [n]
        for p in range(1, (n//2)+1):
            if n % p == 0:
                number = number + 1
                your_factors.append(p)
        if number == your_number:
            print(n)

def magic_factor():
    n_two = 0
    magic_number = 0
    second_factor = 0
    first_factor = 0
    n = 100
    for n in range(100, 1000):
        second_factor = 0
        first_factor = 0
        for f in range(1, (n//2)+1):
            if n % f == 0:
                first_factor = first_factor + f
                n_two = n
        number_two = first_factor
        for g in range(1, (number_two//2)+1):
            if number_two % g == 0:
                second_factor = second_factor + g
        if second_factor == n_two:
            magic_number = n_two
            print(magic_number)

def five_smaller_primes():
    primes = []
    number_two = 0
    your_number = int(input("give me a number "))
    for t in range(your_number, 0, -1):
        my_number = 0
        for n in range(1, t // 2 + 1):
            if t % n == 0:
                my_number = my_number + 1
        if my_number == 1:
            primes.append(t)
    print(primes[0], primes[1], primes[2], primes[3], primes[4])

def nearest_primes():
    other_number = []
    other_primes = []
    number = []
    primes = []
    your_number = int(input("give me a number"))
    for t in range(your_number, 0, -1):
        my_number = 0
        for n in range(1, t // 2 + 1):
            if t % n == 0:
                my_number = my_number + 1
        if my_number == 1:
            primes.append(t)
    list = (primes[0], primes[1], primes[2], primes[3], primes[4])
    for z in range(len(primes)):
        distance = abs(your_number - primes[z])
        number.append(distance)
    for b in range(your_number+1, your_number*2):
        my_number = 0
        for n in range(1, b // 2 + 1):
            if b % n == 0:
                my_number = my_number + 1
        if my_number == 1:
            other_primes.append(b)
    for x in range(len(other_primes)):
        distance = abs(other_primes[x] - your_number)
        other_number.append(distance)
    print(number)
    print(other_number)

    special = 0
    found = 0
    while found < 5 and special < your_number:
        if special in number:
            found = found + 1
            print(your_number - special)
        if special in other_number:
            found = found + 1
            print(your_number + special)
        special = special + 1

def in_order():
    your_list = input("give me a list ").split(",")
    your_list = [int(x) for x in your_list]
    my_number = 0
    my_list = []
    min = your_list[0]
    max = your_list[0]
    for c in range(len(your_list)):
        if max < your_list[c]:
            max = your_list[c]
        if min > your_list[c]:
            min = your_list[c]
    for my_number in range(min, max):
        for x in range(len(your_list)):
            if your_list[x] == my_number:
                my_list.append(your_list[x])
    print(my_list)

def tree_problem():
    your_list = [1, ]
    trees = int(input("give me a number of trees "))
    twig = []
    leaves = trees
    other_trees = []
    other_trees.append(leaves)
    distance = int(input("give me the distance between the trees"))
    last_distance = 0
    my_number = 1
    while my_number + distance <= trees * 2:
        my_number = my_number + distance
        if my_number > trees:
            new_number = (2 * trees - my_number) + 1
            your_list.append(new_number)
        else:
            your_list.append(my_number)
    print(your_list)

def patterns():
    your_list = input("give me a list ").split(",")
    your_list = [int(x) for x in your_list]
    success = True
    pattern = []
    x = 0
    distance = your_list[1] - your_list[0]
    while x+1 < len(your_list):
        if your_list[x] + distance != your_list[x+1]:
            success = False
        x = x + 1

    y = 0
    z = 0
    while y+1 < len(your_list):
        success = True
        if your_list[y] + z != your_list[y+1]:
            success = False
        else:
            z = z + 1
        y = y + 1

def triangle_number():
    your_list = input("give me a list ").split(",")
    your_list = [int(x) for x in your_list]
    success = False
    answers = []
    for x in range(len(your_list)):
        for y in range(x+1, len(your_list)):
            for z in range(y+1, len(your_list)):
                if your_list[x] + your_list[y] > your_list[z]:
                    if your_list[x] + your_list[z] > your_list[y]:
                        if your_list[y] + your_list[z] > your_list[x]:
                            success = True
                            if your_list[y] == your_list[z] or your_list[x] == your_list[y] or your_list[x] == your_list[z]:
                                success = False
                if success == True:
                    answers.append((your_list[x], your_list[y], your_list[z]))
    print(answers)

def circle_problem():
    a = int(input("give me the first distance "))
    b = int(input("give me the second distance "))
    c = int(input("give me the third distance "))

    my_number = (a + b + c)/2
    answer_a = my_number - (c)
    answer_b = my_number - (a)
    answer_c = my_number - (b)
    print(answer_a, answer_b, answer_c)

def fill_board_diagonal():
    n = 11
    board = []
    for i in range(n):
        board.append([1] * n)

    for row in range(n):
        for col in range(n):
            if row == col:
                board[row][col] = 2
            elif row + col == n-1:
                board[row][col] = 2
    for i in range(n):
        print(board[i])

def up_to_squared_board():
    n = 6
    board = []
    for i in range(n):
        board.append([0] * n)

    col = 0
    row = 0
    for v in range(1, n * n + 1):
        board[row][col] = v
        col = col + 1
        if col >=n:
            col = 0
            row = row + 1

    for i in range(n):
        print(board[i])

def up_then_down_board():
    n = 6
    board = []
    for i in range(n):
        board.append([0] * n)
    up = False
    col = 0
    row = 0
    for v in range(1, n * n + 1):
        board[row][col] = v
        if up == False:
            row = row + 1
        else:
            row = row - 1
        if row >=n:
            row = n - 1
            col = col + 1
            up = not up
        elif row < 0:
            col = col + 1
            row = 0
            up = not up

    for i in range(n):
        print(board[i])

def matrix_up_Down():
    n = 9
    board = []
    for i in range(n):
        board.append([0] * n)
    col = 0
    row = 0
    directions = [0, 1, 2, 3]
    distance = n - 1
    direction = 0
    value = 1

    while value <= n * n:
        for step in range(distance):
            print(row, col)
            board[row][col] = value
            value = value + 1

            if direction == 0:
                row = row + 1
            elif direction == 1:
                col = col + 1
            elif direction == 2:
                row = row - 1
            elif direction == 3:
                col = col - 1
        direction = direction + 1
        if direction > 3:
            direction = 0
            distance = distance - 2
            row = row + 1
            col = col + 1
            if distance == 0:
                board[row][col] = value
                value = value + 1
    for i in range(n):
        print(board[i])

def sort_and_how_many_dictionary():
    numbers = [1, 4, 2, 30, -1]
    dt = {}
    min = numbers[0]
    max = numbers[0]
    end = []
    for number in numbers:
        if number in dt:
            dt[number] = dt[number] + 1
        else:
            dt[number] = 1
    for t in range(len(numbers)):
        if max < numbers[t]:
            max = numbers[t]
        if min > numbers[t]:
            min = numbers[t]
    for number in dt:
        print(number, ':', dt[number])
    for x in range(min, max+1):
        if x in dt:
            for y in range(1, dt[x]+1):
                print(x)

def calculate_trees():
    trees = int(input("how many trees are there? "))
    distance = int(input(("what is the distance between marked trees? ")))
    real = distance
    number = int(input("how many times do you want your code repeated? "))
    direction = True
    my_list = []
    start = 1
    counter = 0
    while counter <  number:
        my_list.append(start)
        if distance == 10:
            distance = real
        if direction == True:

            start = start + distance
            if start > trees:
                direction = not direction
                counter = counter + 1
                start = trees - (start - trees)
                distance = distance + 1
        elif direction == False:

            start =  start - distance
            if start < 1:
                direction = not direction
                counter = counter + 1
                start = 1 + (1 - start)
                distance = distance + 1

    print(my_list)

def lcm_hcf():
    def hcf(a, b):
        while a != b:
            if a > b:
                a = a - b
            elif b > a:
                b = b - a

        return a

    def lcm(a, b):
        temp = hcf(a, b)
        number = (a * b) // temp
        return number

    max = -1
    maxx = -2
    maxy = -1
    mylist = [4, 5, 6, 9]
    for x in mylist:
        for y in mylist:
            if x != y:
                a = lcm(x, y)
                if a > max:
                    max = a
                    maxx = x
                    maxy = y

    print('({}, {}) = {}'.format(maxx, maxy, max))

def x_y_problem():
    sum = 0
    for x in range(0, 10):
        for y in range(0, 10):
            thing = int('24{}8{}'.format(x, y))
            if thing % 5 == 0 and thing % 7 == 0 and thing % 9 == 0:
                print(thing)

def algebra_code():
    for v in range(1,10):
        for y in range(0,10):
            if y != v:
                for a in range(1, 10):
                    if a != v and a != y:
                        for n in range(1, 10):
                                if n != v and n != y and n != a:
                                    for h in range(0, 10):
                                        if h != v and h != y and h != a and h != n:
                                            number = (a * 100) + (n * 10) + (h * 1)
                                            next_number = (v * 10) + (y * 1)
                                            ans = (n * 10) + y
                                            if number % next_number == 0:
                                                if number // next_number == ans:
                                                    print(a , n, h, v, y)

def b1():
    for x in range(1,10):
        for y in range(0,10):
            number =  (x * 1000) + (1 * 100) + (2 * 10) + y
            if number % 15 == 0:
                print(number)

def b5a():
    for a in range(1,10):
        for b in range(0, 10):
            one = (a * 10) + b
            two = (b * 10) + a
            distance = (one // 4) * 3
            if two == one + distance:
                print(one)

def split_list_to_two():
    n_list = input("give me a list of numbers ").split(",")
    n_list = [int(x) for x in n_list]
    success = False
    my_sum = sum(n_list)
    thingy = my_sum // 2
    stuff = []
    for x in range(len(n_list)):
        for y in range(x+1,len(n_list)):
             if x != y:
                if n_list[x] + n_list[y] == thingy:
                    success = True
                    stuff.append(n_list[x])
                    stuff.append(n_list[y])
    if success == True:
        print(stuff)
    else:
        print("NOOOOOOO!!!!@!@!!@")

def numbers():
    n_list = input("give me a list of numbers ").split(",")
    n_list = [int(x) for x in n_list]
    t = 0
    success = False
    for n in range(len(n_list)):
        for p in range(n + 1, len(n_list)):
            if n_list[n] == n_list[p]:
                t = 1
                print("NONONONONONONOONONONO")
    if t == 0:
        if len(n_list) == 9:
            one = n_list[0], n_list[1], n_list[2]
            a = sum(one)
            two = n_list[3], n_list[4], n_list[5]
            b = sum(two)
            three = n_list[6], n_list[7], n_list[8]
            c = sum(three)
            four = n_list[0], n_list[4], n_list[8]
            d = sum(four)
            five = n_list[2], n_list[4], n_list[6]
            e = sum(five)
            six = n_list[0], n_list[3], n_list[6]
            f = sum(six)
            seven = n_list[1], n_list[4], n_list[7]
            g = sum(seven)
            eight = n_list[2], n_list[5], n_list[8]
            h = sum(eight)
            print(a, b ,c ,d ,e ,f ,g ,h)
            if a == b == c == d == e == f == g == h:
                success = True
    if success == False:
        print("NONONONONONONONONONONONONONONONONONONONO")
    else:
        print("YAYAYAYAYAYAYAYAYAYAYAYAYAYAYAYYAYYAYYAY")

def code_string():
    first_string = input("give me a string ")
    second_string = input("give me the secret string ")
    for x in range(len(second_string)):
        if second_string[x] == 'u':
            my_value = int(second_string[x+1])
            first_string = first_string[0:my_value-1] + first_string[my_value-1].upper() + first_string[my_value: ]
        if second_string[x] == 'l':
            my_value = int(second_string[x+1])
            first_string = first_string[0:my_value - 1] + first_string[my_value - 1].lower() + first_string[my_value:]
        if second_string[x] == 'c':
            my_value = int(second_string[x+1])
            if first_string[my_value].isupper():
                first_string = first_string[0:my_value - 1] + first_string[my_value - 1].lower() + first_string[my_value:]
            elif first_string[my_value].islower():
                first_string = first_string[0:my_value - 1] + first_string[my_value - 1].upper() + first_string[my_value:]
        if second_string[x] == 'd':
            my_value = int(second_string[x+1])
            first_string = first_string[0:my_value - 1] +  first_string[my_value:]
        if second_string[x] == 'a':         #this is a random code. you give a string like abcdef, and second_string must be u(upper), then the number
            my_value = second_string[x+1]  #position of the letter you want to change: abcdef, u2, = aBcdef     l = lower, c = change, d = delete, and a = add

            first_string = first_string[0: ] + my_value
    print(first_string)


def hcf():
    def hcf(a, b):
        while a != b:
            if b > a:
                b = b - a
            else:
                a = a - b
        return a #this code will find the highest common factor of 2 numbers

    def tiny_hcf(a):
        min = 100000000000000000000000000000
        for x in range(len(a)):
            for y in range(x + 1, len(a)):
                    if hcf(a[x], a[y]) < min:
                        min = hcf(a[x], a[y])
                        vx = a[x]
                        vy = a[y]
        return min
    a = [45, 25, 29, 35]
    success = False
    number = 0
    for t in range(number, len(a)):
        b = a[0:t] + a[t + 1:]
        if tiny_hcf(b) != 1:
            success = True
            thing = a[t]
    if success == True:
        print(thing)
    else:
        print("NO!")

def fibonacci_with_def(n):

    k = 1
    s = 1
    p = [1, 1]



    for m in range(n - 2):
        e = k + s
        k = s
        s = e
        p.append(s)

    return(s)

def def_s():
    def fibonacci_recursive(n):
        if n < 3:
            return 1
        else:
            return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

    print(fibonacci_recursive(4))

    def exponential(n):
        a = 1
        t = range(1, n + 1)
        for x in t:
            a = a * x
        return a
    print(exponential(5))

    def expo_recu(n):
        if n == 1:
            return 1
        else:
            return n * expo_recu(n-1)
    print(expo_recu(4))

def rs():
    def repeat_string(a,b):
        z = []
        for x in range(len(a)):
            for y in range(len(b)):
                if a[x] == b[y]:
                    b = b[0:y] + b[y+1:]
                    z.append(a[x])
                    break
        return z
    print(repeat_string('dff','fe'))

def poop_pile():
    your_list = input("give me a list ").split(",")
    tally = 0
    for x in range(0,len(your_list)):
        for y in range(your_list[0,len(your_list)]):
            for z in range(your_list[0,len(your_list)]):
                for a in range(your_list[x]):
                    if z == a:
                        tally = tally + 1
    if tally>tally:
        max = tally
    print(tally)

def m0st_c0mm0n_letters():
    def t(x,y):
        tally = 0
        for a in range(len(x)):
            for b in range(len(y)):
                if x[a] == y[b]:
                    y = y[0:b] + y[b+1:]
                    tally = tally + 1
                    break

        return tally

    your_list = input("give me a list ").split(",")
    d = your_list
    max = 0
    for f in range(len(your_list)):
        for g in range(len(your_list)):
            if f != g:
                if t(d[f], d[g]) > max:
                    max = t(d[f], d[g])
                    thing = d[f], d[g]
    print(thing, max)

def poop_pile():
    y_name = input("give me a list ").split(",")
    success = False
    space = -1
    for x in range(len(y_name)):
        for n in range(len(x) - 1, -1, -1):

            if (y_name[x])[n] == ' ':
                success = True
                space = n
        distance = (y_name[x])[0:space]

        y_name = y_name[space + 1: ] + ' ' + distance[0].upper() + distance[1:]

    print(y_name)

def name_thing_and_missing_numbers():
    y_name = input("give me a list ").split(",")
    names = []
    for x in y_name:
        for y in range(len(x)-1):
            if x[y] == ' ':
                surname = x[y+1:]
                firstname = x[0:y]
                names.append(surname)
    #print(sorted(names))

    numbers = ['0','1','2','3','4','5','6','7','8','9']
    y_string = input("give me a string ")
    final=[]
    my_str = ''
    for x in range(len(numbers)):
        if numbers[x] not in y_string:
            final.append(x)
            my_str = my_str + numbers[x]
    print(my_str)

#def code_and_number():
def number_ord_chr(number, y_string):
    new_string = ''

    for x in y_string:
        if ord(x) >= 97 and ord(x) <= 122:
            if ord(x) + number > 122:
                new_number = 122 - number
                other_num = ord(x) - new_number                #this code encodes your string by any number you want:
                                                            #you could enter number 2 and 'abc' to get 'cde'
                my_ord = 96 + other_num
            else:
                my_ord = ord(x) + number
        else:
            if ord(x) + number > 90:
                new_number = 90 - number
                other_num = ord(x) - new_number
                my_ord = 64 + other_num
            else:
                my_ord = ord(x) + number
        new_string = new_string + chr(my_ord)
    return new_string
    print(number_ord_chr(2,abc))

    coded_message = input("give me your coded message ")
    key_words = ["abc", "egi", "kos"]
    for x in range(0, 26):
        for y in key_words:
            if number_ord_chr(x, y) in coded_message:
                print(x)

def shortcut():
    for x in range(1000, 10000):
        number = str(x)
        if number[0] == number[3]:
            if x % 11 == 0 and x % 12 == 0:
                print(x)

def shortcut2():
    for x in range(1000, 10000):
        thousands_digit = x//1000
        ones_digit = x % 10
        if thousands_digit == ones_digit:
            if x % 11 == 0 and x % 12 == 0:
                print(x)
def shortcut3():
    for thousands_digit in range(2, 10, 2):
        for hundreds_digit in range(0, 9):
            for tens_digit in range(0, 9):
                number = thousands_digit * 1000 + hundreds_digit * 100 + tens_digit*10 + thousands_digit
                if number % 11 == 0 and number % 12 == 0:
                    print(number)

def guessnumber():
    numbers = [0]
    number = int(input('Enter a number '))
    while number != 0:
        if number > numbers[-1]:
            numbers.append(number)
        number = int(input('Enter a number '))

    print(numbers[1:])
    guess = int(input(' guess a number in the list  '))
    while guess != 0:
        check = False
        for x in range(len(numbers)):
            if guess == numbers[x]:
                check = True
                print('YAAAAAAAY at position {}'.format(x))

        if check == False:
            print('NOOOOOOOOOOO ')

        guess = int(input(' guess a number in the list '))

def prime_search():
    def is_prime(number):
        if number < 2:
            return (False, 0)
        tally = 0
        for x in range(2, (number//2)+1):
            tally = tally + 1
            if number % x == 0:
                return (False, tally)
        return (True, tally)
    def all_primes_between(a, b):
        primes_list = []
        hack = []
        for x in range(a, b+1):
            value = is_prime(x)
            if value[0]:
                primes_list.append(x)
            hack.append(value[1])
        return primes_list, sum(hack)


    print(all_primes_between(1, 20))

list_of_numbers = [1, 3, 4, 6, 9, 15, 16, 19, 23, 500, 1000]
value = int(input('Number = '))
check = False
first_index = 0
last_index = 10
middle_index = 5
while last_index - first_index > 1:
    if value > list_of_numbers[first_index] and value < list_of_numbers[middle_index]:
        last_index = middle_index
        middle_index = (first_index+last_index)//2
        if list_of_numbers[first_index] == value or list_of_numbers[middle_index] == value or list_of_numbers[last_index] == value:
            check = True

    elif value > list_of_numbers[first_index] and value > list_of_numbers[middle_index]:
        first_index = middle_index
        middle_index = (first_index+last_index)//2
        if list_of_numbers[first_index] == value or list_of_numbers[middle_index] == value or list_of_numbers[last_index] == value:
            check = True
    if list_of_numbers[first_index] == value or list_of_numbers[middle_index] == value or list_of_numbers[last_index] == value:
        check = True
        break
    print(first_index, middle_index, last_index)
if list_of_numbers[first_index] != value and list_of_numbers[middle_index] != value and list_of_numbers[last_index] != value:
    check = False
print(check)

def symmetry(i):
    i = [int(x) for x in i]
    success = True
    for p in range(len(i)//2):
        if i[p] != i[len(i) - (p + 1)]:
            success = False
    if success == True:
        print("Yay!")
    if success == False:
        print("NO!")


def binary_search(numbers, val):
    """
    return True if val is in numbers
    numbers is a sorted list
    """
    x = len(numbers)
    min = 0
    max = x - 1
    mid = max //2
    if val < numbers[min] or val > numbers[max]:
        return False
    if val == numbers[mid] or val == numbers[min] or val == numbers[max]:
        return True
    while min != mid:
        print(min, mid, max)
        if val > numbers[min] and val < numbers[mid]:
            max = mid
            mid = max//2
        elif val > numbers[mid] and val < numbers[max]:
            min = mid
            mid = (min + max) // 2
        if val == numbers[mid] or val == numbers[min] or val == numbers[max]:
            return True
    return False
numbers = [1, 3, 4, 5, 9, 11, 14, 17, 18]
n = len(numbers )
print(binary_search(numbers, 15)) # return True
#print(binary_search(numbers, 10)) # return False
#print(binary_search(numbers, 100)) # return False


























































































































