flyingpigs = 'Y'
while flyingpigs == 'Y':
    a = int(input('You are requested by Sir Poshface to print an integer '))
    b = int(input('Sir Poshface insists that you print another '))
    hotsuns = a
    coldmoons = b

    while  a != b:
        if b > a:
            b = b - a
        else:
            a = a - b

    purplecats = (hotsuns * coldmoons) // a
    print("The highest common factor of {} and {} is hereby {}".format(hotsuns, coldmoons, a))
    print("The lowest common multiple of {} and {} is hereby {} It is now the law that you must declare this is of great enjoyment! ".format(hotsuns, coldmoons, purplecats))
    flyingpigs = input(" We demand you try again! Do you agree? Y/N")
print("Oh no.. Sir Poshface is depressed now.")